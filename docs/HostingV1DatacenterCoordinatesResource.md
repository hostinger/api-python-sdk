# HostingV1DatacenterCoordinatesResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude coordinate | [optional] 
**longitude** | **float** | Longitude coordinate | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_datacenter_coordinates_resource import HostingV1DatacenterCoordinatesResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1DatacenterCoordinatesResource from a JSON string
hosting_v1_datacenter_coordinates_resource_instance = HostingV1DatacenterCoordinatesResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1DatacenterCoordinatesResource.to_json())

# convert the object into a dict
hosting_v1_datacenter_coordinates_resource_dict = hosting_v1_datacenter_coordinates_resource_instance.to_dict()
# create an instance of HostingV1DatacenterCoordinatesResource from a dict
hosting_v1_datacenter_coordinates_resource_from_dict = HostingV1DatacenterCoordinatesResource.from_dict(hosting_v1_datacenter_coordinates_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


