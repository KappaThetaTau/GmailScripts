#!/usr/bin/env python

import os
import sys
import datetime


# For tutorial documentation
sys.path.append(os.path.abspath('../src'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
html_static_path = ['_static']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = '.rst'
master_doc = 'index'

year = datetime.date.today().year
project = 'Email Script'
copyright = '{:d}, Theta Tau - Kappa Chapter'.format(year)
author = 'Nathan Marasigan'
version = '0.1'
release = version

html_theme = 'alabaster'

html_sidebars = {
    '**': [
        'about.html',
        'localtoc.html',
        'navigation.html',
        'searchbox.html',
    ]
}

html_theme_options = {
    'github_user': 'nmarasign16',
    'github_repo': 'ttEmailScripts',
    'description': 'Email Script for Theta Tau - Kappa Chapter',
}
