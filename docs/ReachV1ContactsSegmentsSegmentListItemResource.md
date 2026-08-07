# ReachV1ContactsSegmentsSegmentListItemResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**contacts_count** | **int** | Contacts currently matching the segment conditions | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_segments_segment_list_item_resource import ReachV1ContactsSegmentsSegmentListItemResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsSegmentsSegmentListItemResource from a JSON string
reach_v1_contacts_segments_segment_list_item_resource_instance = ReachV1ContactsSegmentsSegmentListItemResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsSegmentsSegmentListItemResource.to_json())

# convert the object into a dict
reach_v1_contacts_segments_segment_list_item_resource_dict = reach_v1_contacts_segments_segment_list_item_resource_instance.to_dict()
# create an instance of ReachV1ContactsSegmentsSegmentListItemResource from a dict
reach_v1_contacts_segments_segment_list_item_resource_from_dict = ReachV1ContactsSegmentsSegmentListItemResource.from_dict(reach_v1_contacts_segments_segment_list_item_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


