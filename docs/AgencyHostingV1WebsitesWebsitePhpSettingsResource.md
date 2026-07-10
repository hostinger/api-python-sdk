# AgencyHostingV1WebsitesWebsitePhpSettingsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | PHP version | [optional] 
**workers** | **int** | Number of PHP workers | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_website_php_settings_resource import AgencyHostingV1WebsitesWebsitePhpSettingsResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesWebsitePhpSettingsResource from a JSON string
agency_hosting_v1_websites_website_php_settings_resource_instance = AgencyHostingV1WebsitesWebsitePhpSettingsResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesWebsitePhpSettingsResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_website_php_settings_resource_dict = agency_hosting_v1_websites_website_php_settings_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesWebsitePhpSettingsResource from a dict
agency_hosting_v1_websites_website_php_settings_resource_from_dict = AgencyHostingV1WebsitesWebsitePhpSettingsResource.from_dict(agency_hosting_v1_websites_website_php_settings_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


