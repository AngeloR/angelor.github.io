---
title: "Moving to Hugo and GitHub Pages"
Description: "Moving to Hugo"
date: 2020-06-03T14:00:00-04:00
draft: false
tags: ["general", "hugo", "github"]
---

## Goal

I've been running my blog over on Ghost[^1] for a few years now. I really don't have a lot of issues with it, except for the fact that I have to manage the server itself. I've been running a small Digital Ocean VPS for a number of years where I host my blog. Ghost itself goes through a lot of updates and keeping the application up to date was starting to become a hassle. 

I was keen to move to a solution where I could

- Write my posts in markdown
- Not have to worry about hosting/management

After looking at a few different solutions I ended up settling on a static site that was hosted through GitHub. The benefits of this was that 

- I could have all my content stored on GitHub.
- I could utilize GitHub pages to serve the site with a custom domain name (with SSL)
- I wouldn't need to keep everything up to date
- I could re-purpose my VPS for other things



Of course, not all static sites are created the same. I specifically settled on Hugo to power my static site.

## Hugo
Unlike more traditional blogging software (WordPress, Ghost, etc.) which saves your posts in a database, Hugo[^2] generates a bunch of static files (HTML) for each post. By doing this you're still able to have the more complex features (tagging, drafts, pagination, themeing, etc.) but because Hugo pre-processes everything, you're just left with a bunch of HTML files that represent your site. Once you're happy, you can just sync the generated files with your server. In my case, I'm simply able to `git add` and `git push` my content to GitHub.

### Dynamic Blogging Platforms
Lets look at Wordpress to contrast Hugo. WordPress is the most used blogging software in the world and has the following requirements: 
- PHP
- MySQL

The implicit requirement is also a server that supports these two. That means you are either relying on a 3rd party host that manages the server and just exposes the Wordpress interface... or you are managing that server yourself. 

Most blogging systems work this way - Some language requirement, and some database system for storing the data you create. 

However, there's lots of additional caveats that you aren't normally aware of, that tend to bite you later:  
- You need to run a web server, either Apache or Nginx
- You need to keep the server itself up to date (security patches)
- You need to keep Apache|Nginx/PHP/MySQL up to date (security patches)
- You need to manage database backups (what happens if your server crashes)
- You need to keep WordPress up to date.

That's a heck of a lot of stuff for something that's supposed to be easy. And I just picked WordPress because it's popular. Almost every blogging system is the same way. 

Except for static site generators.

### Static Site Generators
Static Site Generators are a different way to approach blogging that merges more recent tooling with traditional delivery methods. That's just a fancy way of saying Static Site Generators give you some tooling to generate a bunch of HTML documents that represent your site. 

With Hugo, I install hugo locally.. write some markdown for my posts, and then use Hugo to generate the HTML for my site. With this, we bring our "management" layer down to:  
- Hugo
- Web server (nginx/apache)
- The hosting server

Hugo runs locally, so the surface of attack is pretty minimal. There's nothing really wrong with running an outdated version of Hugo except you won't get the most recent features/bug fixes. But there's no security implications of doing so. 

Since the output from Static Site Generators is just .. static content it can be hosted anywhere. You can use a hosting provider, a VPS, S3+CloudFront, or.. GitHub Pages!

## GitHub Pages
GitHub pages is a feature of GitHub that is available to all accounts, regardless of subscription. GitHub pages allows you to serve static content from any repository you'd like. They have some rules around how you need to organize your code and how to configure your site (project vs. main) but it's all relatively straight forward. 

I haven't really hosted much on GitHub pages, but it's very easy - They also have a great walkthrough page[^3] that shows you how to configure the kind of Static Site you want to host.



## Project Configuration

I'm not going to go into too much detail, because both Hugo and GitHub have very good introductions, but this should be enough to get a site running.



### Installing Hugo

Installing Hugo can be done from a terminal in your chosen operating system. There are alternate installation instructions available if you don't have brew installed or if you don't have a mac[^4]. 

```bash
brew install hugo
```



### Setup Hugo

Open up your terminal, and navigate to the place you want to store your website. Then you can run the following command:

```bash
hugo new site mysite
```

This creates a new folder called `mysite` that contains the raw files for your static site. At this point you don't have anything generated just the files that will eventually be compiled into your static site. 

You can install a theme by doing the following:

```bash
git init
git submodule add https://github.com/budparr/gohugo-theme-ananke.git themes/ananke
```

You can actually choose whatever theme you would like from https://themes.gohugo.io/  [^5]and just replace the `git submodule` line with the instructions from your theme.



Line 1 creates a git repository in the `mysite` directory. We want this because themes in Hugo are installed via `git submodule` which clones a particular repository into the current one. It also allows you to save the raw site (before static generation) to git!



Now it's time to head over to your `config.toml` file and set up the defaults for your website. My config file looks like this. You only really need the configurations on the first 9 lines. The rest are just further configurations[^6] that I've made.

```toml
baseURL = "https://xangelo.ca"
theme = "plain"
title = "Xangelo.ca"
author = "Angelo R"
copyright = "Copyright © 2011 - 2020"
paginate = 15
languageCode = "en-us"
enableInlineShortcodes = true
footnoteReturnLinkContents = "^"

[params]
subtitle = "Technical musings and other tidbits"

[markup]
[markup.highlight]
lineNos = true
lineNumbersInTable = true
style = "vs"
tabWidth = 2
[markup.tableOfContents]
endLevel = 3
ordered = true
startLevel = 2
```





### Create and test!

Hugo ships with a built in server that allows you to preview what your site will end up looking like, you can start it up with:

```bash
hugo server -w
```

This creates the server and the `-w` flag sets it to "watch". Any changes that are made will automatically reload the server and also reload the site. You can visit this site by navigating to `https://localhost:1313` in your browser.

You can create a new post by using `hugo new posts/welcome.md`. This creates a new Markdown file in the `posts/` directory. 

You can go ahead and edit that file - saving it will cause Hugo to live reload the website.



### Publish your site!

Once you're happy with your stuff, you can turn off the live-reloading server and run the `hugo` command. This parses all your information and generates the static files for your website. It will then put all this content in the `public/` directory. If you followed the instructions from earlier around setting up GitHub Pages, you can `cd` into the `public/` directory and set it up as another git repository. 

then running `git push `will publish your static files to whatever GitHub repository you configured to host the site.



## Wrapping Up

I haven't really dug too much into setting up GitHub pages because it's mostly clicking around the interface and the instructions for that are kept up to date [^3]. I highly recommend GitHub pages because of the ease of setting up

- Custom domain names (if you have your own domain it's trivial to point it to your GitHub pages site)
- Custom domain name SSL certificafte. Most places only allow you custom SSL certs if you use a subdomain, but GitHub lets you use a custom domain name.



I also highly suggest you spend some time going through the themes[^5] on Hugo to find one that you really like. There are so many and it's so easy to make new themes that you'll definitely find one you like. 



## Footnotes

[^1]: Ghost, a node.js based blogging engine: https://ghost.org/
[^2]: Hugo, static site generatror: https://gohugo.io
[^3]: GitHub Pages setup:  https://pages.github.com/
[^4]: Hugo installation: https://gohugo.io/getting-started/installing
[^5]: Hugo themes: https://themes.gohugo.io/  
[^6]: Hugo configuration options: https://gohugo.io/getting-started/configuration-markup