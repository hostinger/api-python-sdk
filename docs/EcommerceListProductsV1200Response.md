# EcommerceListProductsV1200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EcommerceV1ProductProductResource]**](EcommerceV1ProductProductResource.md) | Array of [&#x60;Ecommerce.V1.Product.ProductResource&#x60;](#model/ecommercev1productproductresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_list_products_v1200_response import EcommerceListProductsV1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceListProductsV1200Response from a JSON string
ecommerce_list_products_v1200_response_instance = EcommerceListProductsV1200Response.from_json(json)
# print the JSON string representation of the object
print(EcommerceListProductsV1200Response.to_json())

# convert the object into a dict
ecommerce_list_products_v1200_response_dict = ecommerce_list_products_v1200_response_instance.to_dict()
# create an instance of EcommerceListProductsV1200Response from a dict
ecommerce_list_products_v1200_response_from_dict = EcommerceListProductsV1200Response.from_dict(ecommerce_list_products_v1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


