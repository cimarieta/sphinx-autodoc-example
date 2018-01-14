# First time using sphinx-autodoc

## Steps

* install sphinx by running `pip install sphinx`

* this by itself didn't work for me (Ubuntu 16.04), so I had to run: `apt install python3-sphinx`

* create a folder inside your project named `docs` and, from inside it,
run `sphinx-quickstart`. Make sure to answer `y` where autodoc is mentioned (default is `n`)

* edit `conf.py` to include the following lines (to guarantee sphinx will understand
google or numpy style syntax):
```
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',]

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
```

* it is possible to change the html template, also in the `conf.py` file. A good choice is:
```
html_theme = 'sphinx_rtd_theme'
```

* cd into the `docs` folder and run `sphinx-apidoc -f -o ../docs/source/ ../src/`

* then, run `make html`

* if it has worked, now you have a `build` folder, and your documentation webpages are there

* if it did not, it might be that your module is not visible to sphinx, so you can uncomment some lines
in `conf.py` file to add the path to your module:
```
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))
```

## Using [vim-pydocstring](https://github.com/heavenshell/vim-pydocstring)

* Add `Plugin 'heavenshell/vim-pydocstring'` to the list of vundle packages

* If you want to use another template, provide the path to it in the `.vimrc` file. For example:
```
" use numpy template
let g:pydocstring_templates_dir = '~/.vim/bundle/vim-pydocstring/test/templates/numpy'
```

* Use `:Pydocstring` or `<C-l>` in the definition line (or right above it) to get the docstring written
below the definition line. For example:
```
def classify_even(number):
    return (number % 2 == 0)
```
should turn into:
```
def classify_even(number):
    """classify_even

    Parameters
    ----------

    number :

    Returns
    -------
    """
    return (number % 2 == 0)
```
