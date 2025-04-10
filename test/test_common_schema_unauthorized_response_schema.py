# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.6

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.common_schema_unauthorized_response_schema import CommonSchemaUnauthorizedResponseSchema

class TestCommonSchemaUnauthorizedResponseSchema(unittest.TestCase):
    """CommonSchemaUnauthorizedResponseSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonSchemaUnauthorizedResponseSchema:
        """Test CommonSchemaUnauthorizedResponseSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonSchemaUnauthorizedResponseSchema`
        """
        model = CommonSchemaUnauthorizedResponseSchema()
        if include_optional:
            return CommonSchemaUnauthorizedResponseSchema(
                message = 'Unauthenticated',
                correlation_id = '26a91bd9-f8c8-4a83-9df9-83e23d696fe3'
            )
        else:
            return CommonSchemaUnauthorizedResponseSchema(
        )
        """

    def testCommonSchemaUnauthorizedResponseSchema(self):
        """Test CommonSchemaUnauthorizedResponseSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
