# WordPressV1PluginsInstallPluginsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugins** | **List[str]** | Plugin slugs to install. Use GET /api/hosting/v1/wordpress/plugins to discover available slugs. | 

## Example

```python
from hostinger_api.models.word_press_v1_plugins_install_plugins_request import WordPressV1PluginsInstallPluginsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1PluginsInstallPluginsRequest from a JSON string
word_press_v1_plugins_install_plugins_request_instance = WordPressV1PluginsInstallPluginsRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1PluginsInstallPluginsRequest.to_json())

# convert the object into a dict
word_press_v1_plugins_install_plugins_request_dict = word_press_v1_plugins_install_plugins_request_instance.to_dict()
# create an instance of WordPressV1PluginsInstallPluginsRequest from a dict
word_press_v1_plugins_install_plugins_request_from_dict = WordPressV1PluginsInstallPluginsRequest.from_dict(word_press_v1_plugins_install_plugins_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


