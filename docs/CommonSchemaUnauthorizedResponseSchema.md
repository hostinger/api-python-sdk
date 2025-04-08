# CommonSchemaUnauthorizedResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 

## Example

```python
from hostinger-api.models.common_schema_unauthorized_response_schema import CommonSchemaUnauthorizedResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CommonSchemaUnauthorizedResponseSchema from a JSON string
common_schema_unauthorized_response_schema_instance = CommonSchemaUnauthorizedResponseSchema.from_json(json)
# print the JSON string representation of the object
print(CommonSchemaUnauthorizedResponseSchema.to_json())

# convert the object into a dict
common_schema_unauthorized_response_schema_dict = common_schema_unauthorized_response_schema_instance.to_dict()
# create an instance of CommonSchemaUnauthorizedResponseSchema from a dict
common_schema_unauthorized_response_schema_from_dict = CommonSchemaUnauthorizedResponseSchema.from_dict(common_schema_unauthorized_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


