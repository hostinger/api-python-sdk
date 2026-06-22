# HostingV1DatacenterDatacenterResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Data center title | [optional] 
**code** | **str** | Data center code | [optional] 
**coordinates** | [**HostingV1DatacenterCoordinatesResource**](HostingV1DatacenterCoordinatesResource.md) |  | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_datacenter_datacenter_resource import HostingV1DatacenterDatacenterResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1DatacenterDatacenterResource from a JSON string
hosting_v1_datacenter_datacenter_resource_instance = HostingV1DatacenterDatacenterResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1DatacenterDatacenterResource.to_json())

# convert the object into a dict
hosting_v1_datacenter_datacenter_resource_dict = hosting_v1_datacenter_datacenter_resource_instance.to_dict()
# create an instance of HostingV1DatacenterDatacenterResource from a dict
hosting_v1_datacenter_datacenter_resource_from_dict = HostingV1DatacenterDatacenterResource.from_dict(hosting_v1_datacenter_datacenter_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


