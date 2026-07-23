# MailV1SchemaChangeMailboxPasswordRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | New mailbox password. Minimum 8 characters with uppercase, lowercase, number and special character; must not be a commonly used password. | 

## Example

```python
from hostinger_api.models.mail_v1_schema_change_mailbox_password_request_schema import MailV1SchemaChangeMailboxPasswordRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1SchemaChangeMailboxPasswordRequestSchema from a JSON string
mail_v1_schema_change_mailbox_password_request_schema_instance = MailV1SchemaChangeMailboxPasswordRequestSchema.from_json(json)
# print the JSON string representation of the object
print(MailV1SchemaChangeMailboxPasswordRequestSchema.to_json())

# convert the object into a dict
mail_v1_schema_change_mailbox_password_request_schema_dict = mail_v1_schema_change_mailbox_password_request_schema_instance.to_dict()
# create an instance of MailV1SchemaChangeMailboxPasswordRequestSchema from a dict
mail_v1_schema_change_mailbox_password_request_schema_from_dict = MailV1SchemaChangeMailboxPasswordRequestSchema.from_dict(mail_v1_schema_change_mailbox_password_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


