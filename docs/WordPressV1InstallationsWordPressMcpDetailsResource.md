# WordPressV1InstallationsWordPressMcpDetailsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | JWT used to authenticate against the installation MCP server | [optional] 
**mcp_url** | **str** | MCP (Model Context Protocol) endpoint URL for the WordPress installation | [optional] 
**expires_in** | **int** | Token lifetime in seconds from the moment it was issued | [optional] 
**expires_at** | **datetime** | Date-time at which the token expires | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_installations_word_press_mcp_details_resource import WordPressV1InstallationsWordPressMcpDetailsResource

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1InstallationsWordPressMcpDetailsResource from a JSON string
word_press_v1_installations_word_press_mcp_details_resource_instance = WordPressV1InstallationsWordPressMcpDetailsResource.from_json(json)
# print the JSON string representation of the object
print(WordPressV1InstallationsWordPressMcpDetailsResource.to_json())

# convert the object into a dict
word_press_v1_installations_word_press_mcp_details_resource_dict = word_press_v1_installations_word_press_mcp_details_resource_instance.to_dict()
# create an instance of WordPressV1InstallationsWordPressMcpDetailsResource from a dict
word_press_v1_installations_word_press_mcp_details_resource_from_dict = WordPressV1InstallationsWordPressMcpDetailsResource.from_dict(word_press_v1_installations_word_press_mcp_details_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


