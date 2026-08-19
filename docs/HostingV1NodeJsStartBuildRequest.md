# HostingV1NodeJsStartBuildRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_version** | **int** | Node.js version | 
**app_type** | **str** | Node.js application type | 
**root_directory** | **str** | Application root directory (where package.json is located) relative to public_html | 
**output_directory** | **str** | Build output directory relative to the root directory | 
**build_script** | **str** | Build script that will be ran to build the application | 
**entry_file** | **str** | The main entry point file for the application | [optional] 
**package_manager** | **str** | Package manager | [optional] 
**source_type** | **str** | The source type of the files | 
**source_options** | [**HostingV1NodeJsStartBuildRequestSourceOptions**](HostingV1NodeJsStartBuildRequestSourceOptions.md) |  | 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_start_build_request import HostingV1NodeJsStartBuildRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsStartBuildRequest from a JSON string
hosting_v1_node_js_start_build_request_instance = HostingV1NodeJsStartBuildRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsStartBuildRequest.to_json())

# convert the object into a dict
hosting_v1_node_js_start_build_request_dict = hosting_v1_node_js_start_build_request_instance.to_dict()
# create an instance of HostingV1NodeJsStartBuildRequest from a dict
hosting_v1_node_js_start_build_request_from_dict = HostingV1NodeJsStartBuildRequest.from_dict(hosting_v1_node_js_start_build_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


