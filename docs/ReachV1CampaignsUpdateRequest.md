# ReachV1CampaignsUpdateRequest

Update a campaign. Send at least one field; fields left out keep their current value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Name the campaign is listed under. Not shown to the recipients. | [optional] 
**subject** | **str** | Subject line of the email. | [optional] 
**sender_name** | **str** | From name shown to the recipients. | [optional] 
**sender_email** | **str** | From address of the campaign. Its domain has to be verified on the profile before the campaign can be sent. | [optional] 
**template_uuid** | **str** | Template to send, as returned by the template endpoints. | [optional] 
**all_contacts** | **bool** | &#x60;true&#x60; targets every contact of the profile, &#x60;false&#x60; targets only &#x60;segment_uuids&#x60;. Required when &#x60;segment_uuids&#x60; or &#x60;excluded_segment_uuids&#x60; is sent. | [optional] 
**segment_uuids** | **List[str]** | Segments to target. Replaces the segments currently targeted. | [optional] 
**excluded_segment_uuids** | **List[str]** | Segments to leave out. Only allowed together with &#x60;all_contacts: true&#x60;. | [optional] 
**metadata** | [**ReachV1CampaignsStoreRequestMetadata**](ReachV1CampaignsStoreRequestMetadata.md) |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_campaigns_update_request import ReachV1CampaignsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1CampaignsUpdateRequest from a JSON string
reach_v1_campaigns_update_request_instance = ReachV1CampaignsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1CampaignsUpdateRequest.to_json())

# convert the object into a dict
reach_v1_campaigns_update_request_dict = reach_v1_campaigns_update_request_instance.to_dict()
# create an instance of ReachV1CampaignsUpdateRequest from a dict
reach_v1_campaigns_update_request_from_dict = ReachV1CampaignsUpdateRequest.from_dict(reach_v1_campaigns_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


