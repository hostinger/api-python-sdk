# BillingV1OrderStoreRequestItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Price Item ID | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from hostinger_api.models.billing_v1_order_store_request_items_inner import BillingV1OrderStoreRequestItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1OrderStoreRequestItemsInner from a JSON string
billing_v1_order_store_request_items_inner_instance = BillingV1OrderStoreRequestItemsInner.from_json(json)
# print the JSON string representation of the object
print(BillingV1OrderStoreRequestItemsInner.to_json())

# convert the object into a dict
billing_v1_order_store_request_items_inner_dict = billing_v1_order_store_request_items_inner_instance.to_dict()
# create an instance of BillingV1OrderStoreRequestItemsInner from a dict
billing_v1_order_store_request_items_inner_from_dict = BillingV1OrderStoreRequestItemsInner.from_dict(billing_v1_order_store_request_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


