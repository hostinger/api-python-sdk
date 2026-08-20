# EcommerceV1VariantVariantListResponseResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EcommerceV1VariantVariantResource]**](EcommerceV1VariantVariantResource.md) | The variants. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_variant_variant_list_response_resource import EcommerceV1VariantVariantListResponseResource

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1VariantVariantListResponseResource from a JSON string
ecommerce_v1_variant_variant_list_response_resource_instance = EcommerceV1VariantVariantListResponseResource.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1VariantVariantListResponseResource.to_json())

# convert the object into a dict
ecommerce_v1_variant_variant_list_response_resource_dict = ecommerce_v1_variant_variant_list_response_resource_instance.to_dict()
# create an instance of EcommerceV1VariantVariantListResponseResource from a dict
ecommerce_v1_variant_variant_list_response_resource_from_dict = EcommerceV1VariantVariantListResponseResource.from_dict(ecommerce_v1_variant_variant_list_response_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


