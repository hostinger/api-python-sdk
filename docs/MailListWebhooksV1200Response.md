# MailListWebhooksV1200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MailV1WebhooksWebhookResource]**](MailV1WebhooksWebhookResource.md) | Array of [&#x60;Mail.V1.Webhooks.WebhookResource&#x60;](#model/mailv1webhookswebhookresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.mail_list_webhooks_v1200_response import MailListWebhooksV1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MailListWebhooksV1200Response from a JSON string
mail_list_webhooks_v1200_response_instance = MailListWebhooksV1200Response.from_json(json)
# print the JSON string representation of the object
print(MailListWebhooksV1200Response.to_json())

# convert the object into a dict
mail_list_webhooks_v1200_response_dict = mail_list_webhooks_v1200_response_instance.to_dict()
# create an instance of MailListWebhooksV1200Response from a dict
mail_list_webhooks_v1200_response_from_dict = MailListWebhooksV1200Response.from_dict(mail_list_webhooks_v1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


