# ReachV1ContactsSegmentsStoreRequestConditionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** |  | [optional] 
**value** | [**ReachV1ContactsSegmentsStoreRequestConditionsInnerValue**](ReachV1ContactsSegmentsStoreRequestConditionsInnerValue.md) |  | [optional] 
**attribute** | **str** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_segments_store_request_conditions_inner import ReachV1ContactsSegmentsStoreRequestConditionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsSegmentsStoreRequestConditionsInner from a JSON string
reach_v1_contacts_segments_store_request_conditions_inner_instance = ReachV1ContactsSegmentsStoreRequestConditionsInner.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsSegmentsStoreRequestConditionsInner.to_json())

# convert the object into a dict
reach_v1_contacts_segments_store_request_conditions_inner_dict = reach_v1_contacts_segments_store_request_conditions_inner_instance.to_dict()
# create an instance of ReachV1ContactsSegmentsStoreRequestConditionsInner from a dict
reach_v1_contacts_segments_store_request_conditions_inner_from_dict = ReachV1ContactsSegmentsStoreRequestConditionsInner.from_dict(reach_v1_contacts_segments_store_request_conditions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


