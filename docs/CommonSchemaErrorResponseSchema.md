# CommonSchemaErrorResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 

## Example

```python
from @hostinger/api.models.common_schema_error_response_schema import CommonSchemaErrorResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CommonSchemaErrorResponseSchema from a JSON string
common_schema_error_response_schema_instance = CommonSchemaErrorResponseSchema.from_json(json)
# print the JSON string representation of the object
print(CommonSchemaErrorResponseSchema.to_json())

# convert the object into a dict
common_schema_error_response_schema_dict = common_schema_error_response_schema_instance.to_dict()
# create an instance of CommonSchemaErrorResponseSchema from a dict
common_schema_error_response_schema_from_dict = CommonSchemaErrorResponseSchema.from_dict(common_schema_error_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


