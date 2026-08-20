# EcommerceV1PaymentProviderPaymentProviderListResourceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected** | [**List[EcommerceV1PaymentProviderPaymentProviderListResourceDataConnectedInner]**](EcommerceV1PaymentProviderPaymentProviderListResourceDataConnectedInner.md) | Payment providers already connected to the store. | [optional] 
**available** | [**List[EcommerceV1PaymentProviderPaymentProviderListResourceDataAvailableInner]**](EcommerceV1PaymentProviderPaymentProviderListResourceDataAvailableInner.md) | Payment gateways available to install for the store. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_payment_provider_payment_provider_list_resource_data import EcommerceV1PaymentProviderPaymentProviderListResourceData

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1PaymentProviderPaymentProviderListResourceData from a JSON string
ecommerce_v1_payment_provider_payment_provider_list_resource_data_instance = EcommerceV1PaymentProviderPaymentProviderListResourceData.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1PaymentProviderPaymentProviderListResourceData.to_json())

# convert the object into a dict
ecommerce_v1_payment_provider_payment_provider_list_resource_data_dict = ecommerce_v1_payment_provider_payment_provider_list_resource_data_instance.to_dict()
# create an instance of EcommerceV1PaymentProviderPaymentProviderListResourceData from a dict
ecommerce_v1_payment_provider_payment_provider_list_resource_data_from_dict = EcommerceV1PaymentProviderPaymentProviderListResourceData.from_dict(ecommerce_v1_payment_provider_payment_provider_list_resource_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


