# EcommerceV1VariantCreateVariantRequestOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Option name, e.g. Size. | 
**value** | **str** | Option value for this variant, e.g. M. | 

## Example

```python
from hostinger_api.models.ecommerce_v1_variant_create_variant_request_options_inner import EcommerceV1VariantCreateVariantRequestOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1VariantCreateVariantRequestOptionsInner from a JSON string
ecommerce_v1_variant_create_variant_request_options_inner_instance = EcommerceV1VariantCreateVariantRequestOptionsInner.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1VariantCreateVariantRequestOptionsInner.to_json())

# convert the object into a dict
ecommerce_v1_variant_create_variant_request_options_inner_dict = ecommerce_v1_variant_create_variant_request_options_inner_instance.to_dict()
# create an instance of EcommerceV1VariantCreateVariantRequestOptionsInner from a dict
ecommerce_v1_variant_create_variant_request_options_inner_from_dict = EcommerceV1VariantCreateVariantRequestOptionsInner.from_dict(ecommerce_v1_variant_create_variant_request_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


