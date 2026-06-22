# EcommerceV1StoreStoreRequestSalesChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Sales channel type. Only \&quot;custom\&quot; channels can be created via the API. | [optional] 
**external_id** | **str** | External identifier for the sales channel. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_store_store_request_sales_channel import EcommerceV1StoreStoreRequestSalesChannel

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1StoreStoreRequestSalesChannel from a JSON string
ecommerce_v1_store_store_request_sales_channel_instance = EcommerceV1StoreStoreRequestSalesChannel.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1StoreStoreRequestSalesChannel.to_json())

# convert the object into a dict
ecommerce_v1_store_store_request_sales_channel_dict = ecommerce_v1_store_store_request_sales_channel_instance.to_dict()
# create an instance of EcommerceV1StoreStoreRequestSalesChannel from a dict
ecommerce_v1_store_store_request_sales_channel_from_dict = EcommerceV1StoreStoreRequestSalesChannel.from_dict(ecommerce_v1_store_store_request_sales_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


