# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.14

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_firewall_firewall_rule_resource import VPSV1FirewallFirewallRuleResource

class TestVPSV1FirewallFirewallRuleResource(unittest.TestCase):
    """VPSV1FirewallFirewallRuleResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1FirewallFirewallRuleResource:
        """Test VPSV1FirewallFirewallRuleResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1FirewallFirewallRuleResource`
        """
        model = VPSV1FirewallFirewallRuleResource()
        if include_optional:
            return VPSV1FirewallFirewallRuleResource(
                id = 24541,
                action = 'accept',
                protocol = 'TCP',
                port = '1024:2048',
                source = 'any',
                source_detail = 'any'
            )
        else:
            return VPSV1FirewallFirewallRuleResource(
        )
        """

    def testVPSV1FirewallFirewallRuleResource(self):
        """Test VPSV1FirewallFirewallRuleResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
