# ReachV1FormsFormResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** | A &#x60;paused&#x60; form keeps its template online but stops accepting submissions. | [optional] 
**type** | **str** |  | [optional] 
**template** | [**ReachV1FormsFormTemplateResource**](ReachV1FormsFormTemplateResource.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_forms_form_resource import ReachV1FormsFormResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1FormsFormResource from a JSON string
reach_v1_forms_form_resource_instance = ReachV1FormsFormResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1FormsFormResource.to_json())

# convert the object into a dict
reach_v1_forms_form_resource_dict = reach_v1_forms_form_resource_instance.to_dict()
# create an instance of ReachV1FormsFormResource from a dict
reach_v1_forms_form_resource_from_dict = ReachV1FormsFormResource.from_dict(reach_v1_forms_form_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


