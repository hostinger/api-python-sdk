# EcommerceV1PaymentEnableManualPaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Optional display name shown to customers at checkout. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_payment_enable_manual_payment_request import EcommerceV1PaymentEnableManualPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1PaymentEnableManualPaymentRequest from a JSON string
ecommerce_v1_payment_enable_manual_payment_request_instance = EcommerceV1PaymentEnableManualPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1PaymentEnableManualPaymentRequest.to_json())

# convert the object into a dict
ecommerce_v1_payment_enable_manual_payment_request_dict = ecommerce_v1_payment_enable_manual_payment_request_instance.to_dict()
# create an instance of EcommerceV1PaymentEnableManualPaymentRequest from a dict
ecommerce_v1_payment_enable_manual_payment_request_from_dict = EcommerceV1PaymentEnableManualPaymentRequest.from_dict(ecommerce_v1_payment_enable_manual_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


