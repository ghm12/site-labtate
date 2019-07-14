#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from os import environ

AUTHOR = 'João Paulo Taylor Ienczak Zanette'
SITENAME = 'LABTATE'
THEME = 'theme'

if environ.get('LOCAL', '0') == '1':
    SITEURL = ''
else:
    SITEURL = 'https://jptiz.github.io/site-labtate'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Override URLs
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = '{category}/{slug}.html'
PAGE_SAVE_AS = '{category}/{slug}.html'

STATIC_PATHS = ['img']

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    'jinja2content',
]
