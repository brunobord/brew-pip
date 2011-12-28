# Homebrew requires any external commands be named 'brew-<cmd>'; so
# the lack of a .py extension and hyphen in the middle make it somewhat
# hard to test properly.
#
# For this reason I create a symlink in lib/ instead.

from nose import tools
from lib.brew_pip import get_package_info

def test_get_package_info():
    tests = [
        ('Django', ('django', '1.3.1')),
        ('django', ('django', '1.3.1')), # lowercase, too
        ('Django==1.2', ('django', '1.2')),
        ('Django>=1.2', ('django', '1.3.1')),
        ('./transmissionrpc-0.9.tar.gz', ('transmissionrpc', '0.9')),
        ('./transmissionrpc-0.9.tar.bz2', ('transmissionrpc', '0.9')),
        ('transmissionrpc-0.9.tar.gz', ('transmissionrpc', '0.9')),
        ('./transmissionrpc-0.9.zip', ('transmissionrpc', '0.9')),
        ('~/src/transmissionrpc-0.9.tar.gz', ('transmissionrpc', '0.9')),
        ('http://example.com/transmissionrpc-0.9.tar.gz', ('transmissionrpc', '0.9')),
        ('git+https://github.com/edavis/django-memcached#egg=django-memcached2', ('django-memcached2', 'HEAD')),
        ('git+https://github.com/edavis/django-memcached@c5334ba72661cb7e8364713240f777b2dcbb457e#egg=django-memcached2', ('django-memcached2', 'rev-c5334ba72661cb7e8364713240f777b2dcbb457e')),
        ('hg+https://bitbucket.org/blueluna/transmissionrpc@b2cd245b3af8#egg=transmissionrpc', ('transmissionrpc', 'rev-b2cd245b3af8')),
        ('hg+https://bitbucket.org/blueluna/transmissionrpc@release-0.8#egg=transmissionrpc', ('transmissionrpc', 'rev-release-0.8')),
        ('gitegginfo==0.3', ('gitegginfo', '0.3')),
        ('gitegginfo', ('gitegginfo', '0.3')),
    ]

    for s, answer in tests:
        info = get_package_info(s)
        tools.eq_(info, answer)

@tools.raises(AssertionError)
def test_missing_egg_raises_assertion_error():
    get_package_info("git+https://github.com/edavis/django-memcached")

@tools.raises(AssertionError)
def test_nonexistent_packages_raises_assertion_error():
    get_package_info("alksdjf949jla")
