# VPSV1ActionActionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Action ID | [optional] 
**name** | **str** | Action name | [optional] 
**state** | **str** | Action state | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger-api.models.vpsv1_action_action_resource import VPSV1ActionActionResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1ActionActionResource from a JSON string
vpsv1_action_action_resource_instance = VPSV1ActionActionResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1ActionActionResource.to_json())

# convert the object into a dict
vpsv1_action_action_resource_dict = vpsv1_action_action_resource_instance.to_dict()
# create an instance of VPSV1ActionActionResource from a dict
vpsv1_action_action_resource_from_dict = VPSV1ActionActionResource.from_dict(vpsv1_action_action_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


