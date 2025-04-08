# coding: utf-8

"""
    Hostinger API Python SDK

    The version of the OpenAPI document: 0.0.1-beta

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_virtual_machine_nameservers_update_request import VPSV1VirtualMachineNameserversUpdateRequest

class TestVPSV1VirtualMachineNameserversUpdateRequest(unittest.TestCase):
    """VPSV1VirtualMachineNameserversUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1VirtualMachineNameserversUpdateRequest:
        """Test VPSV1VirtualMachineNameserversUpdateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1VirtualMachineNameserversUpdateRequest`
        """
        model = VPSV1VirtualMachineNameserversUpdateRequest()
        if include_optional:
            return VPSV1VirtualMachineNameserversUpdateRequest(
                ns1 = '4.3.2.1',
                ns2 = '1.2.3.4'
            )
        else:
            return VPSV1VirtualMachineNameserversUpdateRequest(
                ns1 = '4.3.2.1',
        )
        """

    def testVPSV1VirtualMachineNameserversUpdateRequest(self):
        """Test VPSV1VirtualMachineNameserversUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
