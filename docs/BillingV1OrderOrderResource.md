# BillingV1OrderOrderResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Order ID | [optional] 
**subscription_id** | **str** | Subscription ID | [optional] 
**status** | **str** |  | [optional] 
**currency** | **str** | Currency code | [optional] 
**subtotal** | **int** | Subtotal price (exc. VAT) in cents | [optional] 
**total** | **int** | Total price (inc. VAT) in cents | [optional] 
**billing_address** | [**BillingV1OrderOrderBillingAddressResource**](BillingV1OrderOrderBillingAddressResource.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger-api.models.billing_v1_order_order_resource import BillingV1OrderOrderResource

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1OrderOrderResource from a JSON string
billing_v1_order_order_resource_instance = BillingV1OrderOrderResource.from_json(json)
# print the JSON string representation of the object
print(BillingV1OrderOrderResource.to_json())

# convert the object into a dict
billing_v1_order_order_resource_dict = billing_v1_order_order_resource_instance.to_dict()
# create an instance of BillingV1OrderOrderResource from a dict
billing_v1_order_order_resource_from_dict = BillingV1OrderOrderResource.from_dict(billing_v1_order_order_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


