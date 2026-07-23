# BillingV1OrderPurchaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_id** | **int** | Payment method ID, default will be used if not provided | [optional] 
**items** | [**List[BillingV1OrderPurchaseRequestItemsInner]**](BillingV1OrderPurchaseRequestItemsInner.md) | Catalog price items to purchase | 
**coupons** | **List[object]** | Discount coupon codes | [optional] 

## Example

```python
from hostinger_api.models.billing_v1_order_purchase_request import BillingV1OrderPurchaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1OrderPurchaseRequest from a JSON string
billing_v1_order_purchase_request_instance = BillingV1OrderPurchaseRequest.from_json(json)
# print the JSON string representation of the object
print(BillingV1OrderPurchaseRequest.to_json())

# convert the object into a dict
billing_v1_order_purchase_request_dict = billing_v1_order_purchase_request_instance.to_dict()
# create an instance of BillingV1OrderPurchaseRequest from a dict
billing_v1_order_purchase_request_from_dict = BillingV1OrderPurchaseRequest.from_dict(billing_v1_order_purchase_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


