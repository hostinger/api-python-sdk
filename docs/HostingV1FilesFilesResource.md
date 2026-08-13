# HostingV1FilesFilesResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Listed directory, relative to the document root. | 
**items** | [**List[HostingV1FilesFilesResourceItemsInner]**](HostingV1FilesFilesResourceItemsInner.md) | Entries found in the listed directory. | 
**total_items** | **int** | Total number of entries matching the listing, across all pages. | 
**total_items_current_page** | **int** | Number of entries in this page. | 
**offset** | **int** | Number of entries skipped before this page. | 

## Example

```python
from hostinger_api.models.hosting_v1_files_files_resource import HostingV1FilesFilesResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1FilesFilesResource from a JSON string
hosting_v1_files_files_resource_instance = HostingV1FilesFilesResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1FilesFilesResource.to_json())

# convert the object into a dict
hosting_v1_files_files_resource_dict = hosting_v1_files_files_resource_instance.to_dict()
# create an instance of HostingV1FilesFilesResource from a dict
hosting_v1_files_files_resource_from_dict = HostingV1FilesFilesResource.from_dict(hosting_v1_files_files_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


