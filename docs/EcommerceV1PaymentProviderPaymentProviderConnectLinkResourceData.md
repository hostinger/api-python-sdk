# EcommerceV1PaymentProviderPaymentProviderConnectLinkResourceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The gateway onboarding URL for the merchant to open. | [optional] 
**admin_url** | **str** | A deep-link into the store admin for the provider. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_payment_provider_payment_provider_connect_link_resource_data import EcommerceV1PaymentProviderPaymentProviderConnectLinkResourceData

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1PaymentProviderPaymentProviderConnectLinkResourceData from a JSON string
ecommerce_v1_payment_provider_payment_provider_connect_link_resource_data_instance = EcommerceV1PaymentProviderPaymentProviderConnectLinkResourceData.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1PaymentProviderPaymentProviderConnectLinkResourceData.to_json())

# convert the object into a dict
ecommerce_v1_payment_provider_payment_provider_connect_link_resource_data_dict = ecommerce_v1_payment_provider_payment_provider_connect_link_resource_data_instance.to_dict()
# create an instance of EcommerceV1PaymentProviderPaymentProviderConnectLinkResourceData from a dict
ecommerce_v1_payment_provider_payment_provider_connect_link_resource_data_from_dict = EcommerceV1PaymentProviderPaymentProviderConnectLinkResourceData.from_dict(ecommerce_v1_payment_provider_payment_provider_connect_link_resource_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


