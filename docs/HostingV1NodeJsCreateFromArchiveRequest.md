# HostingV1NodeJsCreateFromArchiveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive** | **str** | Project archive file (.zip, .tar.gz, or .tgz), maximum 50MB | 
**node_version** | **int** | Node.js version override (auto-detected from package.json if omitted) | [optional] 
**app_type** | **str** | Node.js application type override | [optional] 
**root_directory** | **str** | Application root directory override (where package.json is located) relative to public_html | [optional] 
**output_directory** | **str** | Build output directory override relative to the root directory | [optional] 
**build_script** | **str** | Build script override | [optional] 
**entry_file** | **str** | Main entry point file override | [optional] 
**package_manager** | **str** | Package manager override | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_node_js_create_from_archive_request import HostingV1NodeJsCreateFromArchiveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1NodeJsCreateFromArchiveRequest from a JSON string
hosting_v1_node_js_create_from_archive_request_instance = HostingV1NodeJsCreateFromArchiveRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1NodeJsCreateFromArchiveRequest.to_json())

# convert the object into a dict
hosting_v1_node_js_create_from_archive_request_dict = hosting_v1_node_js_create_from_archive_request_instance.to_dict()
# create an instance of HostingV1NodeJsCreateFromArchiveRequest from a dict
hosting_v1_node_js_create_from_archive_request_from_dict = HostingV1NodeJsCreateFromArchiveRequest.from_dict(hosting_v1_node_js_create_from_archive_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


