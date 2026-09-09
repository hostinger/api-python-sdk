# BillingV1OrderPaymentProcessingResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Order ID | [optional] 
**subscription_id** | **str** | Subscription ID, use it to find the product once the order completes | [optional] 
**status** | **str** |  | [optional] 
**message** | **str** | Explanation of what happens next | [optional] 

## Example

```python
from hostinger_api.models.billing_v1_order_payment_processing_resource import BillingV1OrderPaymentProcessingResource

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1OrderPaymentProcessingResource from a JSON string
billing_v1_order_payment_processing_resource_instance = BillingV1OrderPaymentProcessingResource.from_json(json)
# print the JSON string representation of the object
print(BillingV1OrderPaymentProcessingResource.to_json())

# convert the object into a dict
billing_v1_order_payment_processing_resource_dict = billing_v1_order_payment_processing_resource_instance.to_dict()
# create an instance of BillingV1OrderPaymentProcessingResource from a dict
billing_v1_order_payment_processing_resource_from_dict = BillingV1OrderPaymentProcessingResource.from_dict(billing_v1_order_payment_processing_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


