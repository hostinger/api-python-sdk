# ReachV1ProfilesSettingsSettingsResource

Sender identity and brand details saved on the profile.  A profile that never filled its settings in returns empty values, so every field can be `null`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_name** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**business_address** | **str** |  | [optional] 
**privacy_policy_url** | **str** |  | [optional] 
**accent_color** | **str** |  | [optional] 
**button_color** | **str** |  | [optional] 
**background_color** | **str** |  | [optional] 
**text_color** | **str** |  | [optional] 
**links_color** | **str** |  | [optional] 
**button_text** | **str** | Button text colour. | [optional] 
**button_corners** | **int** | Button corner radius in pixels. | [optional] 
**font_family** | **str** | Body and button font. | [optional] 
**heading_font_family** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**social_links** | **List[str]** |  | [optional] 
**socials** | **Dict[str, str]** | Social profile links keyed by platform. | [optional] 
**about** | **str** |  | [optional] 
**keywords** | **List[str]** |  | [optional] 
**topics** | **List[str]** |  | [optional] 
**selling_points** | **List[str]** |  | [optional] 
**sender_name** | **str** | Default sender name that campaigns created afterwards start from. | [optional] 
**sender_email** | **str** | Part of the default sender address before the &#x60;@&#x60;. It is combined with the profile&#39;s connected sending domain, see the connected sending domain endpoint. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_profiles_settings_settings_resource import ReachV1ProfilesSettingsSettingsResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ProfilesSettingsSettingsResource from a JSON string
reach_v1_profiles_settings_settings_resource_instance = ReachV1ProfilesSettingsSettingsResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1ProfilesSettingsSettingsResource.to_json())

# convert the object into a dict
reach_v1_profiles_settings_settings_resource_dict = reach_v1_profiles_settings_settings_resource_instance.to_dict()
# create an instance of ReachV1ProfilesSettingsSettingsResource from a dict
reach_v1_profiles_settings_settings_resource_from_dict = ReachV1ProfilesSettingsSettingsResource.from_dict(reach_v1_profiles_settings_settings_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


