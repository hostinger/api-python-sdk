# WordPressV1PluginsPluginResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | Plugin slug used when installing the plugin | [optional] 
**title** | **str** | Human readable plugin name | [optional] 
**icons** | [**WordPressV1PluginsPluginResourceIcons**](WordPressV1PluginsPluginResourceIcons.md) |  | [optional] 
**description** | **str** | Short plugin description | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_plugins_plugin_resource import WordPressV1PluginsPluginResource

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1PluginsPluginResource from a JSON string
word_press_v1_plugins_plugin_resource_instance = WordPressV1PluginsPluginResource.from_json(json)
# print the JSON string representation of the object
print(WordPressV1PluginsPluginResource.to_json())

# convert the object into a dict
word_press_v1_plugins_plugin_resource_dict = word_press_v1_plugins_plugin_resource_instance.to_dict()
# create an instance of WordPressV1PluginsPluginResource from a dict
word_press_v1_plugins_plugin_resource_from_dict = WordPressV1PluginsPluginResource.from_dict(word_press_v1_plugins_plugin_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


