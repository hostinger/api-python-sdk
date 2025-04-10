# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.4

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_data_center_data_center_resource import VPSV1DataCenterDataCenterResource

class TestVPSV1DataCenterDataCenterResource(unittest.TestCase):
    """VPSV1DataCenterDataCenterResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1DataCenterDataCenterResource:
        """Test VPSV1DataCenterDataCenterResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1DataCenterDataCenterResource`
        """
        model = VPSV1DataCenterDataCenterResource()
        if include_optional:
            return VPSV1DataCenterDataCenterResource(
                id = 29,
                name = 'phx',
                location = 'us',
                city = 'Phoenix',
                continent = 'North America'
            )
        else:
            return VPSV1DataCenterDataCenterResource(
        )
        """

    def testVPSV1DataCenterDataCenterResource(self):
        """Test VPSV1DataCenterDataCenterResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
