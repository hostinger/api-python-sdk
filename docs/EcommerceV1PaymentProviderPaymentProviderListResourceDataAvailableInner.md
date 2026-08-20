# EcommerceV1PaymentProviderPaymentProviderListResourceDataAvailableInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The payment gateway ID, e.g. stripe. | [optional] 
**is_installed** | **bool** | Whether the gateway is installed on the store. | [optional] 
**is_enabled** | **bool** | Whether the gateway is enabled on the store. | [optional] 
**is_currency_supported** | **bool** | Whether the gateway supports the store currency. | [optional] 
**supported_currencies** | **List[str]** | Currencies the gateway supports; present only when the store currency is unsupported. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_payment_provider_payment_provider_list_resource_data_available_inner import EcommerceV1PaymentProviderPaymentProviderListResourceDataAvailableInner

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1PaymentProviderPaymentProviderListResourceDataAvailableInner from a JSON string
ecommerce_v1_payment_provider_payment_provider_list_resource_data_available_inner_instance = EcommerceV1PaymentProviderPaymentProviderListResourceDataAvailableInner.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1PaymentProviderPaymentProviderListResourceDataAvailableInner.to_json())

# convert the object into a dict
ecommerce_v1_payment_provider_payment_provider_list_resource_data_available_inner_dict = ecommerce_v1_payment_provider_payment_provider_list_resource_data_available_inner_instance.to_dict()
# create an instance of EcommerceV1PaymentProviderPaymentProviderListResourceDataAvailableInner from a dict
ecommerce_v1_payment_provider_payment_provider_list_resource_data_available_inner_from_dict = EcommerceV1PaymentProviderPaymentProviderListResourceDataAvailableInner.from_dict(ecommerce_v1_payment_provider_payment_provider_list_resource_data_available_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


