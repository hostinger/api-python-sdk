# WordPressV1ThemesUpdateThemesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**themes** | **List[str]** | Slugs of the installed themes to update to their latest version. | 

## Example

```python
from hostinger_api.models.word_press_v1_themes_update_themes_request import WordPressV1ThemesUpdateThemesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1ThemesUpdateThemesRequest from a JSON string
word_press_v1_themes_update_themes_request_instance = WordPressV1ThemesUpdateThemesRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1ThemesUpdateThemesRequest.to_json())

# convert the object into a dict
word_press_v1_themes_update_themes_request_dict = word_press_v1_themes_update_themes_request_instance.to_dict()
# create an instance of WordPressV1ThemesUpdateThemesRequest from a dict
word_press_v1_themes_update_themes_request_from_dict = WordPressV1ThemesUpdateThemesRequest.from_dict(word_press_v1_themes_update_themes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


