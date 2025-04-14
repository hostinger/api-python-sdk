# CommonSchemaUnprocessableContentResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Validation error message | [optional] 
**errors** | [**CommonSchemaUnprocessableContentResponseSchemaErrors**](CommonSchemaUnprocessableContentResponseSchemaErrors.md) |  | [optional] 
**correlation_id** | **str** |  | [optional] 

## Example

```python
from hostinger_api.models.common_schema_unprocessable_content_response_schema import CommonSchemaUnprocessableContentResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CommonSchemaUnprocessableContentResponseSchema from a JSON string
common_schema_unprocessable_content_response_schema_instance = CommonSchemaUnprocessableContentResponseSchema.from_json(json)
# print the JSON string representation of the object
print(CommonSchemaUnprocessableContentResponseSchema.to_json())

# convert the object into a dict
common_schema_unprocessable_content_response_schema_dict = common_schema_unprocessable_content_response_schema_instance.to_dict()
# create an instance of CommonSchemaUnprocessableContentResponseSchema from a dict
common_schema_unprocessable_content_response_schema_from_dict = CommonSchemaUnprocessableContentResponseSchema.from_dict(common_schema_unprocessable_content_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


