# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.3

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.common_schema_unprocessable_content_response_schema_errors import CommonSchemaUnprocessableContentResponseSchemaErrors

class TestCommonSchemaUnprocessableContentResponseSchemaErrors(unittest.TestCase):
    """CommonSchemaUnprocessableContentResponseSchemaErrors unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonSchemaUnprocessableContentResponseSchemaErrors:
        """Test CommonSchemaUnprocessableContentResponseSchemaErrors
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonSchemaUnprocessableContentResponseSchemaErrors`
        """
        model = CommonSchemaUnprocessableContentResponseSchemaErrors()
        if include_optional:
            return CommonSchemaUnprocessableContentResponseSchemaErrors(
                field_1 = ["The field_1 field is required.","The field_1 must be a number."],
                field_2 = ["The field_2 field is required.","The field_2 must be a string."]
            )
        else:
            return CommonSchemaUnprocessableContentResponseSchemaErrors(
        )
        """

    def testCommonSchemaUnprocessableContentResponseSchemaErrors(self):
        """Test CommonSchemaUnprocessableContentResponseSchemaErrors"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
