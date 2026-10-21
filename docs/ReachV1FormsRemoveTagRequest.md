# ReachV1FormsRemoveTagRequest

Tag the form stops applying to future submitters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_uuid** | **str** |  | 

## Example

```python
from hostinger_api.models.reach_v1_forms_remove_tag_request import ReachV1FormsRemoveTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1FormsRemoveTagRequest from a JSON string
reach_v1_forms_remove_tag_request_instance = ReachV1FormsRemoveTagRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1FormsRemoveTagRequest.to_json())

# convert the object into a dict
reach_v1_forms_remove_tag_request_dict = reach_v1_forms_remove_tag_request_instance.to_dict()
# create an instance of ReachV1FormsRemoveTagRequest from a dict
reach_v1_forms_remove_tag_request_from_dict = ReachV1FormsRemoveTagRequest.from_dict(reach_v1_forms_remove_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


