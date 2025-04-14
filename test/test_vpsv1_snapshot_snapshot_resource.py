# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.17

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_snapshot_snapshot_resource import VPSV1SnapshotSnapshotResource

class TestVPSV1SnapshotSnapshotResource(unittest.TestCase):
    """VPSV1SnapshotSnapshotResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1SnapshotSnapshotResource:
        """Test VPSV1SnapshotSnapshotResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1SnapshotSnapshotResource`
        """
        model = VPSV1SnapshotSnapshotResource()
        if include_optional:
            return VPSV1SnapshotSnapshotResource(
                id = 325,
                created_at = '2025-02-27T11:54:22Z',
                expires_at = '2025-03-19T11:54:22Z'
            )
        else:
            return VPSV1SnapshotSnapshotResource(
        )
        """

    def testVPSV1SnapshotSnapshotResource(self):
        """Test VPSV1SnapshotSnapshotResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
