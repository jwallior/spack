from spack import *


class PySvgpathtools(PythonPackage):
    """A collection of tools for manipulating and analyzing SVG Path objects and Bezier curves."""

    homepage = "https://pypi.org/project/svgpathtools/"
    url      = "https://files.pythonhosted.org/packages/59/53/a66c970db2abe96152b28fc990bab9a4b93f0dcab21e70db287166910415/svgpathtools-1.3.3.tar.gz"

    version('1.3.3', '253714213424e73b67a73c1fd73b714e')

    depends_on('py-setuptools', type='build')
