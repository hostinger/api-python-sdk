# MailV1SchemaUpdateWebhookRequestSchema

Fields to update. All fields are optional; only provided fields are changed. Pass `\"description\": null` to clear the description.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New human-readable name for the webhook | [optional] 
**description** | **str** | New description, or null to clear it | [optional] 
**events** | **List[str]** | Replaces the full list of subscribed events | [optional] 
**status** | **str** | New status for the webhook | [optional] 
**url** | **str** | New URL to deliver events to | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_schema_update_webhook_request_schema import MailV1SchemaUpdateWebhookRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1SchemaUpdateWebhookRequestSchema from a JSON string
mail_v1_schema_update_webhook_request_schema_instance = MailV1SchemaUpdateWebhookRequestSchema.from_json(json)
# print the JSON string representation of the object
print(MailV1SchemaUpdateWebhookRequestSchema.to_json())

# convert the object into a dict
mail_v1_schema_update_webhook_request_schema_dict = mail_v1_schema_update_webhook_request_schema_instance.to_dict()
# create an instance of MailV1SchemaUpdateWebhookRequestSchema from a dict
mail_v1_schema_update_webhook_request_schema_from_dict = MailV1SchemaUpdateWebhookRequestSchema.from_dict(mail_v1_schema_update_webhook_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


