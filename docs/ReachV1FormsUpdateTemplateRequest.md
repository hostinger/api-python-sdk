# ReachV1FormsUpdateTemplateRequest

Save the design of a form

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | HTML of the form design. After sanitizing it must still contain a form container (&#x60;data-reach-form&#x60;), an email input (&#x60;data-reach-field&#x3D;\&quot;email\&quot;&#x60;) and a submit button (&#x60;data-reach-submit&#x60;). | 

## Example

```python
from hostinger_api.models.reach_v1_forms_update_template_request import ReachV1FormsUpdateTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1FormsUpdateTemplateRequest from a JSON string
reach_v1_forms_update_template_request_instance = ReachV1FormsUpdateTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1FormsUpdateTemplateRequest.to_json())

# convert the object into a dict
reach_v1_forms_update_template_request_dict = reach_v1_forms_update_template_request_instance.to_dict()
# create an instance of ReachV1FormsUpdateTemplateRequest from a dict
reach_v1_forms_update_template_request_from_dict = ReachV1FormsUpdateTemplateRequest.from_dict(reach_v1_forms_update_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


