require 'formula'

class BrewPip < Formula
  url 'https://github.com/edavis/brew-pip/tarball/v0.3.0'
  homepage 'https://github.com/edavis/brew-pip'
  md5 'a4c3b18f21789b65543a3873550242ca'
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
