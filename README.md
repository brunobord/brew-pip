     _                                  _       
    | |__  _ __ _____      __     _ __ (_)_ __  
    | '_ \| '__/ _ \ \ /\ / /____| '_ \| | '_ \      brew pip installs python packages
    | |_) | | |  __/\ V  V /_____| |_) | | |_) |            inside of Homebrew.
    |_.__/|_|  \___| \_/\_/      | .__/|_| .__/ 
                                 |_|     |_|    

Install
-------

    brew install https://raw.github.com/edavis/brew-pip/master/brew-pip.rb

Usage
-----

    brew pip mercurial        # install the latest mercurial package
    brew pip django==1.2      # install django-1.2
    brew pip ~/tox-1.3.tar.gz # can install local packages, too
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

But doesn't everybody use virtualenv now?
-----------------------------------------

Why, yes, they do.  But that doesn't mean global installations are
totally useless.  What if you want to use a package *without* being
active in a virtualenv -- like say ipython?

With `brew pip` you can globally install a select few packages while
relying on virtualenv for everything else.

It's the best of both worlds.

Changelog
---------

*(In development)*

- Much more robust handling of different package syntaxes
- Can install VCS packages

v0.3.0 *(2011-12-26)*

- Add `brew-pip.rb` for Homebrew installation
- Can accept local source distributions for installation

v0.2.0 *(2011-12-25)*

- Use pip directly, instead of creating temporary formula files.
