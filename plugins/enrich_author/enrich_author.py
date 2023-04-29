"""
Summary
-------
This plugin allows easy addition of author biography information
"""

from __future__ import unicode_literals
from pelican import signals
from pelican.generators import ArticlesGenerator
from pelican.readers import Readers
import os, logging

logger = logging.getLogger(__name__)

def run_plugin(generators):
    generator = None
    for item in generators:
        if isinstance(item, ArticlesGenerator):
            generator = item
    path = generator.settings['PATH']
    readAuthors = {}
    
    # run reader on all content/author/*.markdown
    for file in generator.get_files(os.path.join(generator.settings['PATH'],'author')):
        parsedAuthor = generator.readers.read_file(base_path=path, path=file)
        readAuthors[parsedAuthor.name] = parsedAuthor
    for author, _ in generator.authors:
        if author.name in readAuthors.keys():
            for key, value in readAuthors[author.name].metadata.items():
                if key != 'name':
                    setattr(author, key, value)
                if getattr(readAuthors[author.name], 'content') is not None:
                    setattr(author, 'content', readAuthors[author.name].content)

def register():
    signals.all_generators_finalized.connect(run_plugin)

