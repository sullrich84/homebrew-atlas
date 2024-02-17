class Atlas < Formula
  include Language::Python::Virtualenv

  desc "Garmin Activity Downloader"
  homepage "https://github.com/sullrich84/homebrew-atlas"
  head "https://github.com/sullrich84/homebrew-atlas.git",
    :branch => "main"

  depends_on "python@3.9"

  resource "click" do
    url "https://files.pythonhosted.org/packages/96/d3/f04c7bfcf5c1862a2a5b845c6b2b360488cf47af55dfa79c98f6a6bf98b5/click-8.1.7.tar.gz"
    sha256 "ca9853ad459e787e2192211578cc907e7594e294c7ccc834310722b41b9ca6de"
  end
  
  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match "sullrich84/atlas 0.0.0-alpha", shell_output("#{bin}/atlas")
  end
  
  def post_install
    ohai "🌐 Atlas successfully installed"
  end
end
