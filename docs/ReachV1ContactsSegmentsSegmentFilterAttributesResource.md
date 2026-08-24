# ReachV1ContactsSegmentsSegmentFilterAttributesResource

The vocabulary a segment condition can be built from, for one profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Dict[str, ReachV1ContactsSegmentsSegmentFilterAttributeResource]**](ReachV1ContactsSegmentsSegmentFilterAttributeResource.md) | Every attribute a condition can filter on, keyed by the value to send as &#x60;attribute&#x60;. Custom contact fields are keyed &#x60;cf:{fieldUuid}&#x60;, tags and campaigns by their uuid, so the keys are not a fixed list and should be read from this response rather than hardcoded. | [optional] 
**logic_operators** | **Dict[str, str]** | The values accepted by &#x60;logic&#x60; when a segment combines several conditions. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_segments_segment_filter_attributes_resource import ReachV1ContactsSegmentsSegmentFilterAttributesResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsSegmentsSegmentFilterAttributesResource from a JSON string
reach_v1_contacts_segments_segment_filter_attributes_resource_instance = ReachV1ContactsSegmentsSegmentFilterAttributesResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsSegmentsSegmentFilterAttributesResource.to_json())

# convert the object into a dict
reach_v1_contacts_segments_segment_filter_attributes_resource_dict = reach_v1_contacts_segments_segment_filter_attributes_resource_instance.to_dict()
# create an instance of ReachV1ContactsSegmentsSegmentFilterAttributesResource from a dict
reach_v1_contacts_segments_segment_filter_attributes_resource_from_dict = ReachV1ContactsSegmentsSegmentFilterAttributesResource.from_dict(reach_v1_contacts_segments_segment_filter_attributes_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


