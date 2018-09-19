from spack import *


class PyPrometheusClient(PythonPackage):
    """Python client for the Prometheus monitoring system."""

    homepage = "https://pypi.org/project/prometheus_client/"
    url      = "https://files.pythonhosted.org/packages/a1/b1/08de091b392fec31da9bd3f5edd9214ec1c6931dd81641610ac20f3ff934/prometheus_client-0.3.1.tar.gz"

    version('0.3.1', 'adfd75da26ae2c3e139e66922a687919')

    depends_on('py-setuptools', type='build')
