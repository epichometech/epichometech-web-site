"""
Summary
-------
This plugin allows easy addition of category information
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
    readCategories = {}
    
    # run reader on all content/category/*.markdown
    for file in generator.get_files(os.path.join(generator.settings['PATH'],'category')):
        parsedCategory = generator.readers.read_file(base_path=path, path=file)
        readCategories[parsedCategory.name] = parsedCategory
    for category, _ in generator.categories:
        if category.name in readCategories.keys():
            for key, value in readCategories[category.name].metadata.items():
                if key != 'name':
                    setattr(category, key, value)
                if getattr(readCategories[category.name], 'content') is not None:
                    setattr(category, 'content', readCategories[category.name].content)

def register():
    signals.all_generators_finalized.connect(run_plugin)

