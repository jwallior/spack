from spack import *


class PyXlwt(PythonPackage):
    """Library to create spreadsheet files compatible with MS Excel 97/2000/XP/2003 XLS files, on any platform, with Python 2.6, 2.7, 3.3+."""

    homepage = "https://pypi.org/project/xlwt/"
    url      = "https://files.pythonhosted.org/packages/06/97/56a6f56ce44578a69343449aa5a0d98eefe04085d69da539f3034e2cd5c1/xlwt-1.3.0.tar.gz"

    version('1.3.0', '4b1ca8a3cef3261f4b4dc3f138e383a8')

    depends_on('py-setuptools', type='build')
