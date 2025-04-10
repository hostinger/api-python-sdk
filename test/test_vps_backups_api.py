# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.5

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.api.vps_backups_api import VPSBackupsApi


class TestVPSBackupsApi(unittest.TestCase):
    """VPSBackupsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VPSBackupsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_backup_v1(self) -> None:
        """Test case for delete_backup_v1

        Delete backup
        """
        pass

    def test_get_backup_list_v1(self) -> None:
        """Test case for get_backup_list_v1

        Get backup list
        """
        pass

    def test_restore_backup_v1(self) -> None:
        """Test case for restore_backup_v1

        Restore backup
        """
        pass


if __name__ == '__main__':
    unittest.main()
