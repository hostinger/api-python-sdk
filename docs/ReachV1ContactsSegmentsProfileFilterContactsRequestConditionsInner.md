# ReachV1ContactsSegmentsProfileFilterContactsRequestConditionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | A built-in contact attribute, or &#x60;cf:{fieldUuid}&#x60; to target a custom contact field. Which operators are accepted depends on the attribute, so read the segment filter attributes endpoint for the authoritative list. | 
**operator** | **str** |  | 
**value** | **str** | Always a string, including for numeric and date comparisons | 

## Example

```python
from hostinger_api.models.reach_v1_contacts_segments_profile_filter_contacts_request_conditions_inner import ReachV1ContactsSegmentsProfileFilterContactsRequestConditionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsSegmentsProfileFilterContactsRequestConditionsInner from a JSON string
reach_v1_contacts_segments_profile_filter_contacts_request_conditions_inner_instance = ReachV1ContactsSegmentsProfileFilterContactsRequestConditionsInner.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsSegmentsProfileFilterContactsRequestConditionsInner.to_json())

# convert the object into a dict
reach_v1_contacts_segments_profile_filter_contacts_request_conditions_inner_dict = reach_v1_contacts_segments_profile_filter_contacts_request_conditions_inner_instance.to_dict()
# create an instance of ReachV1ContactsSegmentsProfileFilterContactsRequestConditionsInner from a dict
reach_v1_contacts_segments_profile_filter_contacts_request_conditions_inner_from_dict = ReachV1ContactsSegmentsProfileFilterContactsRequestConditionsInner.from_dict(reach_v1_contacts_segments_profile_filter_contacts_request_conditions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


