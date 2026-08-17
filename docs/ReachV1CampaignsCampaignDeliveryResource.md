# ReachV1CampaignsCampaignDeliveryResource

Delivery progress. While the campaign is `sending`, `total_sent` climbs towards the estimate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_sent** | **int** | Emails sent so far. | [optional] 
**estimated_total_recipients** | **int** | Recipients this campaign was estimated to reach when sending started. Null for campaigns that have not started sending. | [optional] 
**subscribers_count** | **int** | Contacts currently targeted by this campaign. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_campaigns_campaign_delivery_resource import ReachV1CampaignsCampaignDeliveryResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1CampaignsCampaignDeliveryResource from a JSON string
reach_v1_campaigns_campaign_delivery_resource_instance = ReachV1CampaignsCampaignDeliveryResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1CampaignsCampaignDeliveryResource.to_json())

# convert the object into a dict
reach_v1_campaigns_campaign_delivery_resource_dict = reach_v1_campaigns_campaign_delivery_resource_instance.to_dict()
# create an instance of ReachV1CampaignsCampaignDeliveryResource from a dict
reach_v1_campaigns_campaign_delivery_resource_from_dict = ReachV1CampaignsCampaignDeliveryResource.from_dict(reach_v1_campaigns_campaign_delivery_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


