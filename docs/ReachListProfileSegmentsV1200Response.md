# ReachListProfileSegmentsV1200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReachV1ContactsSegmentsSegmentListItemResource]**](ReachV1ContactsSegmentsSegmentListItemResource.md) | Array of [&#x60;Reach.V1.Contacts.Segments.SegmentListItemResource&#x60;](#model/reachv1contactssegmentssegmentlistitemresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.reach_list_profile_segments_v1200_response import ReachListProfileSegmentsV1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReachListProfileSegmentsV1200Response from a JSON string
reach_list_profile_segments_v1200_response_instance = ReachListProfileSegmentsV1200Response.from_json(json)
# print the JSON string representation of the object
print(ReachListProfileSegmentsV1200Response.to_json())

# convert the object into a dict
reach_list_profile_segments_v1200_response_dict = reach_list_profile_segments_v1200_response_instance.to_dict()
# create an instance of ReachListProfileSegmentsV1200Response from a dict
reach_list_profile_segments_v1200_response_from_dict = ReachListProfileSegmentsV1200Response.from_dict(reach_list_profile_segments_v1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


