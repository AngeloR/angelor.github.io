---
date: 2025-01-29
tags:
  - publish
  - development
  - tutorial
authors:
  - angelor
title: Understanding Pagination
summary: Pagination techniques and trade-offs
lastmod: 2025-02-14T15:45:12.879Z
---
# Pagination

Pagination is an interesting topic. Actually, to be fair, most topics are interesting topics once you make it past the surface. Pagination is no exception. The goals of pagination are simple: returning every since item in a list can be challenging along many axis, so it's easier to split that list into chunks and return the chunks.

There are really 2 major kinds of pagination - offset and cursor. They both have their pros and cons and it really is a question of understanding your system and the scale at which you're operating that makes one more feasible over another.

All pagination options include the idea of a `limit` or `pageSize`. We're mostly going to ignore this as it's just the number of items that you are going to be returning. At low volumes this number doesn't matter too much - we'll just set it at 25 for the duration of this conversation.

## Offset Pagination

`GET /items?limit=25&offset=50`\
This type of pagination is the one that people are most familiar with. With offset pagination you are really just specifying how far from the beginning of your collection you need to look. So if you have 100 items in your list, you might provide an offset of `50` which says 'start at item number 50 and then give me the next 25 items'. In some implementations we hide the `offset` and instead use a `page` which really just means everyone needs to do some math to swap between page and offset. Page just ends up being a human-readable way to share the offset.

This is a great approach for when you're just starting out. All SQL implementations have limit/offset equivalents to segment the returned data. It is trivial to map your url params to these and give you pagination with almost no overhead. But low implementation costs mean you have to pay for it somewhere, and in this scenario you pay for it implicitly.

The thing about all pagination is that the only way to reliably paginate is if you have a deterministic order to your list. Often, that means first SORTING your list along some factor, before you apply pagination. This is where you'll often run into problems. In order to use the offset pagination system you actually have to sort every single element in your list into the same order before you perform your offset. This isn't so bad when you have 100 items... but if you have 2 million it can get a lot more expensive. At this point sorting the items is going to take you much longer than your users can reasonably wait.

There's trade-offs we can make here for sure. If you're using a relational database you can ensure that the sort column is an auto-incrementing btree index. This ensures that new items are always added to the END of the index, and it will maintain some semblance of order, as long as your sort on the correct columns. In most cases this looks like sorting on your integer primary key.

### Backend Example

```typescript
// Backend: Express.js + PostgreSQL
import express from 'express';
import { Pool } from 'pg';

const app = express();
const pool = new Pool({
  user: 'your_user',
  host: 'your_host',
  database: 'your_db',
  password: 'your_password',
  port: 5432,
});

app.get('/items', async (req, res) => {
  try {
    const limit = parseInt(req.query.limit as string) || 25;
    const offset = parseInt(req.query.offset as string) || 0;
    
    const { rows } = await pool.query(
      'SELECT * FROM items ORDER BY id ASC LIMIT $1 OFFSET $2',
      [limit, offset]
    );
    
    res.json({
      items: rows,
      pagination: {
        total: parseInt(count, 10),
        limit,
        offset,
        nextOffset: offset + limit < count ? offset + limit : null,
        prevOffset: offset - limit >= 0 ? offset - limit : null,
      }
    });
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.listen(3000, () => console.log('Server running on port 3000'));

```

### Frontend Example

```tsx

// Frontend: React + Fetch API
import { useState, useEffect } from 'react';

interface Item {
  id: number;
  name: string;
}

interface Pagination {
  total: number;
  limit: number;
  offset: number;
  nextOffset: number | null;
  prevOffset: number | null;
}

export default function PaginatedList() {
  const [items, setItems] = useState<Item[]>([]);
  const [pagination, setPagination] = useState<Pagination | null>(null);
  const [offset, setOffset] = useState(0);
  const limit = 25;

  useEffect(() => {
    fetch(`/items?limit=${limit}&offset=${offset}`)
      .then(res => res.json())
      .then(data => {
        setItems(data.items);
        setPagination(data.pagination);
      });
  }, [offset]);

  return (
    <div>
      <ul>
        {items.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
      <div>
        <button
          onClick={() => setOffset(pagination?.prevOffset ?? 0)}
          disabled={!pagination?.prevOffset}
        >
          Previous
        </button>
        <button
          onClick={() => setOffset(pagination?.nextOffset ?? offset)}
          disabled={!pagination?.nextOffset}
        >
          Next
        </button>
      </div>
    </div>
  );
}

```

## Cursor Pagination

This tends to be the kind of pagination that large systems use - instead of fully abstracting away the pointer to which row in the database you are, instead you use that pointer as the "page". Whenever a user makes a request, they pass along the "cursor" that tells you what the last thing they saw is. Then you can reach out and get the next set of items.

Again, same caveats as before in terms of sorting, but you you can rely on time-based IDs as the cursor.

For example, MongoDBs OID https://www.mongodb.com/docs/manual/reference/method/ObjectId/ has a timestamp component that ensures that object IDs are always incrementing. And so you could potentially use them as cursor pointers. UUIDv7 are similar in this way https://uuid7.com/

From a security standpoint you don't really want to expose these directly, so you may institute a cache with a non-guessable key that is passed as the pointer, and the value for that key in the cache is your actual cursor.

In the example below we are assuming that the cursor is a field called `created_at` which is what we actually give to the client. As long as this is a btree based index in our database we can ensure that new additions will always be appended and the call to "sort" by the index remains quick and performant.

### Backend

```typescript
// Backend: Express.js + PostgreSQL (Cursor-Based Pagination)
import express from 'express';
import { Pool } from 'pg';

const app = express();
const pool = new Pool({
  user: 'your_user',
  host: 'your_host',
  database: 'your_db',
  password: 'your_password',
  port: 5432,
});

app.get('/items', async (req, res) => {
  try {
    const limit = parseInt(req.query.limit as string) || 25;
    const cursor = req.query.cursor as string | null;
    
    let query = 'SELECT * FROM items ORDER BY created_at ASC LIMIT $1';
    let params: any[] = [limit];

    if (cursor) {
      query = 'SELECT * FROM items WHERE created_at > $1 ORDER BY created_at ASC LIMIT $2';
      params = [cursor, limit];
    }

    const { rows } = await pool.query(query, params);
    
    const nextCursor = rows.length > 0 ? rows[rows.length - 1].created_at : null;
    
    res.json({
      items: rows,
      pagination: {
        limit,
        nextCursor,
      }
    });
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.listen(3000, () => console.log('Server running on port 3000'));


```

### Frontend

```tsx
// Frontend: React + Fetch API (Cursor-Based Pagination)
import { useState, useEffect } from 'react';

interface Item {
  id: number;
  name: string;
  created_at: string;
}

interface Pagination {
  limit: number;
  nextCursor: string | null;
}

export default function PaginatedList() {
  const [items, setItems] = useState<Item[]>([]);
  const [pagination, setPagination] = useState<Pagination | null>(null);
  const [cursor, setCursor] = useState<string | null>(null);
  const limit = 25;

  useEffect(() => {
    const url = cursor ? `/items?limit=${limit}&cursor=${cursor}` : `/items?limit=${limit}`;
    fetch(url)
      .then(res => res.json())
      .then(data => {
        setItems(prev => [...prev, ...data.items]);
        setPagination(data.pagination);
      });
  }, [cursor]);

  return (
    <div>
      <ul>
        {items.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
      <div>
        <button
          onClick={() => setCursor(pagination?.nextCursor ?? null)}
          disabled={!pagination?.nextCursor}
        >
          Load More
        </button>
      </div>
    </div>
  );
}

```
