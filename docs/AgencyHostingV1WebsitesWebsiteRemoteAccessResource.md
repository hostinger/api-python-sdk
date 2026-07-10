# AgencyHostingV1WebsitesWebsiteRemoteAccessResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Remote access mode | [optional] 
**ssh** | [**AgencyHostingV1WebsitesWebsiteSshDetailsResource**](AgencyHostingV1WebsitesWebsiteSshDetailsResource.md) |  | [optional] 
**sftp** | [**AgencyHostingV1WebsitesWebsiteSftpDetailsResource**](AgencyHostingV1WebsitesWebsiteSftpDetailsResource.md) |  | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_website_remote_access_resource import AgencyHostingV1WebsitesWebsiteRemoteAccessResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesWebsiteRemoteAccessResource from a JSON string
agency_hosting_v1_websites_website_remote_access_resource_instance = AgencyHostingV1WebsitesWebsiteRemoteAccessResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesWebsiteRemoteAccessResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_website_remote_access_resource_dict = agency_hosting_v1_websites_website_remote_access_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesWebsiteRemoteAccessResource from a dict
agency_hosting_v1_websites_website_remote_access_resource_from_dict = AgencyHostingV1WebsitesWebsiteRemoteAccessResource.from_dict(agency_hosting_v1_websites_website_remote_access_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


