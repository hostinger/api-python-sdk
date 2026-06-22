# EcommerceV1ShippingShippingResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_option** | [**EcommerceV1ShippingShippingResourceShippingOption**](EcommerceV1ShippingShippingResourceShippingOption.md) |  | [optional] 
**admin_url** | **str** | Admin UI deep-link to manage shipping settings. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_shipping_shipping_resource import EcommerceV1ShippingShippingResource

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ShippingShippingResource from a JSON string
ecommerce_v1_shipping_shipping_resource_instance = EcommerceV1ShippingShippingResource.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ShippingShippingResource.to_json())

# convert the object into a dict
ecommerce_v1_shipping_shipping_resource_dict = ecommerce_v1_shipping_shipping_resource_instance.to_dict()
# create an instance of EcommerceV1ShippingShippingResource from a dict
ecommerce_v1_shipping_shipping_resource_from_dict = EcommerceV1ShippingShippingResource.from_dict(ecommerce_v1_shipping_shipping_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


