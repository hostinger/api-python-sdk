# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.14

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_firewall_firewall_resource import VPSV1FirewallFirewallResource

class TestVPSV1FirewallFirewallResource(unittest.TestCase):
    """VPSV1FirewallFirewallResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1FirewallFirewallResource:
        """Test VPSV1FirewallFirewallResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1FirewallFirewallResource`
        """
        model = VPSV1FirewallFirewallResource()
        if include_optional:
            return VPSV1FirewallFirewallResource(
                id = 65224,
                name = 'HTTP and SSH only',
                synced = False,
                rules = [
                    hostinger_api.models.vps/v1/firewall/firewall_rule_resource.VPS.V1.Firewall.FirewallRuleResource(
                        id = 24541, 
                        action = 'accept', 
                        protocol = 'TCP', 
                        port = '1024:2048', 
                        source = 'any', 
                        source_detail = 'any', )
                    ],
                created_at = '2021-09-01T12:00Z',
                updated_at = '2021-09-01T12:00Z'
            )
        else:
            return VPSV1FirewallFirewallResource(
        )
        """

    def testVPSV1FirewallFirewallResource(self):
        """Test VPSV1FirewallFirewallResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
