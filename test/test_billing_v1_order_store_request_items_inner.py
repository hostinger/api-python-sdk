# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.4

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.billing_v1_order_store_request_items_inner import BillingV1OrderStoreRequestItemsInner

class TestBillingV1OrderStoreRequestItemsInner(unittest.TestCase):
    """BillingV1OrderStoreRequestItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingV1OrderStoreRequestItemsInner:
        """Test BillingV1OrderStoreRequestItemsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingV1OrderStoreRequestItemsInner`
        """
        model = BillingV1OrderStoreRequestItemsInner()
        if include_optional:
            return BillingV1OrderStoreRequestItemsInner(
                item_id = 'hostingercom-vps-kvm2-usd-1m',
                quantity = 1
            )
        else:
            return BillingV1OrderStoreRequestItemsInner(
        )
        """

    def testBillingV1OrderStoreRequestItemsInner(self):
        """Test BillingV1OrderStoreRequestItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
