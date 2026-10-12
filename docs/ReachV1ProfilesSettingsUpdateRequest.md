# ReachV1ProfilesSettingsUpdateRequest

Settings to change. Only the fields sent are changed; `null` or an empty string clears a text field.

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
**button_corners** | **int** |  | [optional] 
**font_family** | **str** |  | [optional] 
**heading_font_family** | **str** |  | [optional] 
**logo_url** | **str** | Public image URL. Logo uploads are not supported. | [optional] 
**social_links** | **List[str]** |  | [optional] 
**socials** | **Dict[str, str]** | Social profile links keyed by platform. | [optional] 
**about** | **str** |  | [optional] 
**keywords** | **List[str]** |  | [optional] 
**topics** | **List[str]** |  | [optional] 
**selling_points** | **List[str]** |  | [optional] 
**sender_name** | **str** | Default sender name. Letters, numbers and spaces only. | [optional] 
**sender_email** | **str** | Part of the default sender address before the &#x60;@&#x60;, for example &#x60;hello&#x60;. Never send a full address: Reach adds the profile&#39;s connected sending domain itself. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_profiles_settings_update_request import ReachV1ProfilesSettingsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ProfilesSettingsUpdateRequest from a JSON string
reach_v1_profiles_settings_update_request_instance = ReachV1ProfilesSettingsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1ProfilesSettingsUpdateRequest.to_json())

# convert the object into a dict
reach_v1_profiles_settings_update_request_dict = reach_v1_profiles_settings_update_request_instance.to_dict()
# create an instance of ReachV1ProfilesSettingsUpdateRequest from a dict
reach_v1_profiles_settings_update_request_from_dict = ReachV1ProfilesSettingsUpdateRequest.from_dict(reach_v1_profiles_settings_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


