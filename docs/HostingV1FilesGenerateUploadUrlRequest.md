# HostingV1FilesGenerateUploadUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Account username | 
**domain** | **str** | Website domain | 

## Example

```python
from hostinger_api.models.hosting_v1_files_generate_upload_url_request import HostingV1FilesGenerateUploadUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1FilesGenerateUploadUrlRequest from a JSON string
hosting_v1_files_generate_upload_url_request_instance = HostingV1FilesGenerateUploadUrlRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1FilesGenerateUploadUrlRequest.to_json())

# convert the object into a dict
hosting_v1_files_generate_upload_url_request_dict = hosting_v1_files_generate_upload_url_request_instance.to_dict()
# create an instance of HostingV1FilesGenerateUploadUrlRequest from a dict
hosting_v1_files_generate_upload_url_request_from_dict = HostingV1FilesGenerateUploadUrlRequest.from_dict(hosting_v1_files_generate_upload_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


