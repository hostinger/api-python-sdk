# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.16

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.dnsv1_zone_update_request_zone_inner import DNSV1ZoneUpdateRequestZoneInner

class TestDNSV1ZoneUpdateRequestZoneInner(unittest.TestCase):
    """DNSV1ZoneUpdateRequestZoneInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DNSV1ZoneUpdateRequestZoneInner:
        """Test DNSV1ZoneUpdateRequestZoneInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DNSV1ZoneUpdateRequestZoneInner`
        """
        model = DNSV1ZoneUpdateRequestZoneInner()
        if include_optional:
            return DNSV1ZoneUpdateRequestZoneInner(
                name = 'www',
                records = [
                    hostinger_api.models.dns_v1_zone_update_request_zone_inner_records_inner.DNS_V1_Zone_UpdateRequest_zone_inner_records_inner(
                        content = 'mydomain.tld.', )
                    ],
                ttl = 14400,
                type = 'A'
            )
        else:
            return DNSV1ZoneUpdateRequestZoneInner(
                name = 'www',
                type = 'A',
        )
        """

    def testDNSV1ZoneUpdateRequestZoneInner(self):
        """Test DNSV1ZoneUpdateRequestZoneInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
