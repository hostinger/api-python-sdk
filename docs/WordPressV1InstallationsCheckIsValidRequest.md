# WordPressV1InstallationsCheckIsValidRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**software_ids** | **List[str]** | WordPress installation (software) identifiers to validate. | 
**force** | **bool** | Force fresh validation without cache. Preferable for troubleshooting purposes. | [optional] [default to False]

## Example

```python
from hostinger_api.models.word_press_v1_installations_check_is_valid_request import WordPressV1InstallationsCheckIsValidRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1InstallationsCheckIsValidRequest from a JSON string
word_press_v1_installations_check_is_valid_request_instance = WordPressV1InstallationsCheckIsValidRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1InstallationsCheckIsValidRequest.to_json())

# convert the object into a dict
word_press_v1_installations_check_is_valid_request_dict = word_press_v1_installations_check_is_valid_request_instance.to_dict()
# create an instance of WordPressV1InstallationsCheckIsValidRequest from a dict
word_press_v1_installations_check_is_valid_request_from_dict = WordPressV1InstallationsCheckIsValidRequest.from_dict(word_press_v1_installations_check_is_valid_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


