# WordPressV1InstallationsUpdateResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Available WordPress core version | [optional] 
**type** | **str** | Update type | [optional] 
**url** | **str** | Download URL for the update package | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_installations_update_resource import WordPressV1InstallationsUpdateResource

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1InstallationsUpdateResource from a JSON string
word_press_v1_installations_update_resource_instance = WordPressV1InstallationsUpdateResource.from_json(json)
# print the JSON string representation of the object
print(WordPressV1InstallationsUpdateResource.to_json())

# convert the object into a dict
word_press_v1_installations_update_resource_dict = word_press_v1_installations_update_resource_instance.to_dict()
# create an instance of WordPressV1InstallationsUpdateResource from a dict
word_press_v1_installations_update_resource_from_dict = WordPressV1InstallationsUpdateResource.from_dict(word_press_v1_installations_update_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


