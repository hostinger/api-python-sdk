# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.68

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_virtual_machine_recovery_start_request import VPSV1VirtualMachineRecoveryStartRequest

class TestVPSV1VirtualMachineRecoveryStartRequest(unittest.TestCase):
    """VPSV1VirtualMachineRecoveryStartRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1VirtualMachineRecoveryStartRequest:
        """Test VPSV1VirtualMachineRecoveryStartRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1VirtualMachineRecoveryStartRequest`
        """
        model = VPSV1VirtualMachineRecoveryStartRequest()
        if include_optional:
            return VPSV1VirtualMachineRecoveryStartRequest(
                root_password = 'oMeNRustosIO'
            )
        else:
            return VPSV1VirtualMachineRecoveryStartRequest(
                root_password = 'oMeNRustosIO',
        )
        """

    def testVPSV1VirtualMachineRecoveryStartRequest(self):
        """Test VPSV1VirtualMachineRecoveryStartRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
