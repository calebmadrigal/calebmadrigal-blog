#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os.path

####### High-level stuff #######
AUTHOR = u'Caleb Madrigal'
SITENAME = u'Caleb Madrigal'
SITESUBTITLE = u'Programming and Poetry'
SITEURL = u'http://calebmadrigal.com'
TIMEZONE = 'US/Central'
DEFAULT_LANG = u'en'
SUMMARY_MAX_LENGTH = 128

####### URL Setup #######

# ARTICLES; Make article urls be in the form: "calebmadrigal.com/map-in-ios/"
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

# TAGS; Make tag urls be in the form: "calebmadrigal.com/tags/python"
TAGS_SAVE_AS = 'tags.html'
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

# CATEGORIES; Make category urls be in the form: "calebmadrigal.com/topics/python"
CATEGORY_URL = 'topics/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

# PAGES; Make pages urls be in the form: "calebmadrigal.com/pages/about-me/"
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Disqus and Google analytics
DISQUS_SITENAME = 'calebmadrigal'
GOOGLE_ANALYTICS = 'UA-31212664-1'

# Copying static files
STATIC_PATHS = ['images', 'code']

CODE_DIR = 'code'
NOTEBOOK_DIR = 'code'

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'}
}

# Feed generation
FEED_ALL_ATOM = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.rss.xml'
TRANSLATION_FEED_ATOM = None
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'

# Social widget
SOCIAL = (('github', 'http://github.com/calebmadrigal'),
          ('linkedin', 'http://www.linkedin.com/pub/caleb-madrigal/40/489/2b8/'))

####### Themes and Plugins #######
THEME = '../pelican-octopress-theme/'
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']

####### Misc #######
DEFAULT_PAGINATION = False
SEARCH_BOX = True

####### IPython Notebook Stuff #######
EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

