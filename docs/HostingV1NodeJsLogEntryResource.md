# HostingV1NodeJsLogEntryResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** | ISO 8601 timestamp of the log entry | 
**level** | **str** | Log level in upper case (usually ERROR, WARN, INFO, LOG, DEBUG or TRACE). Numeric pino levels are mapped to these names. | 
**message** | **str** | Log message | 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_log_entry_resource import HostingV1NodeJsLogEntryResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsLogEntryResource from a JSON string
hosting_v1_node_js_log_entry_resource_instance = HostingV1NodeJsLogEntryResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsLogEntryResource.to_json())

# convert the object into a dict
hosting_v1_node_js_log_entry_resource_dict = hosting_v1_node_js_log_entry_resource_instance.to_dict()
# create an instance of HostingV1NodeJsLogEntryResource from a dict
hosting_v1_node_js_log_entry_resource_from_dict = HostingV1NodeJsLogEntryResource.from_dict(hosting_v1_node_js_log_entry_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


