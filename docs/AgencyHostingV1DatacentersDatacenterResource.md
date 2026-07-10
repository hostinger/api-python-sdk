# AgencyHostingV1DatacentersDatacenterResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Datacenter title | 
**code** | **str** | Datacenter code | 
**country** | **str** | Datacenter country code | 
**coordinates** | [**AgencyHostingV1DatacentersCoordinatesResource**](AgencyHostingV1DatacentersCoordinatesResource.md) |  | 
**pinger_url** | **str** | URL you can ping to measure round-trip latency to this datacenter. Compare the measured latency across datacenters to identify the nearest one (lowest ping) for your website. Null when no online server is currently available to measure against. | 

## Example

```python
from hostinger_api.models.agency_hosting_v1_datacenters_datacenter_resource import AgencyHostingV1DatacentersDatacenterResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1DatacentersDatacenterResource from a JSON string
agency_hosting_v1_datacenters_datacenter_resource_instance = AgencyHostingV1DatacentersDatacenterResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1DatacentersDatacenterResource.to_json())

# convert the object into a dict
agency_hosting_v1_datacenters_datacenter_resource_dict = agency_hosting_v1_datacenters_datacenter_resource_instance.to_dict()
# create an instance of AgencyHostingV1DatacentersDatacenterResource from a dict
agency_hosting_v1_datacenters_datacenter_resource_from_dict = AgencyHostingV1DatacentersDatacenterResource.from_dict(agency_hosting_v1_datacenters_datacenter_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


