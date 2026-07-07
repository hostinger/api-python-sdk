# WordPressV1InstallationsDeleteInstallationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_files** | **bool** | Delete installation files from disk. | [optional] [default to False]
**delete_database** | **bool** | Delete the installation database. | [optional] [default to False]

## Example

```python
from hostinger_api.models.word_press_v1_installations_delete_installation_request import WordPressV1InstallationsDeleteInstallationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1InstallationsDeleteInstallationRequest from a JSON string
word_press_v1_installations_delete_installation_request_instance = WordPressV1InstallationsDeleteInstallationRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1InstallationsDeleteInstallationRequest.to_json())

# convert the object into a dict
word_press_v1_installations_delete_installation_request_dict = word_press_v1_installations_delete_installation_request_instance.to_dict()
# create an instance of WordPressV1InstallationsDeleteInstallationRequest from a dict
word_press_v1_installations_delete_installation_request_from_dict = WordPressV1InstallationsDeleteInstallationRequest.from_dict(word_press_v1_installations_delete_installation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


