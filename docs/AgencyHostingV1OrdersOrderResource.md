# AgencyHostingV1OrdersOrderResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Order ID | [optional] 
**client_id** | **int** | Order client ID | [optional] 
**status** | **str** | Order status | [optional] 
**plan** | [**AgencyHostingV1OrdersPlanResource**](AgencyHostingV1OrdersPlanResource.md) |  | [optional] 
**datacenter** | [**AgencyHostingV1OrdersDatacenterResource**](AgencyHostingV1OrdersDatacenterResource.md) |  | [optional] 
**created_at** | **datetime** | Order creation date | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_orders_order_resource import AgencyHostingV1OrdersOrderResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1OrdersOrderResource from a JSON string
agency_hosting_v1_orders_order_resource_instance = AgencyHostingV1OrdersOrderResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1OrdersOrderResource.to_json())

# convert the object into a dict
agency_hosting_v1_orders_order_resource_dict = agency_hosting_v1_orders_order_resource_instance.to_dict()
# create an instance of AgencyHostingV1OrdersOrderResource from a dict
agency_hosting_v1_orders_order_resource_from_dict = AgencyHostingV1OrdersOrderResource.from_dict(agency_hosting_v1_orders_order_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


