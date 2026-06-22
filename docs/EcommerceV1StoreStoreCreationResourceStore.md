# EcommerceV1StoreStoreCreationResourceStore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Store ID | [optional] 
**name** | **str** | Store name | [optional] 
**company_name** | **str** | Company name | [optional] 
**h_panel_id** | **str** | Identifier of the hPanel account that owns the store. | [optional] 
**created_at** | **datetime** | Creation date | [optional] 
**default_currency_code** | **str** | Default currency code (ISO 4217), in lowercase. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_store_store_creation_resource_store import EcommerceV1StoreStoreCreationResourceStore

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1StoreStoreCreationResourceStore from a JSON string
ecommerce_v1_store_store_creation_resource_store_instance = EcommerceV1StoreStoreCreationResourceStore.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1StoreStoreCreationResourceStore.to_json())

# convert the object into a dict
ecommerce_v1_store_store_creation_resource_store_dict = ecommerce_v1_store_store_creation_resource_store_instance.to_dict()
# create an instance of EcommerceV1StoreStoreCreationResourceStore from a dict
ecommerce_v1_store_store_creation_resource_store_from_dict = EcommerceV1StoreStoreCreationResourceStore.from_dict(ecommerce_v1_store_store_creation_resource_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


