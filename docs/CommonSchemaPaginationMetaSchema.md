# CommonSchemaPaginationMetaSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from hostinger_api.models.common_schema_pagination_meta_schema import CommonSchemaPaginationMetaSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CommonSchemaPaginationMetaSchema from a JSON string
common_schema_pagination_meta_schema_instance = CommonSchemaPaginationMetaSchema.from_json(json)
# print the JSON string representation of the object
print(CommonSchemaPaginationMetaSchema.to_json())

# convert the object into a dict
common_schema_pagination_meta_schema_dict = common_schema_pagination_meta_schema_instance.to_dict()
# create an instance of CommonSchemaPaginationMetaSchema from a dict
common_schema_pagination_meta_schema_from_dict = CommonSchemaPaginationMetaSchema.from_dict(common_schema_pagination_meta_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


