# WordPressV1ThemesActivateThemeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**theme** | **str** | Slug of the installed theme to activate. | 

## Example

```python
from hostinger_api.models.word_press_v1_themes_activate_theme_request import WordPressV1ThemesActivateThemeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1ThemesActivateThemeRequest from a JSON string
word_press_v1_themes_activate_theme_request_instance = WordPressV1ThemesActivateThemeRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1ThemesActivateThemeRequest.to_json())

# convert the object into a dict
word_press_v1_themes_activate_theme_request_dict = word_press_v1_themes_activate_theme_request_instance.to_dict()
# create an instance of WordPressV1ThemesActivateThemeRequest from a dict
word_press_v1_themes_activate_theme_request_from_dict = WordPressV1ThemesActivateThemeRequest.from_dict(word_press_v1_themes_activate_theme_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


