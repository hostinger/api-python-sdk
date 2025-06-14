# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.68

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.billing_v1_subscription_cancel_request import BillingV1SubscriptionCancelRequest

class TestBillingV1SubscriptionCancelRequest(unittest.TestCase):
    """BillingV1SubscriptionCancelRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingV1SubscriptionCancelRequest:
        """Test BillingV1SubscriptionCancelRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingV1SubscriptionCancelRequest`
        """
        model = BillingV1SubscriptionCancelRequest()
        if include_optional:
            return BillingV1SubscriptionCancelRequest(
                reason_code = 'other',
                cancel_option = 'immediately'
            )
        else:
            return BillingV1SubscriptionCancelRequest(
        )
        """

    def testBillingV1SubscriptionCancelRequest(self):
        """Test BillingV1SubscriptionCancelRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
