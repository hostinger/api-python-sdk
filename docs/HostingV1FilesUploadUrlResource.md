# HostingV1FilesUploadUrlResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The TUS upload endpoint URL to send upload requests to | 
**auth_key** | **str** | Authentication token to pass as the &#x60;X-Auth&#x60; header in TUS upload requests | 
**rest_auth_key** | **str** | Authentication token to pass as the &#x60;X-Auth-Rest&#x60; header in TUS upload requests | 

## Example

```python
from hostinger_api.models.hosting_v1_files_upload_url_resource import HostingV1FilesUploadUrlResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1FilesUploadUrlResource from a JSON string
hosting_v1_files_upload_url_resource_instance = HostingV1FilesUploadUrlResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1FilesUploadUrlResource.to_json())

# convert the object into a dict
hosting_v1_files_upload_url_resource_dict = hosting_v1_files_upload_url_resource_instance.to_dict()
# create an instance of HostingV1FilesUploadUrlResource from a dict
hosting_v1_files_upload_url_resource_from_dict = HostingV1FilesUploadUrlResource.from_dict(hosting_v1_files_upload_url_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


