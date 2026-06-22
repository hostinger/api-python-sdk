# HostingV1NodeJsBuildOptionsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_version** | **int** | Node.js version | 
**app_type** | **str** | Node.js application type | 
**root_directory** | **str** | Application root directory | 
**output_directory** | **str** | Build output directory | 
**build_script** | **str** | The npm script to run to build the application | 
**entry_file** | **str** | The main entry point file for the application | 
**package_manager** | **str** | Package manager | 
**source_type** | **str** | Source type for the build | 
**source_options** | [**HostingV1NodeJsSourceOptionsResource**](HostingV1NodeJsSourceOptionsResource.md) |  | 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_build_options_resource import HostingV1NodeJsBuildOptionsResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsBuildOptionsResource from a JSON string
hosting_v1_node_js_build_options_resource_instance = HostingV1NodeJsBuildOptionsResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsBuildOptionsResource.to_json())

# convert the object into a dict
hosting_v1_node_js_build_options_resource_dict = hosting_v1_node_js_build_options_resource_instance.to_dict()
# create an instance of HostingV1NodeJsBuildOptionsResource from a dict
hosting_v1_node_js_build_options_resource_from_dict = HostingV1NodeJsBuildOptionsResource.from_dict(hosting_v1_node_js_build_options_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


