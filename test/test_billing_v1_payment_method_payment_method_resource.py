# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.1-beta

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.billing_v1_payment_method_payment_method_resource import BillingV1PaymentMethodPaymentMethodResource

class TestBillingV1PaymentMethodPaymentMethodResource(unittest.TestCase):
    """BillingV1PaymentMethodPaymentMethodResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingV1PaymentMethodPaymentMethodResource:
        """Test BillingV1PaymentMethodPaymentMethodResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingV1PaymentMethodPaymentMethodResource`
        """
        model = BillingV1PaymentMethodPaymentMethodResource()
        if include_optional:
            return BillingV1PaymentMethodPaymentMethodResource(
                id = 6523,
                name = 'Credit Card',
                identifier = '1234*****6464',
                payment_method = 'card',
                is_default = True,
                is_expired = False,
                is_suspended = False,
                created_at = '2025-02-27T11:54:22Z',
                expires_at = '2025-03-27T11:54:22Z'
            )
        else:
            return BillingV1PaymentMethodPaymentMethodResource(
        )
        """

    def testBillingV1PaymentMethodPaymentMethodResource(self):
        """Test BillingV1PaymentMethodPaymentMethodResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
