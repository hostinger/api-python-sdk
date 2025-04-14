# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.20

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_post_install_script_post_install_script_resource import VPSV1PostInstallScriptPostInstallScriptResource

class TestVPSV1PostInstallScriptPostInstallScriptResource(unittest.TestCase):
    """VPSV1PostInstallScriptPostInstallScriptResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1PostInstallScriptPostInstallScriptResource:
        """Test VPSV1PostInstallScriptPostInstallScriptResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1PostInstallScriptPostInstallScriptResource`
        """
        model = VPSV1PostInstallScriptPostInstallScriptResource()
        if include_optional:
            return VPSV1PostInstallScriptPostInstallScriptResource(
                id = 325,
                name = 'My Setup Script',
                content = '#!/bin/bash\napt-get update\napt-get install -y nginx',
                created_at = '2025-02-27T11:54:22Z',
                updated_at = '2025-03-19T11:54:22Z'
            )
        else:
            return VPSV1PostInstallScriptPostInstallScriptResource(
        )
        """

    def testVPSV1PostInstallScriptPostInstallScriptResource(self):
        """Test VPSV1PostInstallScriptPostInstallScriptResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
