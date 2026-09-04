# HostingV1NodeJsStoredBuildSettingsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_version** | **int** | Node.js major version used to build and run the application | 
**app_type** | **str** | Detected or chosen application framework | 
**root_directory** | **str** | Application root directory (where package.json is located) relative to public_html; null means public_html itself | 
**output_directory** | **str** | Build output directory relative to the root directory | 
**build_script** | **str** | The package.json script that builds the application | 
**entry_file** | **str** | The main entry point file for the application | 
**package_manager** | **str** | Package manager used to install dependencies | 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_stored_build_settings_resource import HostingV1NodeJsStoredBuildSettingsResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsStoredBuildSettingsResource from a JSON string
hosting_v1_node_js_stored_build_settings_resource_instance = HostingV1NodeJsStoredBuildSettingsResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsStoredBuildSettingsResource.to_json())

# convert the object into a dict
hosting_v1_node_js_stored_build_settings_resource_dict = hosting_v1_node_js_stored_build_settings_resource_instance.to_dict()
# create an instance of HostingV1NodeJsStoredBuildSettingsResource from a dict
hosting_v1_node_js_stored_build_settings_resource_from_dict = HostingV1NodeJsStoredBuildSettingsResource.from_dict(hosting_v1_node_js_stored_build_settings_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


