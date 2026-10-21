# ReachV1FormsFormTemplateVersionResource

The stored version of a saved form design.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**path** | **str** | Storage path of the template HTML, relative to the storage directory of this profile. | [optional] 
**edit_type** | **str** | Whether the design was saved by hand or by the AI builder. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_forms_form_template_version_resource import ReachV1FormsFormTemplateVersionResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1FormsFormTemplateVersionResource from a JSON string
reach_v1_forms_form_template_version_resource_instance = ReachV1FormsFormTemplateVersionResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1FormsFormTemplateVersionResource.to_json())

# convert the object into a dict
reach_v1_forms_form_template_version_resource_dict = reach_v1_forms_form_template_version_resource_instance.to_dict()
# create an instance of ReachV1FormsFormTemplateVersionResource from a dict
reach_v1_forms_form_template_version_resource_from_dict = ReachV1FormsFormTemplateVersionResource.from_dict(reach_v1_forms_form_template_version_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


