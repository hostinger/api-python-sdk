# EcommerceV1PaymentManualPaymentResourcePaymentMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Store payment provider ID. | [optional] 
**provider_id** | **str** | The payment provider identifier. | [optional] 
**is_enabled** | **bool** | Whether the payment method is shown at checkout. | [optional] 
**title** | **str** | Display name shown to customers at checkout. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_payment_manual_payment_resource_payment_method import EcommerceV1PaymentManualPaymentResourcePaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1PaymentManualPaymentResourcePaymentMethod from a JSON string
ecommerce_v1_payment_manual_payment_resource_payment_method_instance = EcommerceV1PaymentManualPaymentResourcePaymentMethod.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1PaymentManualPaymentResourcePaymentMethod.to_json())

# convert the object into a dict
ecommerce_v1_payment_manual_payment_resource_payment_method_dict = ecommerce_v1_payment_manual_payment_resource_payment_method_instance.to_dict()
# create an instance of EcommerceV1PaymentManualPaymentResourcePaymentMethod from a dict
ecommerce_v1_payment_manual_payment_resource_payment_method_from_dict = EcommerceV1PaymentManualPaymentResourcePaymentMethod.from_dict(ecommerce_v1_payment_manual_payment_resource_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


