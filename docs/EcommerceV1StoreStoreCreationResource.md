# EcommerceV1StoreStoreCreationResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store** | [**EcommerceV1StoreStoreCreationResourceStore**](EcommerceV1StoreStoreCreationResourceStore.md) |  | [optional] 
**sales_channel** | [**EcommerceV1StoreStoreCreationResourceSalesChannel**](EcommerceV1StoreStoreCreationResourceSalesChannel.md) |  | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_store_store_creation_resource import EcommerceV1StoreStoreCreationResource

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1StoreStoreCreationResource from a JSON string
ecommerce_v1_store_store_creation_resource_instance = EcommerceV1StoreStoreCreationResource.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1StoreStoreCreationResource.to_json())

# convert the object into a dict
ecommerce_v1_store_store_creation_resource_dict = ecommerce_v1_store_store_creation_resource_instance.to_dict()
# create an instance of EcommerceV1StoreStoreCreationResource from a dict
ecommerce_v1_store_store_creation_resource_from_dict = EcommerceV1StoreStoreCreationResource.from_dict(ecommerce_v1_store_store_creation_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


