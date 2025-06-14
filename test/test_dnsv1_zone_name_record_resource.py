# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.68

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.dnsv1_zone_name_record_resource import DNSV1ZoneNameRecordResource

class TestDNSV1ZoneNameRecordResource(unittest.TestCase):
    """DNSV1ZoneNameRecordResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DNSV1ZoneNameRecordResource:
        """Test DNSV1ZoneNameRecordResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DNSV1ZoneNameRecordResource`
        """
        model = DNSV1ZoneNameRecordResource()
        if include_optional:
            return DNSV1ZoneNameRecordResource(
                content = 'mydomain.tld.',
                is_disabled = False
            )
        else:
            return DNSV1ZoneNameRecordResource(
        )
        """

    def testDNSV1ZoneNameRecordResource(self):
        """Test DNSV1ZoneNameRecordResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
