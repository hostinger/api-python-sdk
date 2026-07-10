# AgencyHostingV1SetupsCreateSetupRequestWordpress

WordPress installation options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** |  | 
**title** | **str** |  | 
**admin** | [**AgencyHostingV1SetupsCreateSetupRequestWordpressAdmin**](AgencyHostingV1SetupsCreateSetupRequestWordpressAdmin.md) |  | 

## Example

```python
from hostinger_api.models.agency_hosting_v1_setups_create_setup_request_wordpress import AgencyHostingV1SetupsCreateSetupRequestWordpress

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1SetupsCreateSetupRequestWordpress from a JSON string
agency_hosting_v1_setups_create_setup_request_wordpress_instance = AgencyHostingV1SetupsCreateSetupRequestWordpress.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1SetupsCreateSetupRequestWordpress.to_json())

# convert the object into a dict
agency_hosting_v1_setups_create_setup_request_wordpress_dict = agency_hosting_v1_setups_create_setup_request_wordpress_instance.to_dict()
# create an instance of AgencyHostingV1SetupsCreateSetupRequestWordpress from a dict
agency_hosting_v1_setups_create_setup_request_wordpress_from_dict = AgencyHostingV1SetupsCreateSetupRequestWordpress.from_dict(agency_hosting_v1_setups_create_setup_request_wordpress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


