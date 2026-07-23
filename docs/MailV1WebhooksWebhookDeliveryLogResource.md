# MailV1WebhooksWebhookDeliveryLogResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**mailbox_address** | **str** | Email address of the mailbox this delivery is attached to | [optional] 
**webhook_url** | **str** | URL that received the webhook POST request | [optional] 
**is_successful** | **bool** | Whether the delivery was successful | [optional] 
**duration** | **int** | Webhook request duration in milliseconds | [optional] 
**retry_count** | **int** | Number of delivery attempts made | [optional] 
**max_retry_count** | **int** | Maximum number of delivery attempts allowed | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_webhooks_webhook_delivery_log_resource import MailV1WebhooksWebhookDeliveryLogResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1WebhooksWebhookDeliveryLogResource from a JSON string
mail_v1_webhooks_webhook_delivery_log_resource_instance = MailV1WebhooksWebhookDeliveryLogResource.from_json(json)
# print the JSON string representation of the object
print(MailV1WebhooksWebhookDeliveryLogResource.to_json())

# convert the object into a dict
mail_v1_webhooks_webhook_delivery_log_resource_dict = mail_v1_webhooks_webhook_delivery_log_resource_instance.to_dict()
# create an instance of MailV1WebhooksWebhookDeliveryLogResource from a dict
mail_v1_webhooks_webhook_delivery_log_resource_from_dict = MailV1WebhooksWebhookDeliveryLogResource.from_dict(mail_v1_webhooks_webhook_delivery_log_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


