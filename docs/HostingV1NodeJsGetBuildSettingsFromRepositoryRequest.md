# HostingV1NodeJsGetBuildSettingsFromRepositoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | **str** | Repository owner login, as returned by &#x60;List Git installation repositories&#x60;. GitLab group paths use slashes. | 
**repository** | **str** | Repository name without the .git suffix | 
**branch** | **str** | Branch whose package.json is inspected | 
**installation_uuid** | **str** | Git installation used to access the repository, taken from &#x60;List Git installations&#x60; | 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_get_build_settings_from_repository_request import HostingV1NodeJsGetBuildSettingsFromRepositoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsGetBuildSettingsFromRepositoryRequest from a JSON string
hosting_v1_node_js_get_build_settings_from_repository_request_instance = HostingV1NodeJsGetBuildSettingsFromRepositoryRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsGetBuildSettingsFromRepositoryRequest.to_json())

# convert the object into a dict
hosting_v1_node_js_get_build_settings_from_repository_request_dict = hosting_v1_node_js_get_build_settings_from_repository_request_instance.to_dict()
# create an instance of HostingV1NodeJsGetBuildSettingsFromRepositoryRequest from a dict
hosting_v1_node_js_get_build_settings_from_repository_request_from_dict = HostingV1NodeJsGetBuildSettingsFromRepositoryRequest.from_dict(hosting_v1_node_js_get_build_settings_from_repository_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


