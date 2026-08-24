# ReachV1ContactsSegmentsSegmentFilterOperatorResource

One operator an attribute accepts, and the value format it expects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** | Value to send as the condition &#x60;operator&#x60;. | [optional] 
**description** | **str** |  | [optional] 
**input_type** | **str** | Shape of the value this operator expects, useful for rendering an input. | [optional] 
**example** | **str** | An example value in the format this operator expects. | [optional] 
**enum_values** | **Dict[str, str]** | The values this operator accepts, keyed by the value to send. Only present when the operator is constrained to a fixed set, such as a tag or campaign picker. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_segments_segment_filter_operator_resource import ReachV1ContactsSegmentsSegmentFilterOperatorResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsSegmentsSegmentFilterOperatorResource from a JSON string
reach_v1_contacts_segments_segment_filter_operator_resource_instance = ReachV1ContactsSegmentsSegmentFilterOperatorResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsSegmentsSegmentFilterOperatorResource.to_json())

# convert the object into a dict
reach_v1_contacts_segments_segment_filter_operator_resource_dict = reach_v1_contacts_segments_segment_filter_operator_resource_instance.to_dict()
# create an instance of ReachV1ContactsSegmentsSegmentFilterOperatorResource from a dict
reach_v1_contacts_segments_segment_filter_operator_resource_from_dict = ReachV1ContactsSegmentsSegmentFilterOperatorResource.from_dict(reach_v1_contacts_segments_segment_filter_operator_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


