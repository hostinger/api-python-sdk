# WordPressV1InstallationsInstallWordPressRequestDatabase

Optional. If the named database already exists, it will be used for this WordPress install. Otherwise a new database is created with a generated name and random credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Database name (username prefix added if missing) | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_installations_install_word_press_request_database import WordPressV1InstallationsInstallWordPressRequestDatabase

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1InstallationsInstallWordPressRequestDatabase from a JSON string
word_press_v1_installations_install_word_press_request_database_instance = WordPressV1InstallationsInstallWordPressRequestDatabase.from_json(json)
# print the JSON string representation of the object
print(WordPressV1InstallationsInstallWordPressRequestDatabase.to_json())

# convert the object into a dict
word_press_v1_installations_install_word_press_request_database_dict = word_press_v1_installations_install_word_press_request_database_instance.to_dict()
# create an instance of WordPressV1InstallationsInstallWordPressRequestDatabase from a dict
word_press_v1_installations_install_word_press_request_database_from_dict = WordPressV1InstallationsInstallWordPressRequestDatabase.from_dict(word_press_v1_installations_install_word_press_request_database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


