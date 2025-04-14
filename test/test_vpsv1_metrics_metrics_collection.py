# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.14

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_metrics_metrics_collection import VPSV1MetricsMetricsCollection

class TestVPSV1MetricsMetricsCollection(unittest.TestCase):
    """VPSV1MetricsMetricsCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1MetricsMetricsCollection:
        """Test VPSV1MetricsMetricsCollection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1MetricsMetricsCollection`
        """
        model = VPSV1MetricsMetricsCollection()
        if include_optional:
            return VPSV1MetricsMetricsCollection(
                cpu_usage = {"unit":"%","usage":{"1742269632":1.45}},
                ram_usage = {"unit":"bytes","usage":{"1742269632":554176512}},
                disk_space = {"unit":"bytes","usage":{"1742269632":2620018688}},
                outgoing_traffic = {"unit":"bytes","usage":{"1742269632":784800}},
                incoming_traffic = {"unit":"bytes","usage":{"1742269632":8978400}},
                uptime = {"unit":"milliseconds","usage":{"1742269632":455248}}
            )
        else:
            return VPSV1MetricsMetricsCollection(
        )
        """

    def testVPSV1MetricsMetricsCollection(self):
        """Test VPSV1MetricsMetricsCollection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
