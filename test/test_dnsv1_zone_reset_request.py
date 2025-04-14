# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.14

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.dnsv1_zone_reset_request import DNSV1ZoneResetRequest

class TestDNSV1ZoneResetRequest(unittest.TestCase):
    """DNSV1ZoneResetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DNSV1ZoneResetRequest:
        """Test DNSV1ZoneResetRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DNSV1ZoneResetRequest`
        """
        model = DNSV1ZoneResetRequest()
        if include_optional:
            return DNSV1ZoneResetRequest(
                sync = True,
                reset_email_records = True,
                whitelisted_record_types = ["MX","TXT"]
            )
        else:
            return DNSV1ZoneResetRequest(
        )
        """

    def testDNSV1ZoneResetRequest(self):
        """Test DNSV1ZoneResetRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
