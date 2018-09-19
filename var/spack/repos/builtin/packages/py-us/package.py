from spack import *


class PyUs(PythonPackage):
    """US state meta information and other fun stuff."""

    homepage = "https://pypi.org/project/us/"
    url      = "https://files.pythonhosted.org/packages/72/83/8731cbf5afcf3434c0b24cfc520c11fd27bfc8a6878114662f4e3dbdab71/us-1.0.0.tar.gz"

    version('1.0.0', 'ce13f8d9c4202402acc1eb451e7bf22f')

    depends_on('py-setuptools', type='build')
    depends_on('py-jellyfish', type=('build', 'run'))
