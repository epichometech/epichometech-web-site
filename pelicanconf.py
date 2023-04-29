AUTHOR = 'Carl'
AUTHOR_EMAIL = 'jeremy@epichome.tech'
SITENAME = 'Epic Home Tech'
SITESUBTITLE = 'Where Great Tech Makes An Epic Home'
SITEURL = ''
ARTICLE_PATHS = ['articles']
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

PATH = 'content'
THEME = "themes/editorial-dark"

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('You can add links in your config file', '#'),
    ('Another social link', '#'),
)

CONTACTS = [
    ("Discord", "brands fa-discord", "https://discord.gg/dpC7FnEsar"),
    ("Email Us", "solid fa-envelope", "mailto:jeremy@epichome.tech?subject=Mail from Our Site")
]

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['plugins']
PLUGINS = ['enrich_author','enrich_category']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True