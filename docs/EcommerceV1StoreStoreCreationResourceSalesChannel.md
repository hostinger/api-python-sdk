# EcommerceV1StoreStoreCreationResourceSalesChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Sales channel ID | [optional] 
**type** | **str** | Sales channel type | [optional] 
**external_id** | **str** | External identifier for the sales channel | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_store_store_creation_resource_sales_channel import EcommerceV1StoreStoreCreationResourceSalesChannel

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1StoreStoreCreationResourceSalesChannel from a JSON string
ecommerce_v1_store_store_creation_resource_sales_channel_instance = EcommerceV1StoreStoreCreationResourceSalesChannel.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1StoreStoreCreationResourceSalesChannel.to_json())

# convert the object into a dict
ecommerce_v1_store_store_creation_resource_sales_channel_dict = ecommerce_v1_store_store_creation_resource_sales_channel_instance.to_dict()
# create an instance of EcommerceV1StoreStoreCreationResourceSalesChannel from a dict
ecommerce_v1_store_store_creation_resource_sales_channel_from_dict = EcommerceV1StoreStoreCreationResourceSalesChannel.from_dict(ecommerce_v1_store_store_creation_resource_sales_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


