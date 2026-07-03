# WordPressV1PluginsUpdatePluginsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugins** | **List[str]** | Slugs of the installed plugins to update to their latest version. | 

## Example

```python
from hostinger_api.models.word_press_v1_plugins_update_plugins_request import WordPressV1PluginsUpdatePluginsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1PluginsUpdatePluginsRequest from a JSON string
word_press_v1_plugins_update_plugins_request_instance = WordPressV1PluginsUpdatePluginsRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1PluginsUpdatePluginsRequest.to_json())

# convert the object into a dict
word_press_v1_plugins_update_plugins_request_dict = word_press_v1_plugins_update_plugins_request_instance.to_dict()
# create an instance of WordPressV1PluginsUpdatePluginsRequest from a dict
word_press_v1_plugins_update_plugins_request_from_dict = WordPressV1PluginsUpdatePluginsRequest.from_dict(word_press_v1_plugins_update_plugins_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


