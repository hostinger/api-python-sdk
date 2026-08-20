# EcommerceV1VariantBatchUpdateVariantsRequestVariantsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant_id** | **str** | The id of the variant to update. | 
**title** | **str** | The variant title. | [optional] 
**inventory_quantity** | **int** | Units in stock. | [optional] 
**manage_inventory** | **bool** | Whether stock is tracked for this variant. | [optional] 
**prices** | [**List[EcommerceV1VariantBatchUpdateVariantsRequestVariantsInnerPricesInner]**](EcommerceV1VariantBatchUpdateVariantsRequestVariantsInnerPricesInner.md) | The full list of prices for the variant, replacing the existing ones. A free item is amount: 0. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_variant_batch_update_variants_request_variants_inner import EcommerceV1VariantBatchUpdateVariantsRequestVariantsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1VariantBatchUpdateVariantsRequestVariantsInner from a JSON string
ecommerce_v1_variant_batch_update_variants_request_variants_inner_instance = EcommerceV1VariantBatchUpdateVariantsRequestVariantsInner.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1VariantBatchUpdateVariantsRequestVariantsInner.to_json())

# convert the object into a dict
ecommerce_v1_variant_batch_update_variants_request_variants_inner_dict = ecommerce_v1_variant_batch_update_variants_request_variants_inner_instance.to_dict()
# create an instance of EcommerceV1VariantBatchUpdateVariantsRequestVariantsInner from a dict
ecommerce_v1_variant_batch_update_variants_request_variants_inner_from_dict = EcommerceV1VariantBatchUpdateVariantsRequestVariantsInner.from_dict(ecommerce_v1_variant_batch_update_variants_request_variants_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


