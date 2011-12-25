require 'formula'

class BrewPip < Formula
  url 'https://github.com/edavis/brew-pip/tarball/v0.2.0'
  homepage 'https://github.com/edavis/brew-pip'
  md5 '06698fa58becc6a53f5534fed857932b'

  def install
    bin.install 'bin/brew-pip'
  end
end
