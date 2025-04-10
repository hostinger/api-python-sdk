# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.6

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.api.billing_payment_methods_api import BillingPaymentMethodsApi


class TestBillingPaymentMethodsApi(unittest.TestCase):
    """BillingPaymentMethodsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BillingPaymentMethodsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_payment_method_v1(self) -> None:
        """Test case for delete_payment_method_v1

        Delete payment method
        """
        pass

    def test_get_payment_method_list_v1(self) -> None:
        """Test case for get_payment_method_list_v1

        Get payment method list
        """
        pass

    def test_set_default_payment_method_v1(self) -> None:
        """Test case for set_default_payment_method_v1

        Set default payment method
        """
        pass


if __name__ == '__main__':
    unittest.main()
