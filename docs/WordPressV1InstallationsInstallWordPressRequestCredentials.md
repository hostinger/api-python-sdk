# WordPressV1InstallationsInstallWordPressRequestCredentials

WordPress admin credentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**login** | **str** | WordPress admin username | 
**password** | **str** |  | 

## Example

```python
from hostinger_api.models.word_press_v1_installations_install_word_press_request_credentials import WordPressV1InstallationsInstallWordPressRequestCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1InstallationsInstallWordPressRequestCredentials from a JSON string
word_press_v1_installations_install_word_press_request_credentials_instance = WordPressV1InstallationsInstallWordPressRequestCredentials.from_json(json)
# print the JSON string representation of the object
print(WordPressV1InstallationsInstallWordPressRequestCredentials.to_json())

# convert the object into a dict
word_press_v1_installations_install_word_press_request_credentials_dict = word_press_v1_installations_install_word_press_request_credentials_instance.to_dict()
# create an instance of WordPressV1InstallationsInstallWordPressRequestCredentials from a dict
word_press_v1_installations_install_word_press_request_credentials_from_dict = WordPressV1InstallationsInstallWordPressRequestCredentials.from_dict(word_press_v1_installations_install_word_press_request_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


