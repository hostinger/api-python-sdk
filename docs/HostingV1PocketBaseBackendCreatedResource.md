# HostingV1PocketBaseBackendCreatedResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | PocketBase instance ID | 
**domain** | **str** | Website domain that serves the PocketBase API | 
**api_url** | **str** | Base URL of the PocketBase REST API | 
**admin_url** | **str** | URL of the PocketBase dashboard | 
**superuser_email** | **str** | Email of the superuser set up when the backend was created | 
**superuser_password** | **str** | Password of that superuser, generated when the request had none. Returned only here: Hostinger does not store it, so save it right away. | 
**state** | **str** | Live process state. The instance sleeps when idle and wakes on the first request. Usually null right after creation. | 
**version** | **str** | PocketBase version | 
**next_steps** | **List[str]** | What to do next with this backend | 

## Example

```python
from hostinger_api.models.hosting_v1_pocket_base_backend_created_resource import HostingV1PocketBaseBackendCreatedResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1PocketBaseBackendCreatedResource from a JSON string
hosting_v1_pocket_base_backend_created_resource_instance = HostingV1PocketBaseBackendCreatedResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1PocketBaseBackendCreatedResource.to_json())

# convert the object into a dict
hosting_v1_pocket_base_backend_created_resource_dict = hosting_v1_pocket_base_backend_created_resource_instance.to_dict()
# create an instance of HostingV1PocketBaseBackendCreatedResource from a dict
hosting_v1_pocket_base_backend_created_resource_from_dict = HostingV1PocketBaseBackendCreatedResource.from_dict(hosting_v1_pocket_base_backend_created_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


