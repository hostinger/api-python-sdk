# MailV1SchemaCreateAliasRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_part** | **str** | Local part of the alias address (the part before the @). The domain is taken from the mailbox. Case-insensitive and stored lowercase; must start and end with a letter or digit; single dots, underscores and hyphens are allowed in between. | 

## Example

```python
from hostinger_api.models.mail_v1_schema_create_alias_request_schema import MailV1SchemaCreateAliasRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1SchemaCreateAliasRequestSchema from a JSON string
mail_v1_schema_create_alias_request_schema_instance = MailV1SchemaCreateAliasRequestSchema.from_json(json)
# print the JSON string representation of the object
print(MailV1SchemaCreateAliasRequestSchema.to_json())

# convert the object into a dict
mail_v1_schema_create_alias_request_schema_dict = mail_v1_schema_create_alias_request_schema_instance.to_dict()
# create an instance of MailV1SchemaCreateAliasRequestSchema from a dict
mail_v1_schema_create_alias_request_schema_from_dict = MailV1SchemaCreateAliasRequestSchema.from_dict(mail_v1_schema_create_alias_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


