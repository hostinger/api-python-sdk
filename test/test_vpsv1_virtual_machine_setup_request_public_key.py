# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.20

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_virtual_machine_setup_request_public_key import VPSV1VirtualMachineSetupRequestPublicKey

class TestVPSV1VirtualMachineSetupRequestPublicKey(unittest.TestCase):
    """VPSV1VirtualMachineSetupRequestPublicKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1VirtualMachineSetupRequestPublicKey:
        """Test VPSV1VirtualMachineSetupRequestPublicKey
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1VirtualMachineSetupRequestPublicKey`
        """
        model = VPSV1VirtualMachineSetupRequestPublicKey()
        if include_optional:
            return VPSV1VirtualMachineSetupRequestPublicKey(
                name = 'my-key',
                key = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC2X...'
            )
        else:
            return VPSV1VirtualMachineSetupRequestPublicKey(
        )
        """

    def testVPSV1VirtualMachineSetupRequestPublicKey(self):
        """Test VPSV1VirtualMachineSetupRequestPublicKey"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
