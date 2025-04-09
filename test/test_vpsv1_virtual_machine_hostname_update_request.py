# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.2

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_virtual_machine_hostname_update_request import VPSV1VirtualMachineHostnameUpdateRequest

class TestVPSV1VirtualMachineHostnameUpdateRequest(unittest.TestCase):
    """VPSV1VirtualMachineHostnameUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1VirtualMachineHostnameUpdateRequest:
        """Test VPSV1VirtualMachineHostnameUpdateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1VirtualMachineHostnameUpdateRequest`
        """
        model = VPSV1VirtualMachineHostnameUpdateRequest()
        if include_optional:
            return VPSV1VirtualMachineHostnameUpdateRequest(
                hostname = 'my.server.tld'
            )
        else:
            return VPSV1VirtualMachineHostnameUpdateRequest(
                hostname = 'my.server.tld',
        )
        """

    def testVPSV1VirtualMachineHostnameUpdateRequest(self):
        """Test VPSV1VirtualMachineHostnameUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
