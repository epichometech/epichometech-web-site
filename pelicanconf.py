AUTHOR = 'Carl'
AUTHOR_EMAIL = 'jeremy@epichome.tech'
SITENAME = 'Epic Home Tech'
SITESUBTITLE = 'Where Great Tech Makes An Epic Home'
SITEURL = 'https://dev.epichome.tech'
ARTICLE_PATHS = ['articles']
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

DELETE_OUTPUT_DIRECTORY = True

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

STATIC_PATHS = [
    'images',
    'extra',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.svg': {'path': 'favicon.svg'},
    'extra/logo-256x256.svg': {'path':'logo-256x256.svg'},
    'extra/logo-256x256.png': {'path':'logo-256x256.png'},
}

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
    ("Github", "brands fa-github", "https://github.com/epichometech"),
    ("Email Us", "solid fa-envelope", "mailto:jeremy@epichome.tech?subject=Mail from Our Site"),
]

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['plugins']
PLUGINS = ['enrich_author','enrich_category']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True