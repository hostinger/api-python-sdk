# MailV1SchemaCreateForwarderRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | Email address the messages will be forwarded to | 
**is_keep_copy_enabled** | **bool** | Whether to keep a copy of forwarded messages in the mailbox. Defaults to false. | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_schema_create_forwarder_request_schema import MailV1SchemaCreateForwarderRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1SchemaCreateForwarderRequestSchema from a JSON string
mail_v1_schema_create_forwarder_request_schema_instance = MailV1SchemaCreateForwarderRequestSchema.from_json(json)
# print the JSON string representation of the object
print(MailV1SchemaCreateForwarderRequestSchema.to_json())

# convert the object into a dict
mail_v1_schema_create_forwarder_request_schema_dict = mail_v1_schema_create_forwarder_request_schema_instance.to_dict()
# create an instance of MailV1SchemaCreateForwarderRequestSchema from a dict
mail_v1_schema_create_forwarder_request_schema_from_dict = MailV1SchemaCreateForwarderRequestSchema.from_dict(mail_v1_schema_create_forwarder_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


