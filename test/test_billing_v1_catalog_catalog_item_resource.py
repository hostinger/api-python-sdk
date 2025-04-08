# coding: utf-8

"""
    Hostinger API Python SDK

    The version of the OpenAPI document: 0.0.1-beta

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.billing_v1_catalog_catalog_item_resource import BillingV1CatalogCatalogItemResource

class TestBillingV1CatalogCatalogItemResource(unittest.TestCase):
    """BillingV1CatalogCatalogItemResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingV1CatalogCatalogItemResource:
        """Test BillingV1CatalogCatalogItemResource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingV1CatalogCatalogItemResource`
        """
        model = BillingV1CatalogCatalogItemResource()
        if include_optional:
            return BillingV1CatalogCatalogItemResource(
                id = 'hostingercom-vps-kvm2',
                name = 'KVM 2',
                category = 'VPS',
                prices = [
                    hostinger_api.models.billing/v1/catalog/catalog_item_price_resource.Billing.V1.Catalog.CatalogItemPriceResource(
                        id = 'hostingercom-vps-kvm2-usd-1m', 
                        name = 'KVM 2 (billed every month)', 
                        currency = 'USD', 
                        price = 1799, 
                        first_period_price = 899, 
                        period = 1, 
                        period_unit = 'day', )
                    ]
            )
        else:
            return BillingV1CatalogCatalogItemResource(
        )
        """

    def testBillingV1CatalogCatalogItemResource(self):
        """Test BillingV1CatalogCatalogItemResource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
