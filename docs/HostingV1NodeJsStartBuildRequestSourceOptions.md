# HostingV1NodeJsStartBuildRequestSourceOptions

Source-specific options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_path** | **str** | The path to the archive file relative to the document root of the vhost (required if source is \&quot;archive\&quot;) | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_start_build_request_source_options import HostingV1NodeJsStartBuildRequestSourceOptions

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsStartBuildRequestSourceOptions from a JSON string
hosting_v1_node_js_start_build_request_source_options_instance = HostingV1NodeJsStartBuildRequestSourceOptions.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsStartBuildRequestSourceOptions.to_json())

# convert the object into a dict
hosting_v1_node_js_start_build_request_source_options_dict = hosting_v1_node_js_start_build_request_source_options_instance.to_dict()
# create an instance of HostingV1NodeJsStartBuildRequestSourceOptions from a dict
hosting_v1_node_js_start_build_request_source_options_from_dict = HostingV1NodeJsStartBuildRequestSourceOptions.from_dict(hosting_v1_node_js_start_build_request_source_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


