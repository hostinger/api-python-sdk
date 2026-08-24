# ReachV1ContactsSegmentsProfileFilterContactsRequest

Conditions to preview, in the same shape accepted when creating a segment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[ReachV1ContactsSegmentsProfileFilterContactsRequestConditionsInner]**](ReachV1ContactsSegmentsProfileFilterContactsRequestConditionsInner.md) | Conditions a contact must satisfy to appear in the preview | 
**logic** | **str** | How to combine multiple conditions | 
**page** | **int** | Page number | [optional] 
**per_page** | **int** | Number of items per page | [optional] 
**search** | **str** | Narrow the preview to contacts whose email matches | [optional] 
**sort_by** | **str** |  | [optional] 
**sort_direction** | **str** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_segments_profile_filter_contacts_request import ReachV1ContactsSegmentsProfileFilterContactsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsSegmentsProfileFilterContactsRequest from a JSON string
reach_v1_contacts_segments_profile_filter_contacts_request_instance = ReachV1ContactsSegmentsProfileFilterContactsRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsSegmentsProfileFilterContactsRequest.to_json())

# convert the object into a dict
reach_v1_contacts_segments_profile_filter_contacts_request_dict = reach_v1_contacts_segments_profile_filter_contacts_request_instance.to_dict()
# create an instance of ReachV1ContactsSegmentsProfileFilterContactsRequest from a dict
reach_v1_contacts_segments_profile_filter_contacts_request_from_dict = ReachV1ContactsSegmentsProfileFilterContactsRequest.from_dict(reach_v1_contacts_segments_profile_filter_contacts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


