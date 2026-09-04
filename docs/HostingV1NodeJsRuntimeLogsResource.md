# HostingV1NodeJsRuntimeLogsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[HostingV1NodeJsLogEntryResource]**](HostingV1NodeJsLogEntryResource.md) | Array of [&#x60;Hosting.V1.NodeJs.LogEntryResource&#x60;](#model/hostingv1nodejslogentryresource) | 
**started_at** | **datetime** | Timestamp of the first line of the log file; null when the file is empty or its first line has no timestamp field | 
**total_lines** | **int** | Total number of lines in the raw log file. Send total_lines + 1 as from_line in the next poll to receive only new entries. | 
**last_deployed_at** | **datetime** | Time of the last completed build; entries before it belong to the previous deployment. null when no build has completed yet. | 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_runtime_logs_resource import HostingV1NodeJsRuntimeLogsResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsRuntimeLogsResource from a JSON string
hosting_v1_node_js_runtime_logs_resource_instance = HostingV1NodeJsRuntimeLogsResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsRuntimeLogsResource.to_json())

# convert the object into a dict
hosting_v1_node_js_runtime_logs_resource_dict = hosting_v1_node_js_runtime_logs_resource_instance.to_dict()
# create an instance of HostingV1NodeJsRuntimeLogsResource from a dict
hosting_v1_node_js_runtime_logs_resource_from_dict = HostingV1NodeJsRuntimeLogsResource.from_dict(hosting_v1_node_js_runtime_logs_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


