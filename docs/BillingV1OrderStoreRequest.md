# BillingV1OrderStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_id** | **int** | Payment method ID | 
**items** | [**List[BillingV1OrderStoreRequestItemsInner]**](BillingV1OrderStoreRequestItemsInner.md) |  | 
**coupons** | **List[object]** |  | [optional] 

## Example

```python
from hostinger_api.models.billing_v1_order_store_request import BillingV1OrderStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1OrderStoreRequest from a JSON string
billing_v1_order_store_request_instance = BillingV1OrderStoreRequest.from_json(json)
# print the JSON string representation of the object
print(BillingV1OrderStoreRequest.to_json())

# convert the object into a dict
billing_v1_order_store_request_dict = billing_v1_order_store_request_instance.to_dict()
# create an instance of BillingV1OrderStoreRequest from a dict
billing_v1_order_store_request_from_dict = BillingV1OrderStoreRequest.from_dict(billing_v1_order_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


