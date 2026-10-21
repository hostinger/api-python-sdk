# ReachV1FormsUpdateRequest

Rename a form and/or change its status. Send at least one field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Form name. Letters, digits, spaces and - . &#39; _ only. | [optional] 
**status** | **str** | &#x60;active&#x60; takes the form live, &#x60;paused&#x60; and &#x60;draft&#x60; stop it accepting submissions. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_forms_update_request import ReachV1FormsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1FormsUpdateRequest from a JSON string
reach_v1_forms_update_request_instance = ReachV1FormsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1FormsUpdateRequest.to_json())

# convert the object into a dict
reach_v1_forms_update_request_dict = reach_v1_forms_update_request_instance.to_dict()
# create an instance of ReachV1FormsUpdateRequest from a dict
reach_v1_forms_update_request_from_dict = ReachV1FormsUpdateRequest.from_dict(reach_v1_forms_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


