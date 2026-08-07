# ReachV1ContactsSegmentsProfileStoreRequest

Create a segment from a set of conditions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**conditions** | [**List[ReachV1ContactsSegmentsProfileStoreRequestConditionsInner]**](ReachV1ContactsSegmentsProfileStoreRequestConditionsInner.md) | Conditions a contact must satisfy to fall into the segment | 
**logic** | **str** | How to combine multiple conditions | 

## Example

```python
from hostinger_api.models.reach_v1_contacts_segments_profile_store_request import ReachV1ContactsSegmentsProfileStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsSegmentsProfileStoreRequest from a JSON string
reach_v1_contacts_segments_profile_store_request_instance = ReachV1ContactsSegmentsProfileStoreRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsSegmentsProfileStoreRequest.to_json())

# convert the object into a dict
reach_v1_contacts_segments_profile_store_request_dict = reach_v1_contacts_segments_profile_store_request_instance.to_dict()
# create an instance of ReachV1ContactsSegmentsProfileStoreRequest from a dict
reach_v1_contacts_segments_profile_store_request_from_dict = ReachV1ContactsSegmentsProfileStoreRequest.from_dict(reach_v1_contacts_segments_profile_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


