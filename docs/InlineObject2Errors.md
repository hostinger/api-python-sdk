# InlineObject2Errors

Object of detailed errors for each field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_1** | **List[object]** |  | [optional] 
**field_2** | **List[object]** |  | [optional] 

## Example

```python
from hostinger_api.models.inline_object2_errors import InlineObject2Errors

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject2Errors from a JSON string
inline_object2_errors_instance = InlineObject2Errors.from_json(json)
# print the JSON string representation of the object
print(InlineObject2Errors.to_json())

# convert the object into a dict
inline_object2_errors_dict = inline_object2_errors_instance.to_dict()
# create an instance of InlineObject2Errors from a dict
inline_object2_errors_from_dict = InlineObject2Errors.from_dict(inline_object2_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


