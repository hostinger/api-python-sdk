# ReachV1ContactsTagsUpdateRequest

Rename a tag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | New tag name | 

## Example

```python
from hostinger_api.models.reach_v1_contacts_tags_update_request import ReachV1ContactsTagsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsTagsUpdateRequest from a JSON string
reach_v1_contacts_tags_update_request_instance = ReachV1ContactsTagsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsTagsUpdateRequest.to_json())

# convert the object into a dict
reach_v1_contacts_tags_update_request_dict = reach_v1_contacts_tags_update_request_instance.to_dict()
# create an instance of ReachV1ContactsTagsUpdateRequest from a dict
reach_v1_contacts_tags_update_request_from_dict = ReachV1ContactsTagsUpdateRequest.from_dict(reach_v1_contacts_tags_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


