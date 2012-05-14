#!/usr/bin/env python

"""
Wrapper around pip to install python distributions within Homebrew.
"""

__version__ = '0.4.0'

import re
import os
import shutil
import argparse
import tempfile

HOMEBREW_CELLAR = os.environ.get("HOMEBREW_CELLAR")

def main(args):
    for package in args.packages:
        # Just the name part of the package (no version info)
        # Django==1.4 -> Django
        package_name = re.search(r'^(?P<name>[\w.-]+)', package).group('name')
        assert package_name, "Invalid package name: '%s'" % package

        # Directory in /usr/local/Cellar it gets installed to
        # Django==1.4 -> pip-django
        cellar_package_name = "pip-%s" % package_name.lower()

        if args.upgrade:
            os.system("brew rm %s" % cellar_package_name)

        # Why hard-code the version to "pypi"? Because if you care about
        # versions you're probably already using virtualenv and not
        # installing distributions site wide.
        prefix = os.path.join(HOMEBREW_CELLAR, cellar_package_name, "pypi")
        build_dir = tempfile.mkdtemp(prefix='brew-pip-')

        cmd = ["pip", "install",
               "-v" if args.verbose else "",
               package,
               "--build=%s" % build_dir,
               "--install-option=--prefix=%s" % prefix,
               "--install-option=--install-scripts=%s" % os.path.join(prefix, "share", "python")]

        if args.verbose:
            print(" ".join(cmd))

        os.system(" ".join(cmd))

        if not args.keg_only:
            os.system("brew link %s" % cellar_package_name)

        shutil.rmtree(build_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='brew pip')
    parser.add_argument("--version", action="version", version="%(prog)s v" + __version__)
    parser.add_argument("-v", "--verbose", action="store_true", default=False, help="be verbose")
    parser.add_argument("-k", "--keg-only", action="store_true", default=False, help="don't link files into prefix")
    parser.add_argument("-u", "--upgrade", action="store_true", default=False, help="upgrade the package")
    parser.add_argument("packages", nargs='+', help="name of the package(s) to install", metavar="package")
    main(parser.parse_args())
