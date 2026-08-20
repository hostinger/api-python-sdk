# EcommerceV1OrderOrderDetailResourceItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The line item ID, required by the fulfil endpoint. | [optional] 
**title** | **str** | The line item title. | [optional] 
**sku** | **str** | The variant SKU. | [optional] 
**variant_id** | **str** | The variant ID. | [optional] 
**quantity** | **int** | Quantity ordered. | [optional] 
**fulfilled_quantity** | **int** | Quantity already fulfilled. | [optional] 
**returned_quantity** | **int** | Quantity returned. | [optional] 
**unit_price** | **int** | Unit price in the smallest currency unit. | [optional] 
**total** | **int** | Line total in the smallest currency unit. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_order_order_detail_resource_items_inner import EcommerceV1OrderOrderDetailResourceItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1OrderOrderDetailResourceItemsInner from a JSON string
ecommerce_v1_order_order_detail_resource_items_inner_instance = EcommerceV1OrderOrderDetailResourceItemsInner.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1OrderOrderDetailResourceItemsInner.to_json())

# convert the object into a dict
ecommerce_v1_order_order_detail_resource_items_inner_dict = ecommerce_v1_order_order_detail_resource_items_inner_instance.to_dict()
# create an instance of EcommerceV1OrderOrderDetailResourceItemsInner from a dict
ecommerce_v1_order_order_detail_resource_items_inner_from_dict = EcommerceV1OrderOrderDetailResourceItemsInner.from_dict(ecommerce_v1_order_order_detail_resource_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


