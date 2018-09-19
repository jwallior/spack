from spack import *


class PyJellyfish(PythonPackage):
    """a library for doing approximate and phonetic matching of strings."""

    homepage = "https://pypi.org/project/jellyfish/"
    url      = "https://files.pythonhosted.org/packages/61/3f/60ac86fb43dfbf976768e80674b5538e535f6eca5aa7806cf2fdfd63550f/jellyfish-0.6.1.tar.gz"

    version('0.6.1', '4944750af050995d38dd3c42709ae2ab')

    depends_on('py-setuptools', type='build')
