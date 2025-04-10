# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.5

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.common_schema_unprocessable_content_response_schema import CommonSchemaUnprocessableContentResponseSchema

class TestCommonSchemaUnprocessableContentResponseSchema(unittest.TestCase):
    """CommonSchemaUnprocessableContentResponseSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonSchemaUnprocessableContentResponseSchema:
        """Test CommonSchemaUnprocessableContentResponseSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonSchemaUnprocessableContentResponseSchema`
        """
        model = CommonSchemaUnprocessableContentResponseSchema()
        if include_optional:
            return CommonSchemaUnprocessableContentResponseSchema(
                message = 'The name field is required. (and 1 more error)',
                errors = hostinger_api.models.common_schema_unprocessable_content_response_schema_errors.Common_Schema_UnprocessableContentResponseSchema_errors(
                    field_1 = ["The field_1 field is required.","The field_1 must be a number."], 
                    field_2 = ["The field_2 field is required.","The field_2 must be a string."], ),
                correlation_id = '26a91bd9-f8c8-4a83-9df9-83e23d696fe3'
            )
        else:
            return CommonSchemaUnprocessableContentResponseSchema(
        )
        """

    def testCommonSchemaUnprocessableContentResponseSchema(self):
        """Test CommonSchemaUnprocessableContentResponseSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
