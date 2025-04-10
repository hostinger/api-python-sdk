# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.6

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.billing_v1_order_order_resource import BillingV1OrderOrderResource

class TestBillingV1OrderOrderResource(unittest.TestCase):
    """BillingV1OrderOrderResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingV1OrderOrderResource:
        """Test BillingV1OrderOrderResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingV1OrderOrderResource`
        """
        model = BillingV1OrderOrderResource()
        if include_optional:
            return BillingV1OrderOrderResource(
                id = 2957086,
                subscription_id = 'Azz353Uhl1xC54pR0',
                status = 'completed',
                currency = 'USD',
                subtotal = 899,
                total = 1088,
                billing_address = hostinger_api.models.billing/v1/order/order_billing_address_resource.Billing.V1.Order.OrderBillingAddressResource(
                    first_name = 'John', 
                    last_name = 'Doe', 
                    company = '', 
                    address_1 = '', 
                    address_2 = '', 
                    city = '', 
                    state = '', 
                    zip = '', 
                    country = 'NL', 
                    phone = '', 
                    email = 'john@doe.tld', ),
                created_at = '2025-02-27T11:54:22Z',
                updated_at = '2025-03-27T11:54:22Z'
            )
        else:
            return BillingV1OrderOrderResource(
        )
        """

    def testBillingV1OrderOrderResource(self):
        """Test BillingV1OrderOrderResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
