# ReachV1CampaignsStoreRequest

Create a campaign in draft status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender_name** | **str** | From name shown to the recipients. | 
**sender_email** | **str** | From address of the campaign. Its domain has to be verified on the profile before the campaign can be sent. | 
**title** | **str** | Name the campaign is listed under. Not shown to the recipients. | [optional] 
**subject** | **str** | Subject line of the email. | [optional] 
**template_uuid** | **str** | Template to send, as returned by the template endpoints. Can be left out and attached later, but the campaign cannot be sent without one. | [optional] 
**metadata** | [**ReachV1CampaignsStoreRequestMetadata**](ReachV1CampaignsStoreRequestMetadata.md) |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_campaigns_store_request import ReachV1CampaignsStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1CampaignsStoreRequest from a JSON string
reach_v1_campaigns_store_request_instance = ReachV1CampaignsStoreRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1CampaignsStoreRequest.to_json())

# convert the object into a dict
reach_v1_campaigns_store_request_dict = reach_v1_campaigns_store_request_instance.to_dict()
# create an instance of ReachV1CampaignsStoreRequest from a dict
reach_v1_campaigns_store_request_from_dict = ReachV1CampaignsStoreRequest.from_dict(reach_v1_campaigns_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


