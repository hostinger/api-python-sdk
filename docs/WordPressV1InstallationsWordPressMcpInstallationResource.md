# WordPressV1InstallationsWordPressMcpInstallationResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | WordPress installation (software) id | [optional] 
**username** | **str** | Hosting account username | [optional] 
**domain** | **str** | Domain the installation belongs to | [optional] 
**directory** | **str** | Installation directory on the server | [optional] 
**mcp_details** | [**WordPressV1InstallationsWordPressMcpDetailsResource**](WordPressV1InstallationsWordPressMcpDetailsResource.md) |  | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_installations_word_press_mcp_installation_resource import WordPressV1InstallationsWordPressMcpInstallationResource

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1InstallationsWordPressMcpInstallationResource from a JSON string
word_press_v1_installations_word_press_mcp_installation_resource_instance = WordPressV1InstallationsWordPressMcpInstallationResource.from_json(json)
# print the JSON string representation of the object
print(WordPressV1InstallationsWordPressMcpInstallationResource.to_json())

# convert the object into a dict
word_press_v1_installations_word_press_mcp_installation_resource_dict = word_press_v1_installations_word_press_mcp_installation_resource_instance.to_dict()
# create an instance of WordPressV1InstallationsWordPressMcpInstallationResource from a dict
word_press_v1_installations_word_press_mcp_installation_resource_from_dict = WordPressV1InstallationsWordPressMcpInstallationResource.from_dict(word_press_v1_installations_word_press_mcp_installation_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


