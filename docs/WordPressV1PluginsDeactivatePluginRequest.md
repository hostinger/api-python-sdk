# WordPressV1PluginsDeactivatePluginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin** | **str** | Slug of the installed plugin to deactivate. | 

## Example

```python
from hostinger_api.models.word_press_v1_plugins_deactivate_plugin_request import WordPressV1PluginsDeactivatePluginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1PluginsDeactivatePluginRequest from a JSON string
word_press_v1_plugins_deactivate_plugin_request_instance = WordPressV1PluginsDeactivatePluginRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1PluginsDeactivatePluginRequest.to_json())

# convert the object into a dict
word_press_v1_plugins_deactivate_plugin_request_dict = word_press_v1_plugins_deactivate_plugin_request_instance.to_dict()
# create an instance of WordPressV1PluginsDeactivatePluginRequest from a dict
word_press_v1_plugins_deactivate_plugin_request_from_dict = WordPressV1PluginsDeactivatePluginRequest.from_dict(word_press_v1_plugins_deactivate_plugin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


