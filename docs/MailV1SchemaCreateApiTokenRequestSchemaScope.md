# MailV1SchemaCreateApiTokenRequestSchemaScope

Mailbox scope this token can access

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_all_mailboxes** | **bool** | Grant access to all current and future mailboxes of the order | 
**mailbox_ids** | **List[str]** | Required when &#x60;has_all_mailboxes&#x60; is false. Mailbox resource IDs of this order. | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_schema_create_api_token_request_schema_scope import MailV1SchemaCreateApiTokenRequestSchemaScope

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1SchemaCreateApiTokenRequestSchemaScope from a JSON string
mail_v1_schema_create_api_token_request_schema_scope_instance = MailV1SchemaCreateApiTokenRequestSchemaScope.from_json(json)
# print the JSON string representation of the object
print(MailV1SchemaCreateApiTokenRequestSchemaScope.to_json())

# convert the object into a dict
mail_v1_schema_create_api_token_request_schema_scope_dict = mail_v1_schema_create_api_token_request_schema_scope_instance.to_dict()
# create an instance of MailV1SchemaCreateApiTokenRequestSchemaScope from a dict
mail_v1_schema_create_api_token_request_schema_scope_from_dict = MailV1SchemaCreateApiTokenRequestSchemaScope.from_dict(mail_v1_schema_create_api_token_request_schema_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


