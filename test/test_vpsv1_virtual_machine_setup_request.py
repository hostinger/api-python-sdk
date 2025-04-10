# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.4

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_virtual_machine_setup_request import VPSV1VirtualMachineSetupRequest

class TestVPSV1VirtualMachineSetupRequest(unittest.TestCase):
    """VPSV1VirtualMachineSetupRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1VirtualMachineSetupRequest:
        """Test VPSV1VirtualMachineSetupRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1VirtualMachineSetupRequest`
        """
        model = VPSV1VirtualMachineSetupRequest()
        if include_optional:
            return VPSV1VirtualMachineSetupRequest(
                template_id = 1130,
                data_center_id = 19,
                post_install_script_id = 6324,
                password = 'oMeNRustosIO',
                hostname = 'my.server.tld',
                install_monarx = False,
                enable_backups = True,
                ns1 = '4.3.2.1',
                ns2 = '1.2.3.4',
                public_key = hostinger_api.models.vps_v1_virtual_machine_setup_request_public_key.VPS_V1_VirtualMachine_SetupRequest_public_key(
                    name = 'my-key', 
                    key = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC2X...', )
            )
        else:
            return VPSV1VirtualMachineSetupRequest(
                template_id = 1130,
                data_center_id = 19,
        )
        """

    def testVPSV1VirtualMachineSetupRequest(self):
        """Test VPSV1VirtualMachineSetupRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
