# WordPressV1PluginsSuggestedPluginGroupResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**website_type** | **str** | Website type the suggested plugins are grouped by | [optional] 
**plugins** | [**List[WordPressV1PluginsSuggestedPluginResource]**](WordPressV1PluginsSuggestedPluginResource.md) | Plugins suggested for the website type | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_plugins_suggested_plugin_group_resource import WordPressV1PluginsSuggestedPluginGroupResource

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1PluginsSuggestedPluginGroupResource from a JSON string
word_press_v1_plugins_suggested_plugin_group_resource_instance = WordPressV1PluginsSuggestedPluginGroupResource.from_json(json)
# print the JSON string representation of the object
print(WordPressV1PluginsSuggestedPluginGroupResource.to_json())

# convert the object into a dict
word_press_v1_plugins_suggested_plugin_group_resource_dict = word_press_v1_plugins_suggested_plugin_group_resource_instance.to_dict()
# create an instance of WordPressV1PluginsSuggestedPluginGroupResource from a dict
word_press_v1_plugins_suggested_plugin_group_resource_from_dict = WordPressV1PluginsSuggestedPluginGroupResource.from_dict(word_press_v1_plugins_suggested_plugin_group_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


