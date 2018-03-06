# -*- coding: utf-8 -*-
#
# Connectors documentation build configuration file, created by
# sphinx-quickstart on Mon Feb  4 11:35:44 2013.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.


import ast
import sys
import os
import sphinx_bootstrap_theme

sys.path.append(os.path.abspath('_themes'))


MANIFEST_FILES = [
    '__manifest__.py',
    '__odoo__.py',
    '__openerp__.py',
]


def is_module(path):
    """return False if the path doesn't contain an odoo module, and the full
    path to the module manifest otherwise"""

    if not os.path.isdir(path):
        return False
    files = os.listdir(path)
    filtered = [x for x in files if x in (MANIFEST_FILES + ['__init__.py'])]
    if len(filtered) == 2 and '__init__.py' in filtered:
        return os.path.join(
            path, next(x for x in filtered if x != '__init__.py'))
    else:
        return False


def is_installable_module(path):
    """return False if the path doesn't contain an installable odoo module,
    and the full path to the module manifest otherwise"""
    manifest_path = is_module(path)
    if manifest_path:
        manifest = ast.literal_eval(open(manifest_path).read())
        if manifest.get('installable', True):
            return manifest_path
    return False


if os.environ.get('TRAVIS_BUILD_DIR') and os.environ.get('VERSION'):
    # build from travis
    repos_home = os.environ['HOME']
    deps_path = os.path.join(repos_home, 'dependencies')
    odoo_folder = 'odoo-10.0'
    odoo_root = os.path.join(repos_home, odoo_folder)
    build_path = os.environ['TRAVIS_BUILD_DIR']
else:
    # build from dev
    odoo_root = os.path.abspath('../../../../src')
    deps_path = os.path.abspath('../../..')
    build_path = os.path.abspath('../..')

addons_paths = []


def add_path(*paths):
    addons_paths.append(
        os.path.join(*paths)
    )


add_path(odoo_root, 'odoo', 'addons')
add_path(odoo_root, 'addons')
add_path(build_path)

deps_repos = [repo for repo in os.listdir(deps_path)
              if os.path.isdir(os.path.join(deps_path, repo)) and
              not repo.startswith('.')]

for repo in deps_repos:
    add_path(deps_path, repo)

addons = [x for x in os.listdir(build_path)
          if not x.startswith(('.', '__')) and
          is_installable_module(x)]

# sphinxodoo.ext.autodoc variables
sphinxodoo_root_path = odoo_root
sphinxodoo_addons = addons
sphinxodoo_addons_path = addons_paths
sys.path.append(build_path)


# -- General configuration --------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.viewcode',
              'sphinxodoo.ext.autodoc',
              ]

todo_include_todos = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# autodoc options
autodoc_member_order = 'bysource'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Odoo Magento Connector'
copyright = '2013-2015, Odoo Community Association (OCA)'

# The version info for the project you're documenting, acts as
# replacement for |version| and |release|, also used in various other
# places throughout the built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to
# documentation for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to
# some non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in
# the output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# -- Options for HTML output ------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation
# for a list of builtin themes.
html_theme = 'bootstrap'

# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see
# the documentation.
html_theme_options = {
    # Navigation bar title. (Default: ``project`` value)
    'navbar_title': "Odoo Magento Connector",

    # Tab name for entire site. (Default: "Site")
    'navbar_site_name': "Site",

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 2,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the
    # build will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "true",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "true",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "footer",

    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing with "" (default) or the name of a valid theme
    # such as "amelia" or "cosmo".
    #
    # Note that this is served off CDN, so won't be available offline.
    'bootswatch_theme': "united",
}

# Add any paths that contain custom themes here, relative to this
# directory.
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as
# html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the
# top of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon
# of the docs.  This file should be a Windows icon file (.ico) being
# 16x16 or 32x32 pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets)
# here, relative to this directory. They are copied after the builtin
# static files, so a file named "default.css" will overwrite the builtin
# "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names
# to template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default
# is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is
# True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages
# will contain a <link> tag referring to it.  The value of this option
# must be the base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'odoo-magento-connector-doc'


# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples (source
# start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'odoo-magento-connector.tex',
     'Odoo Magento Connector Documentation',
     'Odoo Community Association (OCA)', 'manual'),
]

# The name of an image file (relative to this directory) to place at the
# top of the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are
# parts, not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output -----------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'odoo-magento-connector',
     'Odoo Magento Connector Documentation',
     ['Odoo Community Association (OCA)'], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'Odoo Magento Connector',
     'Odoo Magento Connector Documentation',
     'Odoo Community Association (OCA)', 'Odoo Magento Connector',
     'Connector between Odoo and Magento',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'


# Example configuration for intersphinx: refer to the Python standard
# library.
intersphinx_mapping = {
    'python': ('http://docs.python.org/2.7', None),
    'connector': ('http://www.odoo-connector.com', None),
}
