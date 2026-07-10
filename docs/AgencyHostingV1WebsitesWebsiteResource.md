# AgencyHostingV1WebsitesWebsiteResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Website UID | [optional] 
**ipv4** | **str** | IPv4 address | [optional] 
**flavor** | **str** | Setup flavor | [optional] 
**type** | **str** | Website type | [optional] 
**description** | **str** | Description | [optional] 
**state** | **str** | Website state | [optional] 
**created_at** | **datetime** |  | [optional] 
**domains** | [**List[AgencyHostingV1WebsitesWebsiteDomainDetailsResource]**](AgencyHostingV1WebsitesWebsiteDomainDetailsResource.md) | Array of [&#x60;AgencyHosting.V1.Websites.WebsiteDomainDetailsResource&#x60;](#model/agencyhostingv1websiteswebsitedomaindetailsresource) | [optional] 
**preview_domain** | [**AgencyHostingV1WebsitesWebsitePreviewDomainResource**](AgencyHostingV1WebsitesWebsitePreviewDomainResource.md) |  | [optional] 
**settings** | [**AgencyHostingV1WebsitesWebsiteSettingsResource**](AgencyHostingV1WebsitesWebsiteSettingsResource.md) |  | [optional] 
**wordpress** | [**AgencyHostingV1WebsitesWordPressInstallResource**](AgencyHostingV1WebsitesWordPressInstallResource.md) |  | [optional] 
**remote_access** | [**AgencyHostingV1WebsitesWebsiteRemoteAccessResource**](AgencyHostingV1WebsitesWebsiteRemoteAccessResource.md) |  | [optional] 
**server** | [**AgencyHostingV1WebsitesWebsiteServerResource**](AgencyHostingV1WebsitesWebsiteServerResource.md) |  | [optional] 
**order** | [**AgencyHostingV1WebsitesWebsiteOrderResource**](AgencyHostingV1WebsitesWebsiteOrderResource.md) |  | [optional] 
**user** | [**AgencyHostingV1WebsitesWebsiteUserResource**](AgencyHostingV1WebsitesWebsiteUserResource.md) |  | [optional] 
**staging_root** | [**AgencyHostingV1WebsitesWebsiteStagingRootResource**](AgencyHostingV1WebsitesWebsiteStagingRootResource.md) |  | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_website_resource import AgencyHostingV1WebsitesWebsiteResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesWebsiteResource from a JSON string
agency_hosting_v1_websites_website_resource_instance = AgencyHostingV1WebsitesWebsiteResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesWebsiteResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_website_resource_dict = agency_hosting_v1_websites_website_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesWebsiteResource from a dict
agency_hosting_v1_websites_website_resource_from_dict = AgencyHostingV1WebsitesWebsiteResource.from_dict(agency_hosting_v1_websites_website_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


