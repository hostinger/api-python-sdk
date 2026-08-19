# HostingV1NodeJsGetBuildSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_path** | **str** | The path to the archive file relative to the document root of the vhost | 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_get_build_settings_request import HostingV1NodeJsGetBuildSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsGetBuildSettingsRequest from a JSON string
hosting_v1_node_js_get_build_settings_request_instance = HostingV1NodeJsGetBuildSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsGetBuildSettingsRequest.to_json())

# convert the object into a dict
hosting_v1_node_js_get_build_settings_request_dict = hosting_v1_node_js_get_build_settings_request_instance.to_dict()
# create an instance of HostingV1NodeJsGetBuildSettingsRequest from a dict
hosting_v1_node_js_get_build_settings_request_from_dict = HostingV1NodeJsGetBuildSettingsRequest.from_dict(hosting_v1_node_js_get_build_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


