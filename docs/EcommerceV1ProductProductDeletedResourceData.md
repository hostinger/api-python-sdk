# EcommerceV1ProductProductDeletedResourceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the product. | [optional] 
**is_deleted** | **bool** | True when the product was deleted. | [optional] 
**is_archived** | **bool** | True when the product was archived instead of deleted (a subscription product with active subscribers). | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_product_product_deleted_resource_data import EcommerceV1ProductProductDeletedResourceData

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ProductProductDeletedResourceData from a JSON string
ecommerce_v1_product_product_deleted_resource_data_instance = EcommerceV1ProductProductDeletedResourceData.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ProductProductDeletedResourceData.to_json())

# convert the object into a dict
ecommerce_v1_product_product_deleted_resource_data_dict = ecommerce_v1_product_product_deleted_resource_data_instance.to_dict()
# create an instance of EcommerceV1ProductProductDeletedResourceData from a dict
ecommerce_v1_product_product_deleted_resource_data_from_dict = EcommerceV1ProductProductDeletedResourceData.from_dict(ecommerce_v1_product_product_deleted_resource_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


