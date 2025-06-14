# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.68

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.api.dns_zone_api import DNSZoneApi


class TestDNSZoneApi(unittest.TestCase):
    """DNSZoneApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DNSZoneApi()

    def tearDown(self) -> None:
        pass

    def test_delete_zone_records_v1(self) -> None:
        """Test case for delete_zone_records_v1

        Delete zone records
        """
        pass

    def test_get_records_v1(self) -> None:
        """Test case for get_records_v1

        Get records
        """
        pass

    def test_reset_zone_records_v1(self) -> None:
        """Test case for reset_zone_records_v1

        Reset zone records
        """
        pass

    def test_update_zone_records_v1(self) -> None:
        """Test case for update_zone_records_v1

        Update zone records
        """
        pass

    def test_validate_zone_records_v1(self) -> None:
        """Test case for validate_zone_records_v1

        Validate zone records
        """
        pass


if __name__ == '__main__':
    unittest.main()
