# EcommerceV1StoreStoreResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Store ID | [optional] 
**name** | **str** | Store name | [optional] 
**created_at** | **datetime** | Creation date | [optional] 
**updated_at** | **datetime** | Last update date | [optional] 
**version** | **str** | Store platform version identifier (e.g. \&quot;v2_standalone\&quot;). | [optional] 
**company_name** | **str** | Company name | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_store_store_resource import EcommerceV1StoreStoreResource

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1StoreStoreResource from a JSON string
ecommerce_v1_store_store_resource_instance = EcommerceV1StoreStoreResource.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1StoreStoreResource.to_json())

# convert the object into a dict
ecommerce_v1_store_store_resource_dict = ecommerce_v1_store_store_resource_instance.to_dict()
# create an instance of EcommerceV1StoreStoreResource from a dict
ecommerce_v1_store_store_resource_from_dict = EcommerceV1StoreStoreResource.from_dict(ecommerce_v1_store_store_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


