# EcommerceV1ProductProductResourcePriceRange

Effective price bounds across the product's variants.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** | Lowest effective variant price in the smallest currency unit, or null if unpriced. | [optional] 
**max** | **int** | Highest effective variant price in the smallest currency unit, or null if unpriced. | [optional] 
**currency_code** | **str** | The store currency the range is expressed in. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_product_product_resource_price_range import EcommerceV1ProductProductResourcePriceRange

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ProductProductResourcePriceRange from a JSON string
ecommerce_v1_product_product_resource_price_range_instance = EcommerceV1ProductProductResourcePriceRange.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ProductProductResourcePriceRange.to_json())

# convert the object into a dict
ecommerce_v1_product_product_resource_price_range_dict = ecommerce_v1_product_product_resource_price_range_instance.to_dict()
# create an instance of EcommerceV1ProductProductResourcePriceRange from a dict
ecommerce_v1_product_product_resource_price_range_from_dict = EcommerceV1ProductProductResourcePriceRange.from_dict(ecommerce_v1_product_product_resource_price_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


