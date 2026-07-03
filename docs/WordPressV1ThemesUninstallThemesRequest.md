# WordPressV1ThemesUninstallThemesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**themes** | **List[str]** | Slugs of the installed themes to uninstall. | 

## Example

```python
from hostinger_api.models.word_press_v1_themes_uninstall_themes_request import WordPressV1ThemesUninstallThemesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1ThemesUninstallThemesRequest from a JSON string
word_press_v1_themes_uninstall_themes_request_instance = WordPressV1ThemesUninstallThemesRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1ThemesUninstallThemesRequest.to_json())

# convert the object into a dict
word_press_v1_themes_uninstall_themes_request_dict = word_press_v1_themes_uninstall_themes_request_instance.to_dict()
# create an instance of WordPressV1ThemesUninstallThemesRequest from a dict
word_press_v1_themes_uninstall_themes_request_from_dict = WordPressV1ThemesUninstallThemesRequest.from_dict(word_press_v1_themes_uninstall_themes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


