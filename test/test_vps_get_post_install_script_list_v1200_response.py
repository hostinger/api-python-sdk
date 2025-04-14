# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.16

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vps_get_post_install_script_list_v1200_response import VPSGetPostInstallScriptListV1200Response

class TestVPSGetPostInstallScriptListV1200Response(unittest.TestCase):
    """VPSGetPostInstallScriptListV1200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSGetPostInstallScriptListV1200Response:
        """Test VPSGetPostInstallScriptListV1200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSGetPostInstallScriptListV1200Response`
        """
        model = VPSGetPostInstallScriptListV1200Response()
        if include_optional:
            return VPSGetPostInstallScriptListV1200Response(
                data = [
                    hostinger_api.models.vps/v1/post_install_script/post_install_script_resource.VPS.V1.PostInstallScript.PostInstallScriptResource(
                        id = 325, 
                        name = 'My Setup Script', 
                        content = '#!/bin/bash\napt-get update\napt-get install -y nginx', 
                        created_at = '2025-02-27T11:54:22Z', 
                        updated_at = '2025-03-19T11:54:22Z', )
                    ],
                meta = hostinger_api.models.common/schema/pagination_meta_schema.Common.Schema.PaginationMetaSchema(
                    current_page = 1, 
                    per_page = 15, 
                    total = 100, )
            )
        else:
            return VPSGetPostInstallScriptListV1200Response(
        )
        """

    def testVPSGetPostInstallScriptListV1200Response(self):
        """Test VPSGetPostInstallScriptListV1200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
