author: Caleb Madrigal
comments: true
date: 2013-08-06 13:00:00
layout: post
slug: wordpress-to-pelican-reasons
title: Wordpress to Pelican Reasons
category: python
tags: python, ipython-notebook

I recently migrated my blog from [Wordpress](http://wordpress.org/) to [Pelican](http://docs.getpelican.com/en/3.2/).  Pelican is a static-site generating blog system which is written in Python and uses [Jinja2](http://jinja.pocoo.org/docs/) for templating.  I'll probably do a post about the migration process later, but for now, I'll just give **my reasons for moving to Pelican...**

### Data Longevity
I didn't want my blog data stored in a database; I vastly prefer it being stored in version-controlled Markdown format.

### Markdown
* I wanted to write blog posts in [Markdown](http://en.wikipedia.org/wiki/Markdown) (which is possible in Wordpress, but Wordpress isn't designed to use Markdown).
* I also get to use `vim` to write my blog posts now, which is much nicer than the Wordpress editor.

### Language
* I hate PHP, but love Python.  It worried me that my blog was sitting on a giant, ugly PHP stack.
* Also, because Pelican is in Python, the code base is much, much cleaner and customizations are much easier.

### Security
* Pelican outputs a static HTML/JS/CSS site, which exposes a much smaller attack surface than the large Wordpress stack.
* I had my Wordpress site hosted on a shared hosting environment, on which I didn't have HTTPS for my blog (so my Wordpress admin password was being transmitted in plain text).  With Pelican, I log in over ssh.

### Version Control
* With Pelican, my blog content and configuration is [stored in Github](https://github.com/calebmadrigal/calebmadrigal-blog), so I have full version control over everything.
* It's true that Wordpress has it's own version control, but I trust (and enjoy) git a lot more.

### Mobility
Because everything is in git, and because I only need basic static HTML webserver capabilities, I can host my site just about anywhere.  So I can easily change hosts if I see fit.

### Nice Octopress theme
The default Pelican theme is pretty bad, but I love the [Octopress](http://octopress.org) theme, which has been [ported](https://github.com/duilio/pelican-octopress-theme) to Pelican.

### Speed
[nginx](http://nginx.org/en/) serving static HTML/JS/CSS files is **very fast**.  Preliminary tests showed that my site would load **3-10x** faster than with wordpress.

### Staging changes and easy deployment
* In Pelican, I can make large changes to the entire blog, regenerate it, and run a staging server to verify that my changes work before ever deploying them.
* Pelican comes with a Makefile to make blog generation, testing, and deployment very easy
* The command to regenerate the blog is `make html`
* The command to run a staging server is `make serve` or `make devserver`
* The command to deploy is `make ssh_upload`

### Nicer syntax highlighting
Pelican has very nice `syntax highlighting` with [Pygments](http://pygments.org/)

See:

    # Result: 1.6180339887498947
    reduce(lambda acc,_: (acc+1.0)/acc, xrange(100), 1)

### Easy code file inclusion
Include code syntax:

    {% literal include_code python/liquid_tags_test.py lang:python %}

Result:

{% include_code python/liquid_tags_test.py lang:python %}

### Ability to embed IPython Notebooks

Thanks to [Jake VanderPlas](http://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/#This-Is-An-IPython-Notebook) [liquid_tags plugin](https://github.com/jakevdp/pelican-plugins/tree/liquid_tags/liquid_tags), I can embed an IPython Notebook like this:

    {% literal notebook ipython_notebook/EmbedNotebookExample.ipynb %}

Which looks like this:

{% notebook ipython_notebook/EmbedNotebookExample.ipynb %}


