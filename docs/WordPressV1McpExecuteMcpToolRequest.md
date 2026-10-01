# WordPressV1McpExecuteMcpToolRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_name** | **str** | Tool name as returned by the List MCP tools endpoint. | 
**parameters** | **Dict[str, object]** | Tool input matching the input schema returned by the Show MCP tool info endpoint. | [optional] 
**server** | **str** | MCP server exposing the tool. Defaults to the mcp-adapter default server. | [optional] 

## Example

```python
from hostinger_api.models.word_press_v1_mcp_execute_mcp_tool_request import WordPressV1McpExecuteMcpToolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WordPressV1McpExecuteMcpToolRequest from a JSON string
word_press_v1_mcp_execute_mcp_tool_request_instance = WordPressV1McpExecuteMcpToolRequest.from_json(json)
# print the JSON string representation of the object
print(WordPressV1McpExecuteMcpToolRequest.to_json())

# convert the object into a dict
word_press_v1_mcp_execute_mcp_tool_request_dict = word_press_v1_mcp_execute_mcp_tool_request_instance.to_dict()
# create an instance of WordPressV1McpExecuteMcpToolRequest from a dict
word_press_v1_mcp_execute_mcp_tool_request_from_dict = WordPressV1McpExecuteMcpToolRequest.from_dict(word_press_v1_mcp_execute_mcp_tool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


