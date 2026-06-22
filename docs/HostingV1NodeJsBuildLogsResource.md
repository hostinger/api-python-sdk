# HostingV1NodeJsBuildLogsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | **str** | Logs from the build process, may contain ANSI escape sequences (for colors, etc.) | 
**lines** | **int** | Number of log lines returned | 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_build_logs_resource import HostingV1NodeJsBuildLogsResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsBuildLogsResource from a JSON string
hosting_v1_node_js_build_logs_resource_instance = HostingV1NodeJsBuildLogsResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsBuildLogsResource.to_json())

# convert the object into a dict
hosting_v1_node_js_build_logs_resource_dict = hosting_v1_node_js_build_logs_resource_instance.to_dict()
# create an instance of HostingV1NodeJsBuildLogsResource from a dict
hosting_v1_node_js_build_logs_resource_from_dict = HostingV1NodeJsBuildLogsResource.from_dict(hosting_v1_node_js_build_logs_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


