# HostingV1FilesFilesResourceItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Entry name. | 
**path** | **str** | Entry path, relative to the document root. | 
**type** | **str** | Entry type. | 
**size_bytes** | **int** | Entry size in bytes. Null for directories, symlinks, and other non-file entries. | 

## Example

```python
from hostinger_api.models.hosting_v1_files_files_resource_items_inner import HostingV1FilesFilesResourceItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1FilesFilesResourceItemsInner from a JSON string
hosting_v1_files_files_resource_items_inner_instance = HostingV1FilesFilesResourceItemsInner.from_json(json)
# print the JSON string representation of the object
print(HostingV1FilesFilesResourceItemsInner.to_json())

# convert the object into a dict
hosting_v1_files_files_resource_items_inner_dict = hosting_v1_files_files_resource_items_inner_instance.to_dict()
# create an instance of HostingV1FilesFilesResourceItemsInner from a dict
hosting_v1_files_files_resource_items_inner_from_dict = HostingV1FilesFilesResourceItemsInner.from_dict(hosting_v1_files_files_resource_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


