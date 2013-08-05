#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os.path

AUTHOR = u'Caleb Madrigal'
SITENAME = u'Caleb Madrigal'
SITESUBTITLE = u'Welcome to my domain'
SITEURL = u'http://labs.calebmadrigal.com'

TIMEZONE = 'US/Central'

DEFAULT_LANG = u'en'

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
DISQUS_SITENAME = "calebmadrigallabs"

STATIC_OUT_DIR = ''
STATIC_PATHS = ['images', 'code']

FILES_TO_COPY = (
    ('extra/favicon.ico', 'favicon.ico'),
    ('extra/robots.txt', 'robots.txt'))
#FILES_TO_COPY = [('extra/favicon.ico', 'favicon.ico')]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'http://github.com/calebmadrigal'),
          ('linkedin', 'http://www.linkedin.com/pub/caleb-madrigal/40/489/2b8/'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '../pelican-octopress-theme/'
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']

FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'
SEARCH_BOX = True
