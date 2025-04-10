# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.7

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from @hostinger/api.models.vps_get_public_key_list_v1200_response import VPSGetPublicKeyListV1200Response

class TestVPSGetPublicKeyListV1200Response(unittest.TestCase):
    """VPSGetPublicKeyListV1200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSGetPublicKeyListV1200Response:
        """Test VPSGetPublicKeyListV1200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSGetPublicKeyListV1200Response`
        """
        model = VPSGetPublicKeyListV1200Response()
        if include_optional:
            return VPSGetPublicKeyListV1200Response(
                data = [
                    @hostinger/api.models.vps/v1/public_key/public_key_resource.VPS.V1.PublicKey.PublicKeyResource(
                        id = 325, 
                        name = 'My public key', 
                        key = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD...', )
                    ],
                meta = @hostinger/api.models.common/schema/pagination_meta_schema.Common.Schema.PaginationMetaSchema(
                    current_page = 1, 
                    per_page = 15, 
                    total = 100, )
            )
        else:
            return VPSGetPublicKeyListV1200Response(
        )
        """

    def testVPSGetPublicKeyListV1200Response(self):
        """Test VPSGetPublicKeyListV1200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
