# WordPressV1InstallationsJwtTokenResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Signed JWT used to authenticate requests against the WordPress installation | [optional] 
**expires_in** | **int** | Token lifetime in seconds from the moment it was issued | [optional] 
**expires_at** | **datetime** | Date-time at which the token expires, or null when not provided | [optional] 
**mcp_url** | **str** | MCP (Model Context Protocol) endpoint URL for the WordPress installation, or null when not provided | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_installations_jwt_token_resource import WordPressV1InstallationsJwtTokenResource

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1InstallationsJwtTokenResource from a JSON string
word_press_v1_installations_jwt_token_resource_instance = WordPressV1InstallationsJwtTokenResource.from_json(json)
# print the JSON string representation of the object
print(WordPressV1InstallationsJwtTokenResource.to_json())

# convert the object into a dict
word_press_v1_installations_jwt_token_resource_dict = word_press_v1_installations_jwt_token_resource_instance.to_dict()
# create an instance of WordPressV1InstallationsJwtTokenResource from a dict
word_press_v1_installations_jwt_token_resource_from_dict = WordPressV1InstallationsJwtTokenResource.from_dict(word_press_v1_installations_jwt_token_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


