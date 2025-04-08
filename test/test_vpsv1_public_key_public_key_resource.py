# coding: utf-8

"""
    Hostinger API Python SDK

    The version of the OpenAPI document: 0.0.1-beta

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_public_key_public_key_resource import VPSV1PublicKeyPublicKeyResource

class TestVPSV1PublicKeyPublicKeyResource(unittest.TestCase):
    """VPSV1PublicKeyPublicKeyResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1PublicKeyPublicKeyResource:
        """Test VPSV1PublicKeyPublicKeyResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1PublicKeyPublicKeyResource`
        """
        model = VPSV1PublicKeyPublicKeyResource()
        if include_optional:
            return VPSV1PublicKeyPublicKeyResource(
                id = 325,
                name = 'My public key',
                key = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD...'
            )
        else:
            return VPSV1PublicKeyPublicKeyResource(
        )
        """

    def testVPSV1PublicKeyPublicKeyResource(self):
        """Test VPSV1PublicKeyPublicKeyResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
