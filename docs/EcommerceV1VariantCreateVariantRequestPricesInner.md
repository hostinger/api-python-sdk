# EcommerceV1VariantCreateVariantRequestPricesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Price in the smallest currency unit (e.g. cents). | 
**sale_amount** | **int** | Optional sale price in the smallest currency unit; must be lower than amount. | [optional] 
**currency** | **str** | ISO 4217 currency code. Defaults to the store&#39;s default currency when omitted. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_variant_create_variant_request_prices_inner import EcommerceV1VariantCreateVariantRequestPricesInner

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1VariantCreateVariantRequestPricesInner from a JSON string
ecommerce_v1_variant_create_variant_request_prices_inner_instance = EcommerceV1VariantCreateVariantRequestPricesInner.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1VariantCreateVariantRequestPricesInner.to_json())

# convert the object into a dict
ecommerce_v1_variant_create_variant_request_prices_inner_dict = ecommerce_v1_variant_create_variant_request_prices_inner_instance.to_dict()
# create an instance of EcommerceV1VariantCreateVariantRequestPricesInner from a dict
ecommerce_v1_variant_create_variant_request_prices_inner_from_dict = EcommerceV1VariantCreateVariantRequestPricesInner.from_dict(ecommerce_v1_variant_create_variant_request_prices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


