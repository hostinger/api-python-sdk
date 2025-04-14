# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.20

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


import unittest

from hostinger_api.models.common_schema_pagination_meta_schema import CommonSchemaPaginationMetaSchema

class TestCommonSchemaPaginationMetaSchema(unittest.TestCase):
    """CommonSchemaPaginationMetaSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonSchemaPaginationMetaSchema:
        """Test CommonSchemaPaginationMetaSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonSchemaPaginationMetaSchema`
        """
        model = CommonSchemaPaginationMetaSchema()
        if include_optional:
            return CommonSchemaPaginationMetaSchema(
                current_page = 1,
                per_page = 15,
                total = 100
            )
        else:
            return CommonSchemaPaginationMetaSchema(
        )
        """

    def testCommonSchemaPaginationMetaSchema(self):
        """Test CommonSchemaPaginationMetaSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
