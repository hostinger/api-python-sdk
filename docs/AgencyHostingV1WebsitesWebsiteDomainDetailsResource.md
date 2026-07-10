# AgencyHostingV1WebsitesWebsiteDomainDetailsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | Domain name | [optional] 
**parent_fqdn** | **str** | Parent domain name if the domain is a subdomain | [optional] 
**ipv6** | **str** | IPv6 address | [optional] 
**created_at** | **datetime** |  | [optional] 
**nameservers** | **List[str]** |  | [optional] 
**ssl_cert** | [**AgencyHostingV1WebsitesSslCertResource**](AgencyHostingV1WebsitesSslCertResource.md) |  | [optional] 
**custom_ssl_cert** | [**AgencyHostingV1WebsitesCustomSslCertResource**](AgencyHostingV1WebsitesCustomSslCertResource.md) |  | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_website_domain_details_resource import AgencyHostingV1WebsitesWebsiteDomainDetailsResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesWebsiteDomainDetailsResource from a JSON string
agency_hosting_v1_websites_website_domain_details_resource_instance = AgencyHostingV1WebsitesWebsiteDomainDetailsResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesWebsiteDomainDetailsResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_website_domain_details_resource_dict = agency_hosting_v1_websites_website_domain_details_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesWebsiteDomainDetailsResource from a dict
agency_hosting_v1_websites_website_domain_details_resource_from_dict = AgencyHostingV1WebsitesWebsiteDomainDetailsResource.from_dict(agency_hosting_v1_websites_website_domain_details_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


