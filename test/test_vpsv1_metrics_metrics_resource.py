# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.1-beta

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_metrics_metrics_resource import VPSV1MetricsMetricsResource

class TestVPSV1MetricsMetricsResource(unittest.TestCase):
    """VPSV1MetricsMetricsResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1MetricsMetricsResource:
        """Test VPSV1MetricsMetricsResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1MetricsMetricsResource`
        """
        model = VPSV1MetricsMetricsResource()
        if include_optional:
            return VPSV1MetricsMetricsResource(
                unit = 'measurement-unit',
                usage = {"timestamp":123}
            )
        else:
            return VPSV1MetricsMetricsResource(
        )
        """

    def testVPSV1MetricsMetricsResource(self):
        """Test VPSV1MetricsMetricsResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
