# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.6

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_firewall_store_request import VPSV1FirewallStoreRequest

class TestVPSV1FirewallStoreRequest(unittest.TestCase):
    """VPSV1FirewallStoreRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1FirewallStoreRequest:
        """Test VPSV1FirewallStoreRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1FirewallStoreRequest`
        """
        model = VPSV1FirewallStoreRequest()
        if include_optional:
            return VPSV1FirewallStoreRequest(
                name = 'My Firewall Group'
            )
        else:
            return VPSV1FirewallStoreRequest(
                name = 'My Firewall Group',
        )
        """

    def testVPSV1FirewallStoreRequest(self):
        """Test VPSV1FirewallStoreRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
