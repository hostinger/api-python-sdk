# WordPressV1ThemesInstallThemeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**theme** | **str** | Slug of the theme to install. Hostinger theme slugs (hostinger-blog, hostinger-affiliate-theme, hostinger-ai-theme) trigger the custom installer and forward the optional palette/layout/font fields; any other WordPress theme slug uses the standard installer and ignores those fields. | 
**palette** | **str** | Palette identifier. Only applied when the theme is a Hostinger theme; the default is used when omitted. | [optional] [default to 'palette1']
**layout** | **str** | Layout identifier. Only applied when the theme is a Hostinger theme; the default is used when omitted. | [optional] [default to 'layout1']
**font** | **str** | Font identifier. Only applied when the theme is a Hostinger theme; the default is used when omitted. | [optional] [default to 'default']

## Example

```python
from hostinger_api.models.word_press_v1_themes_install_theme_request import WordPressV1ThemesInstallThemeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1ThemesInstallThemeRequest from a JSON string
word_press_v1_themes_install_theme_request_instance = WordPressV1ThemesInstallThemeRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1ThemesInstallThemeRequest.to_json())

# convert the object into a dict
word_press_v1_themes_install_theme_request_dict = word_press_v1_themes_install_theme_request_instance.to_dict()
# create an instance of WordPressV1ThemesInstallThemeRequest from a dict
word_press_v1_themes_install_theme_request_from_dict = WordPressV1ThemesInstallThemeRequest.from_dict(word_press_v1_themes_install_theme_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


