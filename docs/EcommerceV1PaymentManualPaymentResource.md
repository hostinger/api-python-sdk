# EcommerceV1PaymentManualPaymentResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | [**EcommerceV1PaymentManualPaymentResourcePaymentMethod**](EcommerceV1PaymentManualPaymentResourcePaymentMethod.md) |  | [optional] 
**admin_url** | **str** | Admin UI deep-link to manage payment settings. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_payment_manual_payment_resource import EcommerceV1PaymentManualPaymentResource

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1PaymentManualPaymentResource from a JSON string
ecommerce_v1_payment_manual_payment_resource_instance = EcommerceV1PaymentManualPaymentResource.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1PaymentManualPaymentResource.to_json())

# convert the object into a dict
ecommerce_v1_payment_manual_payment_resource_dict = ecommerce_v1_payment_manual_payment_resource_instance.to_dict()
# create an instance of EcommerceV1PaymentManualPaymentResource from a dict
ecommerce_v1_payment_manual_payment_resource_from_dict = EcommerceV1PaymentManualPaymentResource.from_dict(ecommerce_v1_payment_manual_payment_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


