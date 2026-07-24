# MailV1SchemaUpsertAutoreplyRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Subject of the automatic reply | 
**body** | **str** | Body of the automatic reply | 
**display_name** | **str** | Sender display name used for the reply | [optional] 
**starts_at** | **datetime** | When the autoreply becomes active. Defaults to now. | [optional] 
**ends_at** | **datetime** | When the autoreply stops. Omit for an indefinite autoreply. | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_schema_upsert_autoreply_request_schema import MailV1SchemaUpsertAutoreplyRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1SchemaUpsertAutoreplyRequestSchema from a JSON string
mail_v1_schema_upsert_autoreply_request_schema_instance = MailV1SchemaUpsertAutoreplyRequestSchema.from_json(json)
# print the JSON string representation of the object
print(MailV1SchemaUpsertAutoreplyRequestSchema.to_json())

# convert the object into a dict
mail_v1_schema_upsert_autoreply_request_schema_dict = mail_v1_schema_upsert_autoreply_request_schema_instance.to_dict()
# create an instance of MailV1SchemaUpsertAutoreplyRequestSchema from a dict
mail_v1_schema_upsert_autoreply_request_schema_from_dict = MailV1SchemaUpsertAutoreplyRequestSchema.from_dict(mail_v1_schema_upsert_autoreply_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


