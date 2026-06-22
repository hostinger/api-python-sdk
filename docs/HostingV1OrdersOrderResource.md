# HostingV1OrdersOrderResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Order ID | [optional] 
**client_id** | **int** | Client ID | [optional] 
**subscription_id** | **str** | Subscription ID | [optional] 
**created_at** | **datetime** | Creation date | [optional] 
**plan** | [**HostingV1OrdersPlanResource**](HostingV1OrdersPlanResource.md) |  | [optional] 
**status** | **str** | Order status | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_orders_order_resource import HostingV1OrdersOrderResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1OrdersOrderResource from a JSON string
hosting_v1_orders_order_resource_instance = HostingV1OrdersOrderResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1OrdersOrderResource.to_json())

# convert the object into a dict
hosting_v1_orders_order_resource_dict = hosting_v1_orders_order_resource_instance.to_dict()
# create an instance of HostingV1OrdersOrderResource from a dict
hosting_v1_orders_order_resource_from_dict = HostingV1OrdersOrderResource.from_dict(hosting_v1_orders_order_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


