# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.14

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger-api.models.vpsv1_post_install_script_store_request import VPSV1PostInstallScriptStoreRequest

class TestVPSV1PostInstallScriptStoreRequest(unittest.TestCase):
    """VPSV1PostInstallScriptStoreRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1PostInstallScriptStoreRequest:
        """Test VPSV1PostInstallScriptStoreRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1PostInstallScriptStoreRequest`
        """
        model = VPSV1PostInstallScriptStoreRequest()
        if include_optional:
            return VPSV1PostInstallScriptStoreRequest(
                name = 'My Script',
                content = '#!/bin/bash

echo 'Hello, World!''
            )
        else:
            return VPSV1PostInstallScriptStoreRequest(
                name = 'My Script',
                content = '#!/bin/bash

echo 'Hello, World!'',
        )
        """

    def testVPSV1PostInstallScriptStoreRequest(self):
        """Test VPSV1PostInstallScriptStoreRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
