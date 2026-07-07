# WordPressV1InstallationsVersionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Installed WordPress core version | [optional] 
**vulnerabilities** | [**List[WordPressV1CommonVulnerabilityResource]**](WordPressV1CommonVulnerabilityResource.md) | Known vulnerabilities affecting the installed core version | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_installations_version_resource import WordPressV1InstallationsVersionResource

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1InstallationsVersionResource from a JSON string
word_press_v1_installations_version_resource_instance = WordPressV1InstallationsVersionResource.from_json(json)
# print the JSON string representation of the object
print(WordPressV1InstallationsVersionResource.to_json())

# convert the object into a dict
word_press_v1_installations_version_resource_dict = word_press_v1_installations_version_resource_instance.to_dict()
# create an instance of WordPressV1InstallationsVersionResource from a dict
word_press_v1_installations_version_resource_from_dict = WordPressV1InstallationsVersionResource.from_dict(word_press_v1_installations_version_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


