# AgencyHostingV1WebsitesWebsiteSshDetailsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | SSH username | [optional] 
**host** | **str** | SSH host | [optional] 
**port** | **int** | SSH port | [optional] 
**is_enabled** | **bool** | Is SSH access enabled | [optional] 
**is_password_enabled** | **bool** | Is SSH password access enabled | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_website_ssh_details_resource import AgencyHostingV1WebsitesWebsiteSshDetailsResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesWebsiteSshDetailsResource from a JSON string
agency_hosting_v1_websites_website_ssh_details_resource_instance = AgencyHostingV1WebsitesWebsiteSshDetailsResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesWebsiteSshDetailsResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_website_ssh_details_resource_dict = agency_hosting_v1_websites_website_ssh_details_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesWebsiteSshDetailsResource from a dict
agency_hosting_v1_websites_website_ssh_details_resource_from_dict = AgencyHostingV1WebsitesWebsiteSshDetailsResource.from_dict(agency_hosting_v1_websites_website_ssh_details_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


