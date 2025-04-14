# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.17

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.dnsv1_zone_destroy_request import DNSV1ZoneDestroyRequest

class TestDNSV1ZoneDestroyRequest(unittest.TestCase):
    """DNSV1ZoneDestroyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DNSV1ZoneDestroyRequest:
        """Test DNSV1ZoneDestroyRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DNSV1ZoneDestroyRequest`
        """
        model = DNSV1ZoneDestroyRequest()
        if include_optional:
            return DNSV1ZoneDestroyRequest(
                filters = [
                    hostinger_api.models.dns_v1_zone_destroy_request_filters_inner.DNS_V1_Zone_DestroyRequest_filters_inner(
                        name = '@', 
                        type = 'A', )
                    ]
            )
        else:
            return DNSV1ZoneDestroyRequest(
                filters = [
                    hostinger_api.models.dns_v1_zone_destroy_request_filters_inner.DNS_V1_Zone_DestroyRequest_filters_inner(
                        name = '@', 
                        type = 'A', )
                    ],
        )
        """

    def testDNSV1ZoneDestroyRequest(self):
        """Test DNSV1ZoneDestroyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
