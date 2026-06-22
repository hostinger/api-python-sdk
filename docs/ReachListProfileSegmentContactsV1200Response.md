# ReachListProfileSegmentContactsV1200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReachV1ContactsSegmentsSegmentationContactResource]**](ReachV1ContactsSegmentsSegmentationContactResource.md) | Array of [&#x60;Reach.V1.Contacts.Segments.SegmentationContactResource&#x60;](#model/reachv1contactssegmentssegmentationcontactresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.reach_list_profile_segment_contacts_v1200_response import ReachListProfileSegmentContactsV1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReachListProfileSegmentContactsV1200Response from a JSON string
reach_list_profile_segment_contacts_v1200_response_instance = ReachListProfileSegmentContactsV1200Response.from_json(json)
# print the JSON string representation of the object
print(ReachListProfileSegmentContactsV1200Response.to_json())

# convert the object into a dict
reach_list_profile_segment_contacts_v1200_response_dict = reach_list_profile_segment_contacts_v1200_response_instance.to_dict()
# create an instance of ReachListProfileSegmentContactsV1200Response from a dict
reach_list_profile_segment_contacts_v1200_response_from_dict = ReachListProfileSegmentContactsV1200Response.from_dict(reach_list_profile_segment_contacts_v1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


