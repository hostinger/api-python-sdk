# EcommerceV1ProductProductResourceVariantsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The variant ID. | [optional] 
**title** | **str** | The variant title. | [optional] 
**sku** | **str** | The variant SKU. | [optional] 
**options** | [**List[EcommerceV1ProductProductResourceVariantsInnerOptionsInner]**](EcommerceV1ProductProductResourceVariantsInnerOptionsInner.md) | The variant&#39;s option values. | [optional] 
**prices** | [**List[EcommerceV1ProductProductResourceVariantsInnerPricesInner]**](EcommerceV1ProductProductResourceVariantsInnerPricesInner.md) | Prices per currency, in the smallest currency unit. | [optional] 
**inventory_quantity** | **int** | Units in stock. | [optional] 
**manage_inventory** | **bool** | Whether stock is tracked for this variant. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_product_product_resource_variants_inner import EcommerceV1ProductProductResourceVariantsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ProductProductResourceVariantsInner from a JSON string
ecommerce_v1_product_product_resource_variants_inner_instance = EcommerceV1ProductProductResourceVariantsInner.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ProductProductResourceVariantsInner.to_json())

# convert the object into a dict
ecommerce_v1_product_product_resource_variants_inner_dict = ecommerce_v1_product_product_resource_variants_inner_instance.to_dict()
# create an instance of EcommerceV1ProductProductResourceVariantsInner from a dict
ecommerce_v1_product_product_resource_variants_inner_from_dict = EcommerceV1ProductProductResourceVariantsInner.from_dict(ecommerce_v1_product_product_resource_variants_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


