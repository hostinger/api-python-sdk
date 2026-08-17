# ReachV1CampaignsCampaignDetailsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**sender_name** | **str** |  | [optional] 
**sender_email** | **str** |  | [optional] 
**template_uuid** | **str** | The email template this campaign uses. The template title is not exposed. | [optional] 
**status** | **str** | A fully sent campaign is &#x60;publish&#x60;. There is no &#x60;sent&#x60;, &#x60;paused&#x60; or &#x60;archived&#x60; status. | [optional] 
**type** | **str** |  | [optional] 
**failure_reason** | **str** | Set only while the status is &#x60;failed&#x60;. | [optional] 
**is_smart_send** | **bool** | Whether delivery time is picked per contact rather than sent to everyone at once. | [optional] 
**is_all_contacts** | **bool** | Whether the campaign targets every contact instead of the listed segments. | [optional] 
**delivery** | [**ReachV1CampaignsCampaignDeliveryResource**](ReachV1CampaignsCampaignDeliveryResource.md) |  | [optional] 
**segment_uuids** | **List[str]** | Segments this campaign targets. Empty when it targets all contacts. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**sent_at** | **datetime** |  | [optional] 
**scheduled_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_campaigns_campaign_details_resource import ReachV1CampaignsCampaignDetailsResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1CampaignsCampaignDetailsResource from a JSON string
reach_v1_campaigns_campaign_details_resource_instance = ReachV1CampaignsCampaignDetailsResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1CampaignsCampaignDetailsResource.to_json())

# convert the object into a dict
reach_v1_campaigns_campaign_details_resource_dict = reach_v1_campaigns_campaign_details_resource_instance.to_dict()
# create an instance of ReachV1CampaignsCampaignDetailsResource from a dict
reach_v1_campaigns_campaign_details_resource_from_dict = ReachV1CampaignsCampaignDetailsResource.from_dict(reach_v1_campaigns_campaign_details_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


