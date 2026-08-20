# EcommerceV1ProductProductResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The product ID, required by every other product endpoint. | [optional] 
**title** | **str** | The product name. | [optional] 
**status** | **str** | The product status. | [optional] 
**thumbnail** | **str** | The product&#39;s primary image URL, or null. | [optional] 
**type** | **str** | The product type. | [optional] 
**variant_count** | **int** | Number of variants. Use include&#x3D;variants to retrieve them. | [optional] 
**price_range** | [**EcommerceV1ProductProductResourcePriceRange**](EcommerceV1ProductProductResourcePriceRange.md) |  | [optional] 
**variants** | [**List[EcommerceV1ProductProductResourceVariantsInner]**](EcommerceV1ProductProductResourceVariantsInner.md) | Present (non-null) only when include&#x3D;variants is set; null otherwise. | [optional] 
**media** | [**List[EcommerceV1ProductProductResourceMediaInner]**](EcommerceV1ProductProductResourceMediaInner.md) | Present (non-null) only when include&#x3D;media is set; null otherwise. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_product_product_resource import EcommerceV1ProductProductResource

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ProductProductResource from a JSON string
ecommerce_v1_product_product_resource_instance = EcommerceV1ProductProductResource.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ProductProductResource.to_json())

# convert the object into a dict
ecommerce_v1_product_product_resource_dict = ecommerce_v1_product_product_resource_instance.to_dict()
# create an instance of EcommerceV1ProductProductResource from a dict
ecommerce_v1_product_product_resource_from_dict = EcommerceV1ProductProductResource.from_dict(ecommerce_v1_product_product_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


