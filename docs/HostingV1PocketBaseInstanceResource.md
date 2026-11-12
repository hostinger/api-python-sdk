# HostingV1PocketBaseInstanceResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | PocketBase instance ID | 
**domain** | **str** | Website domain that serves the PocketBase API | 
**api_url** | **str** | Base URL of the PocketBase REST API | 
**admin_url** | **str** | URL of the PocketBase dashboard | 
**state** | **str** | Live process state. The instance sleeps when idle and wakes on the first request. Null when the server could not be reached. | 
**version** | **str** | PocketBase version | 
**disk_usage_kb** | **int** | Disk space used by the instance data, in KB | 

## Example

```python
from hostinger_api.models.hosting_v1_pocket_base_instance_resource import HostingV1PocketBaseInstanceResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1PocketBaseInstanceResource from a JSON string
hosting_v1_pocket_base_instance_resource_instance = HostingV1PocketBaseInstanceResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1PocketBaseInstanceResource.to_json())

# convert the object into a dict
hosting_v1_pocket_base_instance_resource_dict = hosting_v1_pocket_base_instance_resource_instance.to_dict()
# create an instance of HostingV1PocketBaseInstanceResource from a dict
hosting_v1_pocket_base_instance_resource_from_dict = HostingV1PocketBaseInstanceResource.from_dict(hosting_v1_pocket_base_instance_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


