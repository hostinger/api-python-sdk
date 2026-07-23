# BillingV1OrderPurchaseRequestItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Catalog price item ID | 
**quantity** | **int** | Quantity to purchase | [optional] [default to 1]

## Example

```python
from hostinger_api.models.billing_v1_order_purchase_request_items_inner import BillingV1OrderPurchaseRequestItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1OrderPurchaseRequestItemsInner from a JSON string
billing_v1_order_purchase_request_items_inner_instance = BillingV1OrderPurchaseRequestItemsInner.from_json(json)
# print the JSON string representation of the object
print(BillingV1OrderPurchaseRequestItemsInner.to_json())

# convert the object into a dict
billing_v1_order_purchase_request_items_inner_dict = billing_v1_order_purchase_request_items_inner_instance.to_dict()
# create an instance of BillingV1OrderPurchaseRequestItemsInner from a dict
billing_v1_order_purchase_request_items_inner_from_dict = BillingV1OrderPurchaseRequestItemsInner.from_dict(billing_v1_order_purchase_request_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


