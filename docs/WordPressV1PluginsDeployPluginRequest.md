# WordPressV1PluginsDeployPluginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | Slug of the plugin | 
**plugin_path** | **str** | Relative path to the plugin directory from wp-content/plugins | 

## Example

```python
from hostinger_api.models.word_press_v1_plugins_deploy_plugin_request import WordPressV1PluginsDeployPluginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1PluginsDeployPluginRequest from a JSON string
word_press_v1_plugins_deploy_plugin_request_instance = WordPressV1PluginsDeployPluginRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1PluginsDeployPluginRequest.to_json())

# convert the object into a dict
word_press_v1_plugins_deploy_plugin_request_dict = word_press_v1_plugins_deploy_plugin_request_instance.to_dict()
# create an instance of WordPressV1PluginsDeployPluginRequest from a dict
word_press_v1_plugins_deploy_plugin_request_from_dict = WordPressV1PluginsDeployPluginRequest.from_dict(word_press_v1_plugins_deploy_plugin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


