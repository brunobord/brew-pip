require 'formula'

class BrewPip < Formula
  url 'https://github.com/edavis/brew-pip/tarball/v0.4.0'
  homepage 'https://github.com/edavis/brew-pip'
  md5 '2c520aaa0eb04c82eba26e4e86e616bc'
  depends_on 'python'

  def install
    bin.install 'bin/brew-pip'
  end

  def caveats; <<-EOS.undent
    pip needs to be installed before brew-pip will work:

        #{HOMEBREW_PREFIX+"share/python"}/easy_install pip
    EOS
  end
end
