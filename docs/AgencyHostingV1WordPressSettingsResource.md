# AgencyHostingV1WordPressSettingsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core_version** | **str** | Currently installed WordPress core version, or null when it cannot be determined. | [optional] 
**is_lite_speed_cache_enabled** | **bool** | Whether the LiteSpeed Cache plugin is active. | [optional] 
**is_object_cache_enabled** | **bool** | Whether LiteSpeed object cache is enabled. | [optional] 
**is_maintenance_mode_enabled** | **bool** | Whether WordPress maintenance mode is currently enabled. | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_word_press_settings_resource import AgencyHostingV1WordPressSettingsResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WordPressSettingsResource from a JSON string
agency_hosting_v1_word_press_settings_resource_instance = AgencyHostingV1WordPressSettingsResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WordPressSettingsResource.to_json())

# convert the object into a dict
agency_hosting_v1_word_press_settings_resource_dict = agency_hosting_v1_word_press_settings_resource_instance.to_dict()
# create an instance of AgencyHostingV1WordPressSettingsResource from a dict
agency_hosting_v1_word_press_settings_resource_from_dict = AgencyHostingV1WordPressSettingsResource.from_dict(agency_hosting_v1_word_press_settings_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


