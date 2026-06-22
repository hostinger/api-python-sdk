# EcommerceV1ShippingSetShippingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **int** | Flat shipping rate in the smallest currency unit (e.g. cents). Use 0 for free shipping. | 

## Example

```python
from hostinger_api.models.ecommerce_v1_shipping_set_shipping_request import EcommerceV1ShippingSetShippingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ShippingSetShippingRequest from a JSON string
ecommerce_v1_shipping_set_shipping_request_instance = EcommerceV1ShippingSetShippingRequest.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ShippingSetShippingRequest.to_json())

# convert the object into a dict
ecommerce_v1_shipping_set_shipping_request_dict = ecommerce_v1_shipping_set_shipping_request_instance.to_dict()
# create an instance of EcommerceV1ShippingSetShippingRequest from a dict
ecommerce_v1_shipping_set_shipping_request_from_dict = EcommerceV1ShippingSetShippingRequest.from_dict(ecommerce_v1_shipping_set_shipping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


