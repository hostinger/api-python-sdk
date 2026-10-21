# ReachV1FormsAssignTagsRequest

Tags every future submitter of the form receives

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_uuids** | **List[str]** |  | 

## Example

```python
from hostinger_api.models.reach_v1_forms_assign_tags_request import ReachV1FormsAssignTagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1FormsAssignTagsRequest from a JSON string
reach_v1_forms_assign_tags_request_instance = ReachV1FormsAssignTagsRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1FormsAssignTagsRequest.to_json())

# convert the object into a dict
reach_v1_forms_assign_tags_request_dict = reach_v1_forms_assign_tags_request_instance.to_dict()
# create an instance of ReachV1FormsAssignTagsRequest from a dict
reach_v1_forms_assign_tags_request_from_dict = ReachV1FormsAssignTagsRequest.from_dict(reach_v1_forms_assign_tags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


