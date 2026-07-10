# AgencyHostingV1SetupsWebsiteSetupStatusResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**website_uid** | **str** | UID of the website created by the setup, available once provisioning completes | [optional] 
**status** | **str** | Website setup status | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_setups_website_setup_status_resource import AgencyHostingV1SetupsWebsiteSetupStatusResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1SetupsWebsiteSetupStatusResource from a JSON string
agency_hosting_v1_setups_website_setup_status_resource_instance = AgencyHostingV1SetupsWebsiteSetupStatusResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1SetupsWebsiteSetupStatusResource.to_json())

# convert the object into a dict
agency_hosting_v1_setups_website_setup_status_resource_dict = agency_hosting_v1_setups_website_setup_status_resource_instance.to_dict()
# create an instance of AgencyHostingV1SetupsWebsiteSetupStatusResource from a dict
agency_hosting_v1_setups_website_setup_status_resource_from_dict = AgencyHostingV1SetupsWebsiteSetupStatusResource.from_dict(agency_hosting_v1_setups_website_setup_status_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


