# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.20

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.api.vps_snapshots_api import VPSSnapshotsApi


class TestVPSSnapshotsApi(unittest.TestCase):
    """VPSSnapshotsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VPSSnapshotsApi()

    def tearDown(self) -> None:
        pass

    def test_create_snapshot_v1(self) -> None:
        """Test case for create_snapshot_v1

        Create snapshot
        """
        pass

    def test_delete_snapshot_v1(self) -> None:
        """Test case for delete_snapshot_v1

        Delete snapshot
        """
        pass

    def test_get_snapshot_v1(self) -> None:
        """Test case for get_snapshot_v1

        Get snapshot
        """
        pass

    def test_restore_snapshot_v1(self) -> None:
        """Test case for restore_snapshot_v1

        Restore snapshot
        """
        pass


if __name__ == '__main__':
    unittest.main()
