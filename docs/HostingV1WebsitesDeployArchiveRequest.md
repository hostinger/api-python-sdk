# HostingV1WebsitesDeployArchiveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_path** | **str** | Relative path to the archive file from website root directory | 

## Example

```python
from hostinger_api.models.hosting_v1_websites_deploy_archive_request import HostingV1WebsitesDeployArchiveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1WebsitesDeployArchiveRequest from a JSON string
hosting_v1_websites_deploy_archive_request_instance = HostingV1WebsitesDeployArchiveRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1WebsitesDeployArchiveRequest.to_json())

# convert the object into a dict
hosting_v1_websites_deploy_archive_request_dict = hosting_v1_websites_deploy_archive_request_instance.to_dict()
# create an instance of HostingV1WebsitesDeployArchiveRequest from a dict
hosting_v1_websites_deploy_archive_request_from_dict = HostingV1WebsitesDeployArchiveRequest.from_dict(hosting_v1_websites_deploy_archive_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


