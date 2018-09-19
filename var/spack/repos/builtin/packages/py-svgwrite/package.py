from spack import *


class PySvgwrite(PythonPackage):
    """A Python library to create SVG drawings."""

    homepage = "https://pypi.org/project/svgwrite/"
    url      = "https://files.pythonhosted.org/packages/a6/e1/8d592fc801e1dc2958fe0c84c733ed729d4020daa1826c58978f9d601bb4/svgwrite-1.1.12.zip"

    version('1.1.12', '05780a4a8ba33c16842faf37818d670e')

    depends_on('py-setuptools', type='build')
