# HostingV1FilesFileContentResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | File path, relative to the document root. | 
**content** | **str** | File content for the requested line range. | 
**from_line** | **int** | Line offset the returned content starts from. | 
**total_lines** | **int** | Total number of lines in the file. | 
**size_bytes** | **int** | Total file size in bytes. | 

## Example

```python
from hostinger_api.models.hosting_v1_files_file_content_resource import HostingV1FilesFileContentResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1FilesFileContentResource from a JSON string
hosting_v1_files_file_content_resource_instance = HostingV1FilesFileContentResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1FilesFileContentResource.to_json())

# convert the object into a dict
hosting_v1_files_file_content_resource_dict = hosting_v1_files_file_content_resource_instance.to_dict()
# create an instance of HostingV1FilesFileContentResource from a dict
hosting_v1_files_file_content_resource_from_dict = HostingV1FilesFileContentResource.from_dict(hosting_v1_files_file_content_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


