# EcommerceListProductVariantsV1200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EcommerceV1VariantVariantResource]**](EcommerceV1VariantVariantResource.md) | Array of [&#x60;Ecommerce.V1.Variant.VariantResource&#x60;](#model/ecommercev1variantvariantresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_list_product_variants_v1200_response import EcommerceListProductVariantsV1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceListProductVariantsV1200Response from a JSON string
ecommerce_list_product_variants_v1200_response_instance = EcommerceListProductVariantsV1200Response.from_json(json)
# print the JSON string representation of the object
print(EcommerceListProductVariantsV1200Response.to_json())

# convert the object into a dict
ecommerce_list_product_variants_v1200_response_dict = ecommerce_list_product_variants_v1200_response_instance.to_dict()
# create an instance of EcommerceListProductVariantsV1200Response from a dict
ecommerce_list_product_variants_v1200_response_from_dict = EcommerceListProductVariantsV1200Response.from_dict(ecommerce_list_product_variants_v1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


