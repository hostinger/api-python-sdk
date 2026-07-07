# VPSV1ActionListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VPSV1ActionActionResource]**](VPSV1ActionActionResource.md) | Array of [&#x60;VPS.V1.Action.ActionResource&#x60;](#model/vpsv1actionactionresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_action_list_response import VPSV1ActionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1ActionListResponse from a JSON string
vpsv1_action_list_response_instance = VPSV1ActionListResponse.from_json(json)
# print the JSON string representation of the object
print(VPSV1ActionListResponse.to_json())

# convert the object into a dict
vpsv1_action_list_response_dict = vpsv1_action_list_response_instance.to_dict()
# create an instance of VPSV1ActionListResponse from a dict
vpsv1_action_list_response_from_dict = VPSV1ActionListResponse.from_dict(vpsv1_action_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


