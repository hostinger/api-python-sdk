# ReachV1FormsFormTagResource

A tag applied to every contact this form captures.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**type** | **str** | How the tag came about. &#x60;custom&#x60; covers the tags you create yourself, &#x60;import&#x60; the ones added by contact imports, and &#x60;form&#x60; and &#x60;system&#x60; the ones Reach creates on its own. Every form gets a &#x60;form:{name}&#x60; tag when it is created. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_forms_form_tag_resource import ReachV1FormsFormTagResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1FormsFormTagResource from a JSON string
reach_v1_forms_form_tag_resource_instance = ReachV1FormsFormTagResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1FormsFormTagResource.to_json())

# convert the object into a dict
reach_v1_forms_form_tag_resource_dict = reach_v1_forms_form_tag_resource_instance.to_dict()
# create an instance of ReachV1FormsFormTagResource from a dict
reach_v1_forms_form_tag_resource_from_dict = ReachV1FormsFormTagResource.from_dict(reach_v1_forms_form_tag_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


