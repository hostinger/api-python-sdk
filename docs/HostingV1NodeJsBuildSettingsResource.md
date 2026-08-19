# HostingV1NodeJsBuildSettingsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_type** | **str** | Node.js application type | 
**node_version** | **int** | Node.js version | 
**root_directory** | **str** | Application root directory | 
**output_directory** | **str** | Build output directory | 
**build_script** | **str** | The npm script to run to build the application | 
**entry_file** | **str** | The main entry point file for the application | 
**package_manager** | **str** | Package manager | 
**available_scripts** | **List[str]** | The scripts configured in the package.json file | 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_build_settings_resource import HostingV1NodeJsBuildSettingsResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsBuildSettingsResource from a JSON string
hosting_v1_node_js_build_settings_resource_instance = HostingV1NodeJsBuildSettingsResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsBuildSettingsResource.to_json())

# convert the object into a dict
hosting_v1_node_js_build_settings_resource_dict = hosting_v1_node_js_build_settings_resource_instance.to_dict()
# create an instance of HostingV1NodeJsBuildSettingsResource from a dict
hosting_v1_node_js_build_settings_resource_from_dict = HostingV1NodeJsBuildSettingsResource.from_dict(hosting_v1_node_js_build_settings_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


