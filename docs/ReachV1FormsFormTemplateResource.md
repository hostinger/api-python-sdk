# ReachV1FormsFormTemplateResource

The rendered form template. Both fields stay null until the template has been generated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**path** | **str** | Storage path of the template HTML, relative to the storage directory of this profile. Get the form details to receive a directly usable URL instead. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_forms_form_template_resource import ReachV1FormsFormTemplateResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1FormsFormTemplateResource from a JSON string
reach_v1_forms_form_template_resource_instance = ReachV1FormsFormTemplateResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1FormsFormTemplateResource.to_json())

# convert the object into a dict
reach_v1_forms_form_template_resource_dict = reach_v1_forms_form_template_resource_instance.to_dict()
# create an instance of ReachV1FormsFormTemplateResource from a dict
reach_v1_forms_form_template_resource_from_dict = ReachV1FormsFormTemplateResource.from_dict(reach_v1_forms_form_template_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


