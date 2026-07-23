# MailV1SchemaCreateMailboxRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_part** | **str** | Local part of the mailbox address (the part before the @). The domain is taken from the order. Must start and end with a letter or digit; single dots, underscores and hyphens are allowed in between. | 
**password** | **str** | Mailbox password. Minimum 8 characters with uppercase, lowercase, number and special character. | 

## Example

```python
from hostinger_api.models.mail_v1_schema_create_mailbox_request_schema import MailV1SchemaCreateMailboxRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1SchemaCreateMailboxRequestSchema from a JSON string
mail_v1_schema_create_mailbox_request_schema_instance = MailV1SchemaCreateMailboxRequestSchema.from_json(json)
# print the JSON string representation of the object
print(MailV1SchemaCreateMailboxRequestSchema.to_json())

# convert the object into a dict
mail_v1_schema_create_mailbox_request_schema_dict = mail_v1_schema_create_mailbox_request_schema_instance.to_dict()
# create an instance of MailV1SchemaCreateMailboxRequestSchema from a dict
mail_v1_schema_create_mailbox_request_schema_from_dict = MailV1SchemaCreateMailboxRequestSchema.from_dict(mail_v1_schema_create_mailbox_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


