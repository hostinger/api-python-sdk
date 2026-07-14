# AgencyHostingV1FilesImportArchiveRequest

Import a website from an already-uploaded archive

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_name** | **str** | Archive filename (e.g., archive.zip). The file must already be uploaded to the website&#39;s .h5g/ directory. | 

## Example

```python
from hostinger_api.models.agency_hosting_v1_files_import_archive_request import AgencyHostingV1FilesImportArchiveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1FilesImportArchiveRequest from a JSON string
agency_hosting_v1_files_import_archive_request_instance = AgencyHostingV1FilesImportArchiveRequest.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1FilesImportArchiveRequest.to_json())

# convert the object into a dict
agency_hosting_v1_files_import_archive_request_dict = agency_hosting_v1_files_import_archive_request_instance.to_dict()
# create an instance of AgencyHostingV1FilesImportArchiveRequest from a dict
agency_hosting_v1_files_import_archive_request_from_dict = AgencyHostingV1FilesImportArchiveRequest.from_dict(agency_hosting_v1_files_import_archive_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


