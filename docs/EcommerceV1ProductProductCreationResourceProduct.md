# EcommerceV1ProductProductCreationResourceProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Product ID. | [optional] 
**title** | **str** | Product name. | [optional] 
**type** | **str** | Product type. | [optional] 
**status** | **str** | Product status. | [optional] 
**price** | **int** | Price in the smallest currency unit (e.g. cents). | [optional] 
**currency_code** | **str** | Currency the product is priced in (ISO 4217, lowercase). | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_product_product_creation_resource_product import EcommerceV1ProductProductCreationResourceProduct

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ProductProductCreationResourceProduct from a JSON string
ecommerce_v1_product_product_creation_resource_product_instance = EcommerceV1ProductProductCreationResourceProduct.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ProductProductCreationResourceProduct.to_json())

# convert the object into a dict
ecommerce_v1_product_product_creation_resource_product_dict = ecommerce_v1_product_product_creation_resource_product_instance.to_dict()
# create an instance of EcommerceV1ProductProductCreationResourceProduct from a dict
ecommerce_v1_product_product_creation_resource_product_from_dict = EcommerceV1ProductProductCreationResourceProduct.from_dict(ecommerce_v1_product_product_creation_resource_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


