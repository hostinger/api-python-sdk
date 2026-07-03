# EcommerceV1SalesChannelSalesChannelListResourceSalesChannelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Sales channel ID | [optional] 
**type** | **str** | Sales channel type | [optional] 
**is_primary** | **bool** | Whether this is the primary sales channel. | [optional] 
**is_active** | **bool** | Whether the sales channel is active. | [optional] 
**external_id** | **str** | External identifier for the sales channel. | [optional] 
**name** | **str** | Merchant-facing custom name. | [optional] 
**domain** | **str** | Public address where the sales channel lives. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_sales_channel_sales_channel_list_resource_sales_channels_inner import EcommerceV1SalesChannelSalesChannelListResourceSalesChannelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1SalesChannelSalesChannelListResourceSalesChannelsInner from a JSON string
ecommerce_v1_sales_channel_sales_channel_list_resource_sales_channels_inner_instance = EcommerceV1SalesChannelSalesChannelListResourceSalesChannelsInner.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1SalesChannelSalesChannelListResourceSalesChannelsInner.to_json())

# convert the object into a dict
ecommerce_v1_sales_channel_sales_channel_list_resource_sales_channels_inner_dict = ecommerce_v1_sales_channel_sales_channel_list_resource_sales_channels_inner_instance.to_dict()
# create an instance of EcommerceV1SalesChannelSalesChannelListResourceSalesChannelsInner from a dict
ecommerce_v1_sales_channel_sales_channel_list_resource_sales_channels_inner_from_dict = EcommerceV1SalesChannelSalesChannelListResourceSalesChannelsInner.from_dict(ecommerce_v1_sales_channel_sales_channel_list_resource_sales_channels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


