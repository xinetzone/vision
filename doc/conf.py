import sys
import os
from pathlib import Path

ROOT = Path('__file__').resolve().parents[1]
print(ROOT)
sys.path.extend([str(ROOT/'src')])
import vision

# The full version, including alpha/beta/rc tags
release = vision.__version__


def setup(app):
    app.add_object_type('confval', 'confval',
                        objname='configuration value',
                        indextemplate='pair: %s; configuration value')
    # theme_dir = vision.get_html_theme_path()
    # print(theme_dir.as_posix())
    # app.add_html_theme("vision", str(theme_dir))
    # # Update templates for sidebar
    # app.config.templates_path.append(str(theme_dir/"_templates"))

# -- Project information -----------------------------------------------------


project = 'vision'
copyright = '2022, xinetzone'
author = 'xinetzone'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'xyzstyle',
    'myst_nb',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    # 'sphinx.ext.autosectionlabel',
    'sphinx.ext.napoleon',
]

# application/vnd.plotly.v1+json and application/vnd.bokehjs_load.v0+json
suppress_warnings = ["mystnb.unknown_mime_type"]

# Add any paths that contain templates here, relative to this directory.
templates_path = [f'{ROOT}/doc/_templates'] # str(vision.get_html_template_path())

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'xyzstyle'
# html_theme_path = [f'{ROOT}/src/vision/themes']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [f'{ROOT}/doc/_static']
html_css_files = ["custom.css"]

html_logo = f'{ROOT}/doc/_static/images/logo.jpg'
# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = f'{ROOT}/doc/_static/images/favicon.jpg'

html_last_updated_fmt = '%Y-%m-%d, %H:%M:%S'

html_theme_options = {
    "footer_items": ["copyright", "last-updated", "sphinx-version", ],
}

intersphinx_mapping = {
    'python': ('https://daobook.github.io/cpython/', None),
    'sphinx': ('https://daobook.github.io/sphinx/', None),
    'peps': ('https://daobook.github.io/peps', None),
}

# MyST-NB 设置
# 如果你希望stderr和stdout中的每个输出都被合并成一个流，请使用以下配置。
# 避免将 jupter 执行报错的信息输出到 cmd
nb_merge_streams = True
nb_execution_allow_errors = True
nb_execution_mode = "cache" # "off"

# nb_mime_priority_overrides = [
#     ('html', 'text/plain', 0),  # 最高级别
#     ('latex', 'image/jpeg', None),  # 禁用
#     # ('*', 'customtype', 20)
# ]

# -- 国际化输出 ----------------------------------------------------------------
gettext_compact = False
locale_dirs = ['locales/']

# Napoleon 设置
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True
napoleon_type_aliases = None
napoleon_attr_annotations = True

# ``pydata-sphinx-theme`` 配置
# Define the json_url for our version switcher.
json_url = 'https://xinetzone.github.io/vision/_static/switcher.json'

version = release

switcher_version = f'v{version}'
if "dev" in version:
    switcher_version = "dev"
elif "rc" in version:
    switcher_version = version.split("rc")[0] + " (rc)"

autosummary_generate = True
html_theme_options = {
    "footer_items": ["copyright", "last-updated", "sphinx-version", ],
    "github_url": "https://github.com/xinetzone/vision",
    "use_edit_page_button": True,
    "navbar_end": ["theme-switcher", "version-switcher", "navbar-icon-links"],
    "switcher": {
        "json_url": json_url,
        "version_match": switcher_version
    },

}

html_context = {
    "github_user": "xinetzone",
    "github_repo": "vision",
    "github_version": "main",
    "doc_path": "doc",
}

html_sidebars = {
    "contribute/index": [
        "search-field",
        "sidebar-nav-bs",
        "custom-template",
    ],  # This ensures we test for custom sidebars
    "demo/no-sidebar": [],  # Test what page looks like with no sidebar items
}
