# EcommerceV1ShippingShippingResourceShippingOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Shipping option ID. | [optional] 
**amount** | **int** | Flat shipping rate in the smallest currency unit (e.g. cents). | [optional] 
**currency_code** | **str** | Currency code the rate is charged in (ISO 4217, lowercase). | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_shipping_shipping_resource_shipping_option import EcommerceV1ShippingShippingResourceShippingOption

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ShippingShippingResourceShippingOption from a JSON string
ecommerce_v1_shipping_shipping_resource_shipping_option_instance = EcommerceV1ShippingShippingResourceShippingOption.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ShippingShippingResourceShippingOption.to_json())

# convert the object into a dict
ecommerce_v1_shipping_shipping_resource_shipping_option_dict = ecommerce_v1_shipping_shipping_resource_shipping_option_instance.to_dict()
# create an instance of EcommerceV1ShippingShippingResourceShippingOption from a dict
ecommerce_v1_shipping_shipping_resource_shipping_option_from_dict = EcommerceV1ShippingShippingResourceShippingOption.from_dict(ecommerce_v1_shipping_shipping_resource_shipping_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


