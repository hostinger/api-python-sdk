# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.2

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_virtual_machine_virtual_machine_resource_template import VPSV1VirtualMachineVirtualMachineResourceTemplate

class TestVPSV1VirtualMachineVirtualMachineResourceTemplate(unittest.TestCase):
    """VPSV1VirtualMachineVirtualMachineResourceTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1VirtualMachineVirtualMachineResourceTemplate:
        """Test VPSV1VirtualMachineVirtualMachineResourceTemplate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1VirtualMachineVirtualMachineResourceTemplate`
        """
        model = VPSV1VirtualMachineVirtualMachineResourceTemplate()
        if include_optional:
            return VPSV1VirtualMachineVirtualMachineResourceTemplate(
                id = 6523,
                name = 'Ubuntu 20.04 LTS',
                description = 'Ubuntu 20.04 LTS',
                documentation = 'https://docs.ubuntu.com'
            )
        else:
            return VPSV1VirtualMachineVirtualMachineResourceTemplate(
        )
        """

    def testVPSV1VirtualMachineVirtualMachineResourceTemplate(self):
        """Test VPSV1VirtualMachineVirtualMachineResourceTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
