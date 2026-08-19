# WordPressV1ThemesDeployThemeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | Slug of the theme | 
**theme_path** | **str** | Relative path to the theme directory from wp-content/themes | 
**is_activated** | **bool** | Whether to activate the theme after deployment | [optional] [default to False]

## Example

```python
from hostinger_api.models.word_press_v1_themes_deploy_theme_request import WordPressV1ThemesDeployThemeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1ThemesDeployThemeRequest from a JSON string
word_press_v1_themes_deploy_theme_request_instance = WordPressV1ThemesDeployThemeRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1ThemesDeployThemeRequest.to_json())

# convert the object into a dict
word_press_v1_themes_deploy_theme_request_dict = word_press_v1_themes_deploy_theme_request_instance.to_dict()
# create an instance of WordPressV1ThemesDeployThemeRequest from a dict
word_press_v1_themes_deploy_theme_request_from_dict = WordPressV1ThemesDeployThemeRequest.from_dict(word_press_v1_themes_deploy_theme_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


