# EcommerceV1VariantVariantResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The variant ID, required by every other variant endpoint. | [optional] 
**title** | **str** | The variant title, or null. | [optional] 
**sku** | **str** | The variant SKU, or null. | [optional] 
**options** | [**List[EcommerceV1VariantVariantResourceOptionsInner]**](EcommerceV1VariantVariantResourceOptionsInner.md) | The variant&#39;s option values. | [optional] 
**prices** | [**List[EcommerceV1ProductProductResourceVariantsInnerPricesInner]**](EcommerceV1ProductProductResourceVariantsInnerPricesInner.md) | Prices per currency, in the smallest currency unit. | [optional] 
**inventory_quantity** | **int** | Units in stock. | [optional] 
**manage_inventory** | **bool** | Whether stock is tracked for this variant. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_variant_variant_resource import EcommerceV1VariantVariantResource

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1VariantVariantResource from a JSON string
ecommerce_v1_variant_variant_resource_instance = EcommerceV1VariantVariantResource.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1VariantVariantResource.to_json())

# convert the object into a dict
ecommerce_v1_variant_variant_resource_dict = ecommerce_v1_variant_variant_resource_instance.to_dict()
# create an instance of EcommerceV1VariantVariantResource from a dict
ecommerce_v1_variant_variant_resource_from_dict = EcommerceV1VariantVariantResource.from_dict(ecommerce_v1_variant_variant_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


