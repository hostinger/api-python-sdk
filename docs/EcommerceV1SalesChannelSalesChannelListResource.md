# EcommerceV1SalesChannelSalesChannelListResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sales_channels** | [**List[EcommerceV1SalesChannelSalesChannelListResourceSalesChannelsInner]**](EcommerceV1SalesChannelSalesChannelListResourceSalesChannelsInner.md) | The store&#39;s active sales channels. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_sales_channel_sales_channel_list_resource import EcommerceV1SalesChannelSalesChannelListResource

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1SalesChannelSalesChannelListResource from a JSON string
ecommerce_v1_sales_channel_sales_channel_list_resource_instance = EcommerceV1SalesChannelSalesChannelListResource.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1SalesChannelSalesChannelListResource.to_json())

# convert the object into a dict
ecommerce_v1_sales_channel_sales_channel_list_resource_dict = ecommerce_v1_sales_channel_sales_channel_list_resource_instance.to_dict()
# create an instance of EcommerceV1SalesChannelSalesChannelListResource from a dict
ecommerce_v1_sales_channel_sales_channel_list_resource_from_dict = EcommerceV1SalesChannelSalesChannelListResource.from_dict(ecommerce_v1_sales_channel_sales_channel_list_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


