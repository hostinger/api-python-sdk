# MailV1WebhooksWebhookTestResultResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_status** | **int** | HTTP status code returned by the webhook endpoint | [optional] 
**is_successful** | **bool** | Whether the test delivery was successful | [optional] 
**error** | **str** | Error message returned by the webhook endpoint in case of failure | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_webhooks_webhook_test_result_resource import MailV1WebhooksWebhookTestResultResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1WebhooksWebhookTestResultResource from a JSON string
mail_v1_webhooks_webhook_test_result_resource_instance = MailV1WebhooksWebhookTestResultResource.from_json(json)
# print the JSON string representation of the object
print(MailV1WebhooksWebhookTestResultResource.to_json())

# convert the object into a dict
mail_v1_webhooks_webhook_test_result_resource_dict = mail_v1_webhooks_webhook_test_result_resource_instance.to_dict()
# create an instance of MailV1WebhooksWebhookTestResultResource from a dict
mail_v1_webhooks_webhook_test_result_resource_from_dict = MailV1WebhooksWebhookTestResultResource.from_dict(mail_v1_webhooks_webhook_test_result_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


