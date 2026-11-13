# HostingV1PocketBaseBackendResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | PocketBase instance ID | 
**domain** | **str** | Website domain that serves the PocketBase API | 
**api_url** | **str** | Base URL of the PocketBase REST API | 
**admin_url** | **str** | URL of the PocketBase dashboard | 
**state** | **str** | Live process state. The instance sleeps when idle and wakes on the first request. Null when the server could not be reached. | 
**failure_reason** | **str** | Why the last start did not succeed, set only while &#x60;state&#x60; is &#x60;failed&#x60;. &#x60;process_limit&#x60; means the hosting account has no free process slots, usually because its Node.js apps are running; &#x60;start_failed&#x60; is any other cause. | 
**retry_after_seconds** | **int** | Seconds until Hostinger tries to start the instance again, set only while &#x60;state&#x60; is &#x60;failed&#x60;. Null when the next try is due now. | 
**version** | **str** | PocketBase version | 
**next_steps** | **List[str]** | What to do next with this backend | 

## Example

```python
from hostinger_api.models.hosting_v1_pocket_base_backend_resource import HostingV1PocketBaseBackendResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1PocketBaseBackendResource from a JSON string
hosting_v1_pocket_base_backend_resource_instance = HostingV1PocketBaseBackendResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1PocketBaseBackendResource.to_json())

# convert the object into a dict
hosting_v1_pocket_base_backend_resource_dict = hosting_v1_pocket_base_backend_resource_instance.to_dict()
# create an instance of HostingV1PocketBaseBackendResource from a dict
hosting_v1_pocket_base_backend_resource_from_dict = HostingV1PocketBaseBackendResource.from_dict(hosting_v1_pocket_base_backend_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


