# WordPressV1PluginsInstalledPluginResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Plugin slug | [optional] 
**title** | **str** | Human readable plugin name | [optional] 
**version** | **str** | Installed plugin version | [optional] 
**status** | **str** | Whether the plugin is active or inactive | [optional] 
**update** | **str** | Available update version, or \&quot;none\&quot; when up to date | [optional] 
**vulnerabilities** | [**List[WordPressV1CommonVulnerabilityResource]**](WordPressV1CommonVulnerabilityResource.md) | Known vulnerabilities affecting the installed version | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_plugins_installed_plugin_resource import WordPressV1PluginsInstalledPluginResource

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1PluginsInstalledPluginResource from a JSON string
word_press_v1_plugins_installed_plugin_resource_instance = WordPressV1PluginsInstalledPluginResource.from_json(json)
# print the JSON string representation of the object
print(WordPressV1PluginsInstalledPluginResource.to_json())

# convert the object into a dict
word_press_v1_plugins_installed_plugin_resource_dict = word_press_v1_plugins_installed_plugin_resource_instance.to_dict()
# create an instance of WordPressV1PluginsInstalledPluginResource from a dict
word_press_v1_plugins_installed_plugin_resource_from_dict = WordPressV1PluginsInstalledPluginResource.from_dict(word_press_v1_plugins_installed_plugin_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


