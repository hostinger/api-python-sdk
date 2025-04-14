# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.14

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_metrics_metrics_collection_incoming_traffic import VPSV1MetricsMetricsCollectionIncomingTraffic

class TestVPSV1MetricsMetricsCollectionIncomingTraffic(unittest.TestCase):
    """VPSV1MetricsMetricsCollectionIncomingTraffic unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1MetricsMetricsCollectionIncomingTraffic:
        """Test VPSV1MetricsMetricsCollectionIncomingTraffic
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1MetricsMetricsCollectionIncomingTraffic`
        """
        model = VPSV1MetricsMetricsCollectionIncomingTraffic()
        if include_optional:
            return VPSV1MetricsMetricsCollectionIncomingTraffic(
                unit = 'measurement-unit',
                usage = {timestamp=123}
            )
        else:
            return VPSV1MetricsMetricsCollectionIncomingTraffic(
        )
        """

    def testVPSV1MetricsMetricsCollectionIncomingTraffic(self):
        """Test VPSV1MetricsMetricsCollectionIncomingTraffic"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
