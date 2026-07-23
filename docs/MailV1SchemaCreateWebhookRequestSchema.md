# MailV1SchemaCreateWebhookRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for this webhook | 
**description** | **str** | Optional description of the webhook&#39;s purpose | [optional] 
**events** | **List[str]** | Events that trigger this webhook | 
**status** | **str** | Initial status of the webhook | [optional] [default to 'active']
**url** | **str** | Publicly reachable URL that receives the webhook POST requests | 

## Example

```python
from hostinger_api.models.mail_v1_schema_create_webhook_request_schema import MailV1SchemaCreateWebhookRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1SchemaCreateWebhookRequestSchema from a JSON string
mail_v1_schema_create_webhook_request_schema_instance = MailV1SchemaCreateWebhookRequestSchema.from_json(json)
# print the JSON string representation of the object
print(MailV1SchemaCreateWebhookRequestSchema.to_json())

# convert the object into a dict
mail_v1_schema_create_webhook_request_schema_dict = mail_v1_schema_create_webhook_request_schema_instance.to_dict()
# create an instance of MailV1SchemaCreateWebhookRequestSchema from a dict
mail_v1_schema_create_webhook_request_schema_from_dict = MailV1SchemaCreateWebhookRequestSchema.from_dict(mail_v1_schema_create_webhook_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


