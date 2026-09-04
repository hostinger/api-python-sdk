# HostingV1NodeJsUpdateBuildSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_version** | **int** | Node.js major version | 
**app_type** | **str** | Node.js application framework. Set it explicitly when auto-detection picked the wrong one. | [optional] 
**root_directory** | **str** | Application root directory (where package.json is located) relative to public_html. Omit it, or send \&quot;.\&quot;, for public_html itself. | [optional] 
**output_directory** | **str** | Build output directory relative to the root directory | [optional] 
**build_script** | **str** | The package.json script that builds the application | [optional] 
**entry_file** | **str** | The main entry point file for the application (required for express, fastify, nest, nuxt and hono app types) | [optional] 
**package_manager** | **str** | Package manager used to install dependencies | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_update_build_settings_request import HostingV1NodeJsUpdateBuildSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsUpdateBuildSettingsRequest from a JSON string
hosting_v1_node_js_update_build_settings_request_instance = HostingV1NodeJsUpdateBuildSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsUpdateBuildSettingsRequest.to_json())

# convert the object into a dict
hosting_v1_node_js_update_build_settings_request_dict = hosting_v1_node_js_update_build_settings_request_instance.to_dict()
# create an instance of HostingV1NodeJsUpdateBuildSettingsRequest from a dict
hosting_v1_node_js_update_build_settings_request_from_dict = HostingV1NodeJsUpdateBuildSettingsRequest.from_dict(hosting_v1_node_js_update_build_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


