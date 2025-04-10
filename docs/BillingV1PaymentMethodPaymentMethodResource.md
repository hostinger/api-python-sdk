# BillingV1PaymentMethodPaymentMethodResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Payment method ID | [optional] 
**name** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**payment_method** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**is_expired** | **bool** |  | [optional] 
**is_suspended** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 

## Example

```python
from @hostinger/api.models.billing_v1_payment_method_payment_method_resource import BillingV1PaymentMethodPaymentMethodResource

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1PaymentMethodPaymentMethodResource from a JSON string
billing_v1_payment_method_payment_method_resource_instance = BillingV1PaymentMethodPaymentMethodResource.from_json(json)
# print the JSON string representation of the object
print(BillingV1PaymentMethodPaymentMethodResource.to_json())

# convert the object into a dict
billing_v1_payment_method_payment_method_resource_dict = billing_v1_payment_method_payment_method_resource_instance.to_dict()
# create an instance of BillingV1PaymentMethodPaymentMethodResource from a dict
billing_v1_payment_method_payment_method_resource_from_dict = BillingV1PaymentMethodPaymentMethodResource.from_dict(billing_v1_payment_method_payment_method_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


