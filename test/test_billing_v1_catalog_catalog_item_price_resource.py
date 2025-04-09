# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.2

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.billing_v1_catalog_catalog_item_price_resource import BillingV1CatalogCatalogItemPriceResource

class TestBillingV1CatalogCatalogItemPriceResource(unittest.TestCase):
    """BillingV1CatalogCatalogItemPriceResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingV1CatalogCatalogItemPriceResource:
        """Test BillingV1CatalogCatalogItemPriceResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingV1CatalogCatalogItemPriceResource`
        """
        model = BillingV1CatalogCatalogItemPriceResource()
        if include_optional:
            return BillingV1CatalogCatalogItemPriceResource(
                id = 'hostingercom-vps-kvm2-usd-1m',
                name = 'KVM 2 (billed every month)',
                currency = 'USD',
                price = 1799,
                first_period_price = 899,
                period = 1,
                period_unit = 'day'
            )
        else:
            return BillingV1CatalogCatalogItemPriceResource(
        )
        """

    def testBillingV1CatalogCatalogItemPriceResource(self):
        """Test BillingV1CatalogCatalogItemPriceResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
