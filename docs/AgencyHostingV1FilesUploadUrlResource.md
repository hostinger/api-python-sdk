# AgencyHostingV1FilesUploadUrlResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The TUS upload endpoint URL to send upload requests to | 
**auth_key** | **str** | Authentication token to pass as the &#x60;X-Auth&#x60; header in TUS upload requests | 
**rest_auth_key** | **str** | Authentication token to pass as the &#x60;X-Auth-Rest&#x60; header in TUS upload requests | 

## Example

```python
from hostinger_api.models.agency_hosting_v1_files_upload_url_resource import AgencyHostingV1FilesUploadUrlResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1FilesUploadUrlResource from a JSON string
agency_hosting_v1_files_upload_url_resource_instance = AgencyHostingV1FilesUploadUrlResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1FilesUploadUrlResource.to_json())

# convert the object into a dict
agency_hosting_v1_files_upload_url_resource_dict = agency_hosting_v1_files_upload_url_resource_instance.to_dict()
# create an instance of AgencyHostingV1FilesUploadUrlResource from a dict
agency_hosting_v1_files_upload_url_resource_from_dict = AgencyHostingV1FilesUploadUrlResource.from_dict(agency_hosting_v1_files_upload_url_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


