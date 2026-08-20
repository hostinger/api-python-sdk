# EcommerceV1OrderFulfillRequestItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_item_id** | **str** | The line item to fulfil, from the order detail items[].id. | 
**quantity** | **int** | Quantity of the line item to fulfil. | 

## Example

```python
from hostinger_api.models.ecommerce_v1_order_fulfill_request_items_inner import EcommerceV1OrderFulfillRequestItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1OrderFulfillRequestItemsInner from a JSON string
ecommerce_v1_order_fulfill_request_items_inner_instance = EcommerceV1OrderFulfillRequestItemsInner.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1OrderFulfillRequestItemsInner.to_json())

# convert the object into a dict
ecommerce_v1_order_fulfill_request_items_inner_dict = ecommerce_v1_order_fulfill_request_items_inner_instance.to_dict()
# create an instance of EcommerceV1OrderFulfillRequestItemsInner from a dict
ecommerce_v1_order_fulfill_request_items_inner_from_dict = EcommerceV1OrderFulfillRequestItemsInner.from_dict(ecommerce_v1_order_fulfill_request_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


