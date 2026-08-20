# EcommerceV1VariantCreateVariantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The variant title. Defaults to the option values joined with &#39; / &#39; (e.g. &#39;Red / L&#39;). | [optional] 
**sku** | **str** | The variant SKU. | [optional] 
**options** | [**List[EcommerceV1VariantCreateVariantRequestOptionsInner]**](EcommerceV1VariantCreateVariantRequestOptionsInner.md) | Option name/value pairs that distinguish this variant, e.g. [{name: Size, value: M}]. Options missing from the product are created; provide a value for every option the product already has. | 
**prices** | [**List[EcommerceV1VariantCreateVariantRequestPricesInner]**](EcommerceV1VariantCreateVariantRequestPricesInner.md) | Prices per currency. Amounts are integers in the smallest currency unit. A free item is amount: 0. | [optional] 
**inventory_quantity** | **int** | Units in stock. Defaults to 0. | [optional] 
**manage_inventory** | **bool** | Whether stock is tracked for this variant. Defaults to false. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_variant_create_variant_request import EcommerceV1VariantCreateVariantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1VariantCreateVariantRequest from a JSON string
ecommerce_v1_variant_create_variant_request_instance = EcommerceV1VariantCreateVariantRequest.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1VariantCreateVariantRequest.to_json())

# convert the object into a dict
ecommerce_v1_variant_create_variant_request_dict = ecommerce_v1_variant_create_variant_request_instance.to_dict()
# create an instance of EcommerceV1VariantCreateVariantRequest from a dict
ecommerce_v1_variant_create_variant_request_from_dict = EcommerceV1VariantCreateVariantRequest.from_dict(ecommerce_v1_variant_create_variant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


