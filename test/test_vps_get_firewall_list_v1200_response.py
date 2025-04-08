# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.1-beta

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vps_get_firewall_list_v1200_response import VPSGetFirewallListV1200Response

class TestVPSGetFirewallListV1200Response(unittest.TestCase):
    """VPSGetFirewallListV1200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSGetFirewallListV1200Response:
        """Test VPSGetFirewallListV1200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSGetFirewallListV1200Response`
        """
        model = VPSGetFirewallListV1200Response()
        if include_optional:
            return VPSGetFirewallListV1200Response(
                data = [
                    hostinger_api.models.vps/v1/firewall/firewall_resource.VPS.V1.Firewall.FirewallResource(
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
                        updated_at = '2021-09-01T12:00Z', )
                    ],
                meta = hostinger_api.models.vps_get_firewall_list_v1_200_response_meta.VPS_getFirewallListV1_200_response_meta(
                    current_page = 1, 
                    per_page = 15, 
                    total = 100, )
            )
        else:
            return VPSGetFirewallListV1200Response(
        )
        """

    def testVPSGetFirewallListV1200Response(self):
        """Test VPSGetFirewallListV1200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
