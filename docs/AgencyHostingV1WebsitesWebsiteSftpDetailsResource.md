# AgencyHostingV1WebsitesWebsiteSftpDetailsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | SFTP username | [optional] 
**host** | **str** | SFTP host | [optional] 
**port** | **int** | SFTP port | [optional] 
**is_enabled** | **bool** | Is SFTP access enabled | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_website_sftp_details_resource import AgencyHostingV1WebsitesWebsiteSftpDetailsResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesWebsiteSftpDetailsResource from a JSON string
agency_hosting_v1_websites_website_sftp_details_resource_instance = AgencyHostingV1WebsitesWebsiteSftpDetailsResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesWebsiteSftpDetailsResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_website_sftp_details_resource_dict = agency_hosting_v1_websites_website_sftp_details_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesWebsiteSftpDetailsResource from a dict
agency_hosting_v1_websites_website_sftp_details_resource_from_dict = AgencyHostingV1WebsitesWebsiteSftpDetailsResource.from_dict(agency_hosting_v1_websites_website_sftp_details_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


