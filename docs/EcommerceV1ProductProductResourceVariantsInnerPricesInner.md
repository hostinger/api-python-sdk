# EcommerceV1ProductProductResourceVariantsInnerPricesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Price in the smallest currency unit. | [optional] 
**sale_amount** | **int** | Sale price in the smallest currency unit, or null. | [optional] 
**currency_code** | **str** | The price currency code. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_product_product_resource_variants_inner_prices_inner import EcommerceV1ProductProductResourceVariantsInnerPricesInner

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ProductProductResourceVariantsInnerPricesInner from a JSON string
ecommerce_v1_product_product_resource_variants_inner_prices_inner_instance = EcommerceV1ProductProductResourceVariantsInnerPricesInner.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ProductProductResourceVariantsInnerPricesInner.to_json())

# convert the object into a dict
ecommerce_v1_product_product_resource_variants_inner_prices_inner_dict = ecommerce_v1_product_product_resource_variants_inner_prices_inner_instance.to_dict()
# create an instance of EcommerceV1ProductProductResourceVariantsInnerPricesInner from a dict
ecommerce_v1_product_product_resource_variants_inner_prices_inner_from_dict = EcommerceV1ProductProductResourceVariantsInnerPricesInner.from_dict(ecommerce_v1_product_product_resource_variants_inner_prices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


