# AgencyHostingV1SetupsWebsiteSetupResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**setup_uuid** | **str** | UUID tracking the asynchronous website setup process | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_setups_website_setup_resource import AgencyHostingV1SetupsWebsiteSetupResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1SetupsWebsiteSetupResource from a JSON string
agency_hosting_v1_setups_website_setup_resource_instance = AgencyHostingV1SetupsWebsiteSetupResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1SetupsWebsiteSetupResource.to_json())

# convert the object into a dict
agency_hosting_v1_setups_website_setup_resource_dict = agency_hosting_v1_setups_website_setup_resource_instance.to_dict()
# create an instance of AgencyHostingV1SetupsWebsiteSetupResource from a dict
agency_hosting_v1_setups_website_setup_resource_from_dict = AgencyHostingV1SetupsWebsiteSetupResource.from_dict(agency_hosting_v1_setups_website_setup_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


