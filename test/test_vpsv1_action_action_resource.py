# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.20

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_action_action_resource import VPSV1ActionActionResource

class TestVPSV1ActionActionResource(unittest.TestCase):
    """VPSV1ActionActionResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1ActionActionResource:
        """Test VPSV1ActionActionResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1ActionActionResource`
        """
        model = VPSV1ActionActionResource()
        if include_optional:
            return VPSV1ActionActionResource(
                id = 8123712,
                name = 'action_name',
                state = 'success',
                created_at = '2025-02-27T11:54Z',
                updated_at = '2025-02-27T11:58Z'
            )
        else:
            return VPSV1ActionActionResource(
        )
        """

    def testVPSV1ActionActionResource(self):
        """Test VPSV1ActionActionResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
