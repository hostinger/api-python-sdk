# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.2

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_metrics_metrics_collection_cpu_usage import VPSV1MetricsMetricsCollectionCpuUsage

class TestVPSV1MetricsMetricsCollectionCpuUsage(unittest.TestCase):
    """VPSV1MetricsMetricsCollectionCpuUsage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1MetricsMetricsCollectionCpuUsage:
        """Test VPSV1MetricsMetricsCollectionCpuUsage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1MetricsMetricsCollectionCpuUsage`
        """
        model = VPSV1MetricsMetricsCollectionCpuUsage()
        if include_optional:
            return VPSV1MetricsMetricsCollectionCpuUsage(
                unit = 'measurement-unit',
                usage = {timestamp=123}
            )
        else:
            return VPSV1MetricsMetricsCollectionCpuUsage(
        )
        """

    def testVPSV1MetricsMetricsCollectionCpuUsage(self):
        """Test VPSV1MetricsMetricsCollectionCpuUsage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
