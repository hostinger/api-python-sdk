# EcommerceV1PaymentProviderPaymentProviderListResourceDataConnectedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The store payment provider row ID. | [optional] 
**provider_id** | **str** | The payment gateway ID, e.g. stripe. | [optional] 
**title** | **str** | The provider title, or null. | [optional] 
**is_enabled** | **bool** | Whether the provider is enabled for the store. | [optional] 
**status** | **str** | The connection status. | [optional] 
**shows_at_checkout** | **bool** | Whether the provider shows at checkout. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_payment_provider_payment_provider_list_resource_data_connected_inner import EcommerceV1PaymentProviderPaymentProviderListResourceDataConnectedInner

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1PaymentProviderPaymentProviderListResourceDataConnectedInner from a JSON string
ecommerce_v1_payment_provider_payment_provider_list_resource_data_connected_inner_instance = EcommerceV1PaymentProviderPaymentProviderListResourceDataConnectedInner.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1PaymentProviderPaymentProviderListResourceDataConnectedInner.to_json())

# convert the object into a dict
ecommerce_v1_payment_provider_payment_provider_list_resource_data_connected_inner_dict = ecommerce_v1_payment_provider_payment_provider_list_resource_data_connected_inner_instance.to_dict()
# create an instance of EcommerceV1PaymentProviderPaymentProviderListResourceDataConnectedInner from a dict
ecommerce_v1_payment_provider_payment_provider_list_resource_data_connected_inner_from_dict = EcommerceV1PaymentProviderPaymentProviderListResourceDataConnectedInner.from_dict(ecommerce_v1_payment_provider_payment_provider_list_resource_data_connected_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


