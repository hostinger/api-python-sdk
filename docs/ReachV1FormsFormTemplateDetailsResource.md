# ReachV1FormsFormTemplateDetailsResource

The rendered form template. There is no ready-made embed snippet - either serve the HTML behind `url` or build your own embed around the form uuid. All fields stay null until the template has been generated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**path** | **str** | Storage path of the template HTML, relative to the storage directory of this profile. &#x60;url&#x60; already includes that prefix, so prefer it unless you resolve storage paths yourself. | [optional] 
**url** | **str** | Publicly reachable URL of the template HTML. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_forms_form_template_details_resource import ReachV1FormsFormTemplateDetailsResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1FormsFormTemplateDetailsResource from a JSON string
reach_v1_forms_form_template_details_resource_instance = ReachV1FormsFormTemplateDetailsResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1FormsFormTemplateDetailsResource.to_json())

# convert the object into a dict
reach_v1_forms_form_template_details_resource_dict = reach_v1_forms_form_template_details_resource_instance.to_dict()
# create an instance of ReachV1FormsFormTemplateDetailsResource from a dict
reach_v1_forms_form_template_details_resource_from_dict = ReachV1FormsFormTemplateDetailsResource.from_dict(reach_v1_forms_form_template_details_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


