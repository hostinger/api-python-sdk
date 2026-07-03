# WordPressV1PluginsActivatePluginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin** | **str** | Slug of the installed plugin to activate. | 

## Example

```python
from hostinger_api.models.word_press_v1_plugins_activate_plugin_request import WordPressV1PluginsActivatePluginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1PluginsActivatePluginRequest from a JSON string
word_press_v1_plugins_activate_plugin_request_instance = WordPressV1PluginsActivatePluginRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1PluginsActivatePluginRequest.to_json())

# convert the object into a dict
word_press_v1_plugins_activate_plugin_request_dict = word_press_v1_plugins_activate_plugin_request_instance.to_dict()
# create an instance of WordPressV1PluginsActivatePluginRequest from a dict
word_press_v1_plugins_activate_plugin_request_from_dict = WordPressV1PluginsActivatePluginRequest.from_dict(word_press_v1_plugins_activate_plugin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


