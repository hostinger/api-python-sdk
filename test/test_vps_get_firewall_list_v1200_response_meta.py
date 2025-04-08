# coding: utf-8

"""
    Hostinger API Python SDK

    The version of the OpenAPI document: 0.0.1-beta

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vps_get_firewall_list_v1200_response_meta import VPSGetFirewallListV1200ResponseMeta

class TestVPSGetFirewallListV1200ResponseMeta(unittest.TestCase):
    """VPSGetFirewallListV1200ResponseMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSGetFirewallListV1200ResponseMeta:
        """Test VPSGetFirewallListV1200ResponseMeta
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSGetFirewallListV1200ResponseMeta`
        """
        model = VPSGetFirewallListV1200ResponseMeta()
        if include_optional:
            return VPSGetFirewallListV1200ResponseMeta(
                current_page = 1,
                per_page = 15,
                total = 100
            )
        else:
            return VPSGetFirewallListV1200ResponseMeta(
        )
        """

    def testVPSGetFirewallListV1200ResponseMeta(self):
        """Test VPSGetFirewallListV1200ResponseMeta"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
