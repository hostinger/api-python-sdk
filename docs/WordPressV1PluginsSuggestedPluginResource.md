# WordPressV1PluginsSuggestedPluginResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | Plugin slug used when installing the plugin | [optional] 
**title** | **str** | Human readable plugin name | [optional] 
**description** | **str** | Short plugin description | [optional] 
**onboarding_description_slug** | **str** | Translation slug for the onboarding description | [optional] 
**recommended_description_slug** | **str** | Translation slug for the recommended description | [optional] 
**link** | **str** | Link to the plugin page on WordPress.org | [optional] 
**version** | **str** | Latest available plugin version | [optional] 
**required_wordpress_version** | **str** | Minimum WordPress version required by the plugin | [optional] 
**required_php_version** | **str** | Minimum PHP version required by the plugin | [optional] 
**is_preselected** | **bool** | Whether the plugin is preselected during onboarding | [optional] 
**is_plan_upgrade_needed** | **bool** | Whether a hosting plan upgrade is required to use the plugin | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_plugins_suggested_plugin_resource import WordPressV1PluginsSuggestedPluginResource

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1PluginsSuggestedPluginResource from a JSON string
word_press_v1_plugins_suggested_plugin_resource_instance = WordPressV1PluginsSuggestedPluginResource.from_json(json)
# print the JSON string representation of the object
print(WordPressV1PluginsSuggestedPluginResource.to_json())

# convert the object into a dict
word_press_v1_plugins_suggested_plugin_resource_dict = word_press_v1_plugins_suggested_plugin_resource_instance.to_dict()
# create an instance of WordPressV1PluginsSuggestedPluginResource from a dict
word_press_v1_plugins_suggested_plugin_resource_from_dict = WordPressV1PluginsSuggestedPluginResource.from_dict(word_press_v1_plugins_suggested_plugin_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


