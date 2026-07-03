# WordPressV1PluginsUninstallPluginsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugins** | **List[str]** | Slugs of the installed plugins to uninstall. | 

## Example

```python
from hostinger_api.models.word_press_v1_plugins_uninstall_plugins_request import WordPressV1PluginsUninstallPluginsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1PluginsUninstallPluginsRequest from a JSON string
word_press_v1_plugins_uninstall_plugins_request_instance = WordPressV1PluginsUninstallPluginsRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1PluginsUninstallPluginsRequest.to_json())

# convert the object into a dict
word_press_v1_plugins_uninstall_plugins_request_dict = word_press_v1_plugins_uninstall_plugins_request_instance.to_dict()
# create an instance of WordPressV1PluginsUninstallPluginsRequest from a dict
word_press_v1_plugins_uninstall_plugins_request_from_dict = WordPressV1PluginsUninstallPluginsRequest.from_dict(word_press_v1_plugins_uninstall_plugins_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


