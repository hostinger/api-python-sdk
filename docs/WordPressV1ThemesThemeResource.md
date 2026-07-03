# WordPressV1ThemesThemeResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | Theme slug used when installing the theme | [optional] 
**title** | **str** | Human readable theme name | [optional] 
**url** | **str** | Link to the theme page on WordPress.org | [optional] 
**featured_image_url** | **str** | URL of the theme preview thumbnail | [optional] 
**full_image_url** | **str** | URL of the full-size theme preview image | [optional] 
**description** | **str** | Short theme description | [optional] 
**logo_url** | **str** | URL of the theme logo | [optional] 
**is_plan_upgrade_needed** | **bool** | Whether a hosting plan upgrade is required to use the theme | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_themes_theme_resource import WordPressV1ThemesThemeResource

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1ThemesThemeResource from a JSON string
word_press_v1_themes_theme_resource_instance = WordPressV1ThemesThemeResource.from_json(json)
# print the JSON string representation of the object
print(WordPressV1ThemesThemeResource.to_json())

# convert the object into a dict
word_press_v1_themes_theme_resource_dict = word_press_v1_themes_theme_resource_instance.to_dict()
# create an instance of WordPressV1ThemesThemeResource from a dict
word_press_v1_themes_theme_resource_from_dict = WordPressV1ThemesThemeResource.from_dict(word_press_v1_themes_theme_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


