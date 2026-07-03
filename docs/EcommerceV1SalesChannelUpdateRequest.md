# EcommerceV1SalesChannelUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Merchant-facing custom name shown in the sales channels list. Pass null to clear it. | [optional] 
**url** | **str** | Public address where the custom sales channel lives. Pass null to clear it. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_sales_channel_update_request import EcommerceV1SalesChannelUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1SalesChannelUpdateRequest from a JSON string
ecommerce_v1_sales_channel_update_request_instance = EcommerceV1SalesChannelUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1SalesChannelUpdateRequest.to_json())

# convert the object into a dict
ecommerce_v1_sales_channel_update_request_dict = ecommerce_v1_sales_channel_update_request_instance.to_dict()
# create an instance of EcommerceV1SalesChannelUpdateRequest from a dict
ecommerce_v1_sales_channel_update_request_from_dict = EcommerceV1SalesChannelUpdateRequest.from_dict(ecommerce_v1_sales_channel_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


