# WordPressV1InstallationsUpdateInstallationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minor** | **bool** | Update the minor version only. | [optional] [default to False]
**version** | **str** | Update to a specific WordPress core version. | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_installations_update_installation_request import WordPressV1InstallationsUpdateInstallationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1InstallationsUpdateInstallationRequest from a JSON string
word_press_v1_installations_update_installation_request_instance = WordPressV1InstallationsUpdateInstallationRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1InstallationsUpdateInstallationRequest.to_json())

# convert the object into a dict
word_press_v1_installations_update_installation_request_dict = word_press_v1_installations_update_installation_request_instance.to_dict()
# create an instance of WordPressV1InstallationsUpdateInstallationRequest from a dict
word_press_v1_installations_update_installation_request_from_dict = WordPressV1InstallationsUpdateInstallationRequest.from_dict(word_press_v1_installations_update_installation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


