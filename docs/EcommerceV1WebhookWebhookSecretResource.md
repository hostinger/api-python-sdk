# EcommerceV1WebhookWebhookSecretResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | [**EcommerceV1WebhookWebhookEndpointResource**](EcommerceV1WebhookWebhookEndpointResource.md) |  | 
**secret** | **str** | New whsec_ signing secret, returned only on create or rotation. Save securely. | 

## Example

```python
from hostinger_api.models.ecommerce_v1_webhook_webhook_secret_resource import EcommerceV1WebhookWebhookSecretResource

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1WebhookWebhookSecretResource from a JSON string
ecommerce_v1_webhook_webhook_secret_resource_instance = EcommerceV1WebhookWebhookSecretResource.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1WebhookWebhookSecretResource.to_json())

# convert the object into a dict
ecommerce_v1_webhook_webhook_secret_resource_dict = ecommerce_v1_webhook_webhook_secret_resource_instance.to_dict()
# create an instance of EcommerceV1WebhookWebhookSecretResource from a dict
ecommerce_v1_webhook_webhook_secret_resource_from_dict = EcommerceV1WebhookWebhookSecretResource.from_dict(ecommerce_v1_webhook_webhook_secret_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


