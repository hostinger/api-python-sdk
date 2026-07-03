# WordPressV1ThemesInstalledThemeResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Theme slug | [optional] 
**title** | **str** | Human readable theme name | [optional] 
**version** | **str** | Installed theme version | [optional] 
**status** | **str** | Whether the theme is active or inactive | [optional] 
**update** | **str** | Available update version, or \&quot;none\&quot; when up to date | [optional] 
**vulnerabilities** | [**List[WordPressV1CommonVulnerabilityResource]**](WordPressV1CommonVulnerabilityResource.md) | Known vulnerabilities affecting the installed version | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_themes_installed_theme_resource import WordPressV1ThemesInstalledThemeResource

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1ThemesInstalledThemeResource from a JSON string
word_press_v1_themes_installed_theme_resource_instance = WordPressV1ThemesInstalledThemeResource.from_json(json)
# print the JSON string representation of the object
print(WordPressV1ThemesInstalledThemeResource.to_json())

# convert the object into a dict
word_press_v1_themes_installed_theme_resource_dict = word_press_v1_themes_installed_theme_resource_instance.to_dict()
# create an instance of WordPressV1ThemesInstalledThemeResource from a dict
word_press_v1_themes_installed_theme_resource_from_dict = WordPressV1ThemesInstalledThemeResource.from_dict(word_press_v1_themes_installed_theme_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


