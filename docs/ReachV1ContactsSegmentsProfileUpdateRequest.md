# ReachV1ContactsSegmentsProfileUpdateRequest

Rename a segment and/or replace the conditions that define it

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**conditions** | [**List[ReachV1ContactsSegmentsProfileStoreRequestConditionsInner]**](ReachV1ContactsSegmentsProfileStoreRequestConditionsInner.md) | Replaces the existing conditions entirely. Omit to keep the current ones. | [optional] 
**logic** | **str** | How to combine multiple conditions. Required when conditions are given. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_segments_profile_update_request import ReachV1ContactsSegmentsProfileUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsSegmentsProfileUpdateRequest from a JSON string
reach_v1_contacts_segments_profile_update_request_instance = ReachV1ContactsSegmentsProfileUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsSegmentsProfileUpdateRequest.to_json())

# convert the object into a dict
reach_v1_contacts_segments_profile_update_request_dict = reach_v1_contacts_segments_profile_update_request_instance.to_dict()
# create an instance of ReachV1ContactsSegmentsProfileUpdateRequest from a dict
reach_v1_contacts_segments_profile_update_request_from_dict = ReachV1ContactsSegmentsProfileUpdateRequest.from_dict(reach_v1_contacts_segments_profile_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


