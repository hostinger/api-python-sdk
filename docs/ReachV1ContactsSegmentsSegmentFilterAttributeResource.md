# ReachV1ContactsSegmentsSegmentFilterAttributeResource

One attribute a segment condition can filter on.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Value to send as the condition &#x60;attribute&#x60;. | [optional] 
**type** | **str** | Where the attribute is sourced from. | [optional] 
**description** | **str** |  | [optional] 
**operators** | [**Dict[str, ReachV1ContactsSegmentsSegmentFilterOperatorResource]**](ReachV1ContactsSegmentsSegmentFilterOperatorResource.md) | Operators this attribute accepts, keyed by operator name. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_segments_segment_filter_attribute_resource import ReachV1ContactsSegmentsSegmentFilterAttributeResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsSegmentsSegmentFilterAttributeResource from a JSON string
reach_v1_contacts_segments_segment_filter_attribute_resource_instance = ReachV1ContactsSegmentsSegmentFilterAttributeResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsSegmentsSegmentFilterAttributeResource.to_json())

# convert the object into a dict
reach_v1_contacts_segments_segment_filter_attribute_resource_dict = reach_v1_contacts_segments_segment_filter_attribute_resource_instance.to_dict()
# create an instance of ReachV1ContactsSegmentsSegmentFilterAttributeResource from a dict
reach_v1_contacts_segments_segment_filter_attribute_resource_from_dict = ReachV1ContactsSegmentsSegmentFilterAttributeResource.from_dict(reach_v1_contacts_segments_segment_filter_attribute_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


