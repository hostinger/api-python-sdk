# ReachV1ContactsSegmentsStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**conditions** | [**List[ReachV1ContactsSegmentsStoreRequestConditionsInner]**](ReachV1ContactsSegmentsStoreRequestConditionsInner.md) |  | 
**logic** | **str** |  | 

## Example

```python
from hostinger_api.models.reach_v1_contacts_segments_store_request import ReachV1ContactsSegmentsStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsSegmentsStoreRequest from a JSON string
reach_v1_contacts_segments_store_request_instance = ReachV1ContactsSegmentsStoreRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsSegmentsStoreRequest.to_json())

# convert the object into a dict
reach_v1_contacts_segments_store_request_dict = reach_v1_contacts_segments_store_request_instance.to_dict()
# create an instance of ReachV1ContactsSegmentsStoreRequest from a dict
reach_v1_contacts_segments_store_request_from_dict = ReachV1ContactsSegmentsStoreRequest.from_dict(reach_v1_contacts_segments_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


