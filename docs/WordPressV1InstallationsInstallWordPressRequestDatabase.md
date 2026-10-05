# WordPressV1InstallationsInstallWordPressRequestDatabase

Optional. If the named database already exists on the account, it is used for this WordPress install. Otherwise a new database is created with this name, or with a generated name when database is omitted or null. A new database gets a random database user and counts toward the plan's database limit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Database name (username prefix added if missing) | [optional] 
**password** | **str** | Password for a new database. Random when omitted or null. Ignored when the named database already exists. | [optional] 

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


