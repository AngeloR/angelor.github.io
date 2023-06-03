---
title: "gitweb - a GitHub/GitLab alternative"
date: 2022-03-24T01:29:37-04:00
tags: ["git", "development", "dev tools", "gitweb"]
summary: Setting up your own git repo browser
---

## Owning Your Digital Space
Over the last year or so I've slowly pushed further and further into the idea of
owning your digital space. Part of that has been re-evaluating all of the
services online that I think of as "necessary". One of these such services has
been GitHub. 

The more I dive into development processes the more I find that they are all
centered around the idea that in order for you to be a "developer" it mostly
requires that you buy into the idea of centralized forges like GitHub/GitLab.
But these very ideas make it harder and harder to actually get work done. All
development over the last few years has been about dealing with changes that
GitHub has brought about. Don't get me wrong - GitHub really does have some
wonderful services and they've done a lot for visibility and getting people
involved in OS projects. 

But they definitely shouldn't be the only game in town.

In an attempt to take some control back from the major forges, I've been
experimenting with a small tool called gitweb.

## gitweb
gitweb is a very simple tool - it allows you to browse all the git repositories
within a specified folder. You simply install gitweb, point nginx over to it,
and edit a single configuration file. You immediately get  
- A browser for all local git projects
- A tree view for your repos with raw file previews
- Commit history w/ colorized diffs
- Snapshot downloads
- RSS feed tracking commit history
- Search (with regex) throughout your repos

For personal projects, or even for small collaborative projects gitweb provides
more than enough functionality.

The two features that I think are missing from gitweb are Issue Tracking and 
Merge Requests. I don't think these are necessarily features that have any place
in gitweb itself, but it means as a replacement for a centralized forge today,
you probably need to rely on additional tooling.


## Setting up gitweb
Actually setting up gitweb was surprisingly easy. 

### Installing gitweb
```bash
sudo apt install gitweb
```

### Configuring gitweb
The gitweb configuration file is located at `/etc/gitweb.conf`. Installing
gitweb automatically populates this file with some of the defaults. It's a very tiny
file and honestly you don't need to touch most of it to get going. The only
thing that's required is setting the `$projectroot`.

```inf
$projectroot = "/path/to/gitfolders";
```

### Configuring nginx
Most of the tutorials about getting gitweb going seem to be primarily apache
related. I haven't personally used apache in close to 10 years now - mostly
living in nginx land. Here's a very short snippet to get your nginx config going
to actually serve gitweb.

```nginx
server {
  server_name git.xangelo.ca;
  location /index.cgi {
    root /usr/share/gitweb/;
    include fastcgi_params;
    gzip off;
    fastcgi_param SCRIPT_NAME $uri;
    fastcgi_param GITWEB_CONFIG /etc/gitweb.conf;
    fastcgi_pass  unix:/var/run/fcgiwrap.socket;
  }

  location / {
    root /usr/share/gitweb/;
    index index.cgi;
  }
}
```
All the paths included are the default locations of things gitweb configures.
The entire block should work for you if you just change the `server_name`
directive.

## Further Customizing
Unfortunately not all the configuration options are specified in the
configuration file that's generated. Reading the source will get you a list
pretty quick but if you don't feel like it, here's a few other params I changed
up.

```inf
# sets the title in the <title></title> html tag
$site_name = "My Site";

# by default the root of your gitweb is called "projects". 
# I simply changed that to Home and explicitly set the url 
# that users get directed to when they click it
$home_link_str = "Home";
$home_link = "https://git.xangelo.ca";

# There's a small "Header" section above the project listing 
# that you can customize with whatever text you want. This 
# allows you to specify an html  file that should be used 
# in that area
$home_text = "/path/to/file.html";

# since all of these repos are mine, I don't list the owner
# so I've disabled this prop
$omit_owner = "1";
```

## Resources
- Git Docs: https://git-scm.com/docs/gitweb.html
- Gitweb Source: https://repo.or.cz/w/git.git/tree/HEAD:/gitweb/
- My projects: https://git.xangelo.ca
