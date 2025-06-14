# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.68

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_public_key_store_request import VPSV1PublicKeyStoreRequest

class TestVPSV1PublicKeyStoreRequest(unittest.TestCase):
    """VPSV1PublicKeyStoreRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1PublicKeyStoreRequest:
        """Test VPSV1PublicKeyStoreRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1PublicKeyStoreRequest`
        """
        model = VPSV1PublicKeyStoreRequest()
        if include_optional:
            return VPSV1PublicKeyStoreRequest(
                name = 'My Public Key',
                key = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD...'
            )
        else:
            return VPSV1PublicKeyStoreRequest(
                name = 'My Public Key',
                key = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD...',
        )
        """

    def testVPSV1PublicKeyStoreRequest(self):
        """Test VPSV1PublicKeyStoreRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
