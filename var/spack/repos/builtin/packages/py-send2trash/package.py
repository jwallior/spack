from spack import *


class PySend2trash(PythonPackage):
    """Send file to trash natively under Mac OS X, Windows and Linux."""

    homepage = "https://pypi.org/project/Send2Trash/"
    url      = "https://files.pythonhosted.org/packages/13/2e/ea40de0304bb1dc4eb309de90aeec39871b9b7c4bd30f1a3cdcb3496f5c0/Send2Trash-1.5.0.tar.gz"

    version('1.5.0', 'eccc3563a305b8cb10001ffd1aa92fa0')

    depends_on('py-setuptools', type='build')
