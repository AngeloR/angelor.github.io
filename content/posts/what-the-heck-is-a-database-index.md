---
title: What the heck is a Database Index?
summary: Explaining database indices
date: 2020-04-29T16:21:29-04:00
draft: false
tags:
  - explanation
  - database
  - publish
lastmod: 2024-12-12T05:30:56.492Z
---
When you do a standard `select * from table_name where columns=some_value` from a table.. the database has no idea where IN the table that data exists. In order to figure out which rows in the table it needs to return to you (based on your where clause), it looks through the rows in the table. Of course, if you don't set a limit clause, it has to look through EVERY single entry in the table because it doesn't know where/how-many instances of a particular value it might find. This is a pretty common problem. Think of a standard `users` table

```
+-------------------+
|       users       |
+-------------------+
|                   |
| id (int)          |
| username (string) |
| password (string) |
|                   |
+-------------------+
```

In this scenario there are a couple different uses of this table .

1. We are registering a user (inserting a row)
2. A user might be changing their password (updating a row)
3. A user is logging in (reading a row)

In a table without any indices when logging in we only know the users username and password. We have to run a `select * from users where username = ?` on the database. Even if we add a `limit 1` to our query, the database still needs to scan through every single row in our database until it finds one (or more) that matches our filter.

If you create an index on a particular column in the table, it serves as a lookup. If you look for a row where a particular indexed column matches a value.. the database doesn't need to scan the table, it can look at the index. You can think of an index exactly the same as as you would an index in a book. If you want to know where a word in the book occurs you have two choices.

1. You can either flip through the entire book until you see what you're looking for
2. Consult the index, which tells you which page in the book you need to look at.

Once you tell the database that you want a particular column to have an index, you don't need to do anything else. The database will ensure that the index is kept up to date (as you modify the data in the table). You also don't need to change anything about how you're accessing the data - (IE: you don't need to modify your queries).

Ok - so it sounds like indexes are pretty awesome right? If it speeds up looking things up, why don't we create an index on every column?

Well, like everything - there's a caveat. READING data from the table is very quick with an index.. but Creating, Updating, and Deleting data becomes a bit slower. This is because the database needs some additional time to update the index with the new data. So it's a bit of a balancing act. The more indices you have on a table.. the slower it becomes to write data to that table (insert/update/delete). You want to take a look at your table and how you're using the data in your table and create the index carefully.

Because of this, you can't really have a "rule" on when to create an index - you'll want to monitor your database and create them based on your investigations. Of course, it's never that easy - the more data IN the table when you create the index the longer it will take to create. It doesn't sound too bad - but if you have hundreds of thousands of rows in a table.. it can take a few minutes to create the index, during which your application will need to be down. So you need to be somewhat pre-emptive in creating your indices.. but also you can't go overboard.. but also there isn't really a guide on when to create an index. How wonderful.

As you progress in your database tuning/development life you'll find use-cases where it makes sense to have an index from the start. For example, most "user" tables will have an index on the username column. This is something that you can then take and implement on your next project!

## Further Reading

I really recommend you peruse this documentation from mysql on what an index is. While you may be using Postgres/MSSQL - the core concepts of what an index is remains the same. https://dev.mysql.com/doc/refman/5.7/en/mysql-indexes.html
