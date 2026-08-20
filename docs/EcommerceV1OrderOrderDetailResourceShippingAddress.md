# EcommerceV1OrderOrderDetailResourceShippingAddress

The shipping address, or null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**address_1** | **str** |  | [optional] 
**address_2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**province_code** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_order_order_detail_resource_shipping_address import EcommerceV1OrderOrderDetailResourceShippingAddress

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1OrderOrderDetailResourceShippingAddress from a JSON string
ecommerce_v1_order_order_detail_resource_shipping_address_instance = EcommerceV1OrderOrderDetailResourceShippingAddress.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1OrderOrderDetailResourceShippingAddress.to_json())

# convert the object into a dict
ecommerce_v1_order_order_detail_resource_shipping_address_dict = ecommerce_v1_order_order_detail_resource_shipping_address_instance.to_dict()
# create an instance of EcommerceV1OrderOrderDetailResourceShippingAddress from a dict
ecommerce_v1_order_order_detail_resource_shipping_address_from_dict = EcommerceV1OrderOrderDetailResourceShippingAddress.from_dict(ecommerce_v1_order_order_detail_resource_shipping_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


