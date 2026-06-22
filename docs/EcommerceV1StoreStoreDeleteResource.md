# EcommerceV1StoreStoreDeleteResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the deleted store. | [optional] 
**is_deleted** | **bool** | Always true when the store was soft-deleted. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_store_store_delete_resource import EcommerceV1StoreStoreDeleteResource

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1StoreStoreDeleteResource from a JSON string
ecommerce_v1_store_store_delete_resource_instance = EcommerceV1StoreStoreDeleteResource.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1StoreStoreDeleteResource.to_json())

# convert the object into a dict
ecommerce_v1_store_store_delete_resource_dict = ecommerce_v1_store_store_delete_resource_instance.to_dict()
# create an instance of EcommerceV1StoreStoreDeleteResource from a dict
ecommerce_v1_store_store_delete_resource_from_dict = EcommerceV1StoreStoreDeleteResource.from_dict(ecommerce_v1_store_store_delete_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


