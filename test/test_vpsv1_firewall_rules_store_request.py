# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.14

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger-api.models.vpsv1_firewall_rules_store_request import VPSV1FirewallRulesStoreRequest

class TestVPSV1FirewallRulesStoreRequest(unittest.TestCase):
    """VPSV1FirewallRulesStoreRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1FirewallRulesStoreRequest:
        """Test VPSV1FirewallRulesStoreRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1FirewallRulesStoreRequest`
        """
        model = VPSV1FirewallRulesStoreRequest()
        if include_optional:
            return VPSV1FirewallRulesStoreRequest(
                protocol = 'TCP',
                port = '443',
                source = 'any',
                source_detail = '351.15.24.0/24'
            )
        else:
            return VPSV1FirewallRulesStoreRequest(
                protocol = 'TCP',
                port = '443',
                source = 'any',
                source_detail = '351.15.24.0/24',
        )
        """

    def testVPSV1FirewallRulesStoreRequest(self):
        """Test VPSV1FirewallRulesStoreRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
