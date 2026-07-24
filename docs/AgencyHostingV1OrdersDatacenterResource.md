# AgencyHostingV1OrdersDatacenterResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Datacenter code | [optional] 
**country** | **str** | Datacenter country | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_orders_datacenter_resource import AgencyHostingV1OrdersDatacenterResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1OrdersDatacenterResource from a JSON string
agency_hosting_v1_orders_datacenter_resource_instance = AgencyHostingV1OrdersDatacenterResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1OrdersDatacenterResource.to_json())

# convert the object into a dict
agency_hosting_v1_orders_datacenter_resource_dict = agency_hosting_v1_orders_datacenter_resource_instance.to_dict()
# create an instance of AgencyHostingV1OrdersDatacenterResource from a dict
agency_hosting_v1_orders_datacenter_resource_from_dict = AgencyHostingV1OrdersDatacenterResource.from_dict(agency_hosting_v1_orders_datacenter_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


