class Atlas < Formula
  include Language::Python::Virtualenv

  desc "Garmin Activity Downloader"
  homepage "https://github.com/sullrich84/homebrew-atlas"
  head "https://github.com/sullrich84/homebrew-atlas.git",
    :branch => "main"

  depends_on "python@3.9"

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
