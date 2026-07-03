# WordPressV1InstallationsWordPressInstallationResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | WordPress installation (software) id | [optional] 
**username** | **str** | Hosting account username | [optional] 
**domain** | **str** | Domain the installation belongs to | [optional] 
**site_title** | **str** | WordPress site title | [optional] 
**url** | **str** | WordPress site URL | [optional] 
**directory** | **str** | Installation directory | [optional] 
**language** | **str** | WordPress locale | [optional] 
**login** | **str** | WordPress admin username | [optional] 
**email** | **str** | WordPress admin email | [optional] 
**is_valid** | **bool** | Whether the installation is considered valid | [optional] 
**validation_error** | **str** | Reason the installation is invalid, if any | [optional] 
**created_at** | **datetime** | Installation creation timestamp | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_installations_word_press_installation_resource import WordPressV1InstallationsWordPressInstallationResource

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1InstallationsWordPressInstallationResource from a JSON string
word_press_v1_installations_word_press_installation_resource_instance = WordPressV1InstallationsWordPressInstallationResource.from_json(json)
# print the JSON string representation of the object
print(WordPressV1InstallationsWordPressInstallationResource.to_json())

# convert the object into a dict
word_press_v1_installations_word_press_installation_resource_dict = word_press_v1_installations_word_press_installation_resource_instance.to_dict()
# create an instance of WordPressV1InstallationsWordPressInstallationResource from a dict
word_press_v1_installations_word_press_installation_resource_from_dict = WordPressV1InstallationsWordPressInstallationResource.from_dict(word_press_v1_installations_word_press_installation_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


