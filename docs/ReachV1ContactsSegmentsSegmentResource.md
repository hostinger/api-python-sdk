# ReachV1ContactsSegmentsSegmentResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**query** | **List[object]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_segments_segment_resource import ReachV1ContactsSegmentsSegmentResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsSegmentsSegmentResource from a JSON string
reach_v1_contacts_segments_segment_resource_instance = ReachV1ContactsSegmentsSegmentResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsSegmentsSegmentResource.to_json())

# convert the object into a dict
reach_v1_contacts_segments_segment_resource_dict = reach_v1_contacts_segments_segment_resource_instance.to_dict()
# create an instance of ReachV1ContactsSegmentsSegmentResource from a dict
reach_v1_contacts_segments_segment_resource_from_dict = ReachV1ContactsSegmentsSegmentResource.from_dict(reach_v1_contacts_segments_segment_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


