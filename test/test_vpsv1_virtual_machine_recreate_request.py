# coding: utf-8

"""
    Hostinger API Python SDK

    The version of the OpenAPI document: 0.0.1-beta

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_virtual_machine_recreate_request import VPSV1VirtualMachineRecreateRequest

class TestVPSV1VirtualMachineRecreateRequest(unittest.TestCase):
    """VPSV1VirtualMachineRecreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1VirtualMachineRecreateRequest:
        """Test VPSV1VirtualMachineRecreateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1VirtualMachineRecreateRequest`
        """
        model = VPSV1VirtualMachineRecreateRequest()
        if include_optional:
            return VPSV1VirtualMachineRecreateRequest(
                password = 'oMeNRustosIO',
                post_install_script_id = 6324,
                template_id = 1130
            )
        else:
            return VPSV1VirtualMachineRecreateRequest(
                password = 'oMeNRustosIO',
                template_id = 1130,
        )
        """

    def testVPSV1VirtualMachineRecreateRequest(self):
        """Test VPSV1VirtualMachineRecreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
