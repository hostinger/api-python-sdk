# AgencyHostingV1WebsitesWordPressInstallResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | WordPress domain | [optional] 
**title** | **str** | WordPress title | [optional] 
**language** | **str** | WordPress language | [optional] 
**is_config_locked** | **bool** | WordPress configuration lock status | [optional] 
**created_at** | **datetime** | Creation date | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_word_press_install_resource import AgencyHostingV1WebsitesWordPressInstallResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesWordPressInstallResource from a JSON string
agency_hosting_v1_websites_word_press_install_resource_instance = AgencyHostingV1WebsitesWordPressInstallResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesWordPressInstallResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_word_press_install_resource_dict = agency_hosting_v1_websites_word_press_install_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesWordPressInstallResource from a dict
agency_hosting_v1_websites_word_press_install_resource_from_dict = AgencyHostingV1WebsitesWordPressInstallResource.from_dict(agency_hosting_v1_websites_word_press_install_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


