# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.3

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.vpsv1_virtual_machine_virtual_machine_resource import VPSV1VirtualMachineVirtualMachineResource

class TestVPSV1VirtualMachineVirtualMachineResource(unittest.TestCase):
    """VPSV1VirtualMachineVirtualMachineResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VPSV1VirtualMachineVirtualMachineResource:
        """Test VPSV1VirtualMachineVirtualMachineResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VPSV1VirtualMachineVirtualMachineResource`
        """
        model = VPSV1VirtualMachineVirtualMachineResource()
        if include_optional:
            return VPSV1VirtualMachineVirtualMachineResource(
                id = 17923,
                firewall_group_id = 56,
                subscription_id = 'Azz353Uhl1xC54pR0',
                plan = 'KVM 4',
                hostname = 'srv17923.hstgr.cloud',
                state = 'running',
                actions_lock = 'unlocked',
                cpus = 4,
                memory = 8192,
                disk = 51200,
                bandwidth = 1073741824,
                ns1 = '1.1.1.1',
                ns2 = '8.8.8.8',
                ipv4 = None,
                ipv6 = None,
                template = None,
                created_at = '2024-09-05T07:25:36Z'
            )
        else:
            return VPSV1VirtualMachineVirtualMachineResource(
        )
        """

    def testVPSV1VirtualMachineVirtualMachineResource(self):
        """Test VPSV1VirtualMachineVirtualMachineResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
