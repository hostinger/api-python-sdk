# WordPressV1InstallationsImportWordPressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_path** | **str** | Path to the WordPress archive file (relative to website root) | 
**sql_path** | **str** | Path to the database SQL file (relative to website root) | 

## Example

```python
from hostinger_api.models.word_press_v1_installations_import_word_press_request import WordPressV1InstallationsImportWordPressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1InstallationsImportWordPressRequest from a JSON string
word_press_v1_installations_import_word_press_request_instance = WordPressV1InstallationsImportWordPressRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1InstallationsImportWordPressRequest.to_json())

# convert the object into a dict
word_press_v1_installations_import_word_press_request_dict = word_press_v1_installations_import_word_press_request_instance.to_dict()
# create an instance of WordPressV1InstallationsImportWordPressRequest from a dict
word_press_v1_installations_import_word_press_request_from_dict = WordPressV1InstallationsImportWordPressRequest.from_dict(word_press_v1_installations_import_word_press_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


