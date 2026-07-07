# WordPressV1InstallationsCheckIsValidResultResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**software_id** | **str** | WordPress installation (software) identifier | [optional] 
**is_valid** | **bool** | Whether the WordPress installation is valid and working correctly | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_installations_check_is_valid_result_resource import WordPressV1InstallationsCheckIsValidResultResource

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1InstallationsCheckIsValidResultResource from a JSON string
word_press_v1_installations_check_is_valid_result_resource_instance = WordPressV1InstallationsCheckIsValidResultResource.from_json(json)
# print the JSON string representation of the object
print(WordPressV1InstallationsCheckIsValidResultResource.to_json())

# convert the object into a dict
word_press_v1_installations_check_is_valid_result_resource_dict = word_press_v1_installations_check_is_valid_result_resource_instance.to_dict()
# create an instance of WordPressV1InstallationsCheckIsValidResultResource from a dict
word_press_v1_installations_check_is_valid_result_resource_from_dict = WordPressV1InstallationsCheckIsValidResultResource.from_dict(word_press_v1_installations_check_is_valid_result_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


