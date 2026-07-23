# MailV1WebhooksWebhookResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique webhook identifier | [optional] 
**mailbox** | [**MailV1WebhooksWebhookMailboxResource**](MailV1WebhooksWebhookMailboxResource.md) |  | [optional] 
**name** | **str** | Human-readable name for this webhook | [optional] 
**description** | **str** | Optional description of the webhook&#39;s purpose | [optional] 
**events** | **List[str]** | Events that trigger this webhook | [optional] 
**status** | **str** | Current status of the webhook | [optional] 
**url** | **str** | URL that receives webhook POST requests | [optional] 
**secret** | **str** | One-time webhook secret, returned only on creation. Sent as &#x60;Authorization: Bearer &lt;secret&gt;&#x60; with every delivery. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_webhooks_webhook_resource import MailV1WebhooksWebhookResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1WebhooksWebhookResource from a JSON string
mail_v1_webhooks_webhook_resource_instance = MailV1WebhooksWebhookResource.from_json(json)
# print the JSON string representation of the object
print(MailV1WebhooksWebhookResource.to_json())

# convert the object into a dict
mail_v1_webhooks_webhook_resource_dict = mail_v1_webhooks_webhook_resource_instance.to_dict()
# create an instance of MailV1WebhooksWebhookResource from a dict
mail_v1_webhooks_webhook_resource_from_dict = MailV1WebhooksWebhookResource.from_dict(mail_v1_webhooks_webhook_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


