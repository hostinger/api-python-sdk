# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.7

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from @hostinger/api.models.vpsv1_metrics_metrics_collection_ram_usage import VPSV1MetricsMetricsCollectionRamUsage

class TestVPSV1MetricsMetricsCollectionRamUsage(unittest.TestCase):
    """VPSV1MetricsMetricsCollectionRamUsage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1MetricsMetricsCollectionRamUsage:
        """Test VPSV1MetricsMetricsCollectionRamUsage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1MetricsMetricsCollectionRamUsage`
        """
        model = VPSV1MetricsMetricsCollectionRamUsage()
        if include_optional:
            return VPSV1MetricsMetricsCollectionRamUsage(
                unit = 'measurement-unit',
                usage = {timestamp=123}
            )
        else:
            return VPSV1MetricsMetricsCollectionRamUsage(
        )
        """

    def testVPSV1MetricsMetricsCollectionRamUsage(self):
        """Test VPSV1MetricsMetricsCollectionRamUsage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
