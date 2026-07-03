# EcommerceV1SalesChannelStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Sales channel type. Only \&quot;custom\&quot; channels can be created via the API. | 
**name** | **str** | Merchant-facing custom name shown in the sales channels list. | 
**url** | **str** | Optional public address where the custom sales channel lives. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_sales_channel_store_request import EcommerceV1SalesChannelStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1SalesChannelStoreRequest from a JSON string
ecommerce_v1_sales_channel_store_request_instance = EcommerceV1SalesChannelStoreRequest.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1SalesChannelStoreRequest.to_json())

# convert the object into a dict
ecommerce_v1_sales_channel_store_request_dict = ecommerce_v1_sales_channel_store_request_instance.to_dict()
# create an instance of EcommerceV1SalesChannelStoreRequest from a dict
ecommerce_v1_sales_channel_store_request_from_dict = EcommerceV1SalesChannelStoreRequest.from_dict(ecommerce_v1_sales_channel_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


