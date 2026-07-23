# MailV1SchemaCreateApiTokenRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable label for this token | 
**scope** | [**MailV1SchemaCreateApiTokenRequestSchemaScope**](MailV1SchemaCreateApiTokenRequestSchemaScope.md) |  | 

## Example

```python
from hostinger_api.models.mail_v1_schema_create_api_token_request_schema import MailV1SchemaCreateApiTokenRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1SchemaCreateApiTokenRequestSchema from a JSON string
mail_v1_schema_create_api_token_request_schema_instance = MailV1SchemaCreateApiTokenRequestSchema.from_json(json)
# print the JSON string representation of the object
print(MailV1SchemaCreateApiTokenRequestSchema.to_json())

# convert the object into a dict
mail_v1_schema_create_api_token_request_schema_dict = mail_v1_schema_create_api_token_request_schema_instance.to_dict()
# create an instance of MailV1SchemaCreateApiTokenRequestSchema from a dict
mail_v1_schema_create_api_token_request_schema_from_dict = MailV1SchemaCreateApiTokenRequestSchema.from_dict(mail_v1_schema_create_api_token_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


