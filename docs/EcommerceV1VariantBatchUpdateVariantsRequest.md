# EcommerceV1VariantBatchUpdateVariantsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variants** | [**List[EcommerceV1VariantBatchUpdateVariantsRequestVariantsInner]**](EcommerceV1VariantBatchUpdateVariantsRequestVariantsInner.md) | Variants to update in place by id, up to 100. Variants omitted from the list are left untouched. | 

## Example

```python
from hostinger_api.models.ecommerce_v1_variant_batch_update_variants_request import EcommerceV1VariantBatchUpdateVariantsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1VariantBatchUpdateVariantsRequest from a JSON string
ecommerce_v1_variant_batch_update_variants_request_instance = EcommerceV1VariantBatchUpdateVariantsRequest.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1VariantBatchUpdateVariantsRequest.to_json())

# convert the object into a dict
ecommerce_v1_variant_batch_update_variants_request_dict = ecommerce_v1_variant_batch_update_variants_request_instance.to_dict()
# create an instance of EcommerceV1VariantBatchUpdateVariantsRequest from a dict
ecommerce_v1_variant_batch_update_variants_request_from_dict = EcommerceV1VariantBatchUpdateVariantsRequest.from_dict(ecommerce_v1_variant_batch_update_variants_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


