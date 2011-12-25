homebrew + pip = brew-pip
=========================

`brew pip` installs python packages inside of Homebrew.

For example, `brew pip Django==1.3.1` installs all its files under
`/usr/local/Cellar/django/1.3.1`.  Those files, in turn, get symlinked
into `/usr/local/lib/python2.7/site-packages` and
`/usr/local/share/python` so you can easily make use of them.

Install
-------

    curl -s https://raw.github.com/edavis/brew-pip/master/bin/brew-pip > ~/bin/brew-pip
    chmod +x ~/bin/brew-pip

Or:

    git clone git://github.com/edavis/brew-pip ~/src/brew-pip
    ln -s ~/src/brew-pip/bin/brew-pip ~/bin/brew-pip

Only requirement is Python 2.7, Homebrew's default version of python.

Usage
-----

    brew pip mercurial        # install the latest mercurial package
    brew pip django==1.2      # install django-1.2
    brew pip -u django==1.3.1 # upgrade to django-1.3.1
    brew pip -k ipython       # install ipython, but don't link it (i.e., keg-only)
    brew rm django            # uninstallation taken care of by homebrew itself
    brew pip -h               # for help

Setup
-----

So python can load your installed libraries, you need to update your `PYTHONPATH`:

    export PYTHONPATH=$(brew --prefix)/lib/python2.7/site-packages

And for any scripts to be found, you need to update your `PATH`:

    export PATH=$PATH:$(brew --prefix)/share/python
