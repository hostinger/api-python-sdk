# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.14

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger-api.models.vpsv1_ip_address_ip_address_resource import VPSV1IPAddressIPAddressResource

class TestVPSV1IPAddressIPAddressResource(unittest.TestCase):
    """VPSV1IPAddressIPAddressResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1IPAddressIPAddressResource:
        """Test VPSV1IPAddressIPAddressResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1IPAddressIPAddressResource`
        """
        model = VPSV1IPAddressIPAddressResource()
        if include_optional:
            return VPSV1IPAddressIPAddressResource(
                id = 52347,
                address = '213.331.273.15',
                ptr = 'something.domain.tld'
            )
        else:
            return VPSV1IPAddressIPAddressResource(
        )
        """

    def testVPSV1IPAddressIPAddressResource(self):
        """Test VPSV1IPAddressIPAddressResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
