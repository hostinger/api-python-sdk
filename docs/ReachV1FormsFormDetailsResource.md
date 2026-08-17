# ReachV1FormsFormDetailsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** | A &#x60;paused&#x60; form keeps its template online but stops accepting submissions. | [optional] 
**type** | **str** |  | [optional] 
**template** | [**ReachV1FormsFormTemplateDetailsResource**](ReachV1FormsFormTemplateDetailsResource.md) |  | [optional] 
**tags** | [**List[ReachV1FormsFormTagResource]**](ReachV1FormsFormTagResource.md) | Tags applied to every contact this form captures. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_forms_form_details_resource import ReachV1FormsFormDetailsResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1FormsFormDetailsResource from a JSON string
reach_v1_forms_form_details_resource_instance = ReachV1FormsFormDetailsResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1FormsFormDetailsResource.to_json())

# convert the object into a dict
reach_v1_forms_form_details_resource_dict = reach_v1_forms_form_details_resource_instance.to_dict()
# create an instance of ReachV1FormsFormDetailsResource from a dict
reach_v1_forms_form_details_resource_from_dict = ReachV1FormsFormDetailsResource.from_dict(reach_v1_forms_form_details_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


