# ReachV1CampaignsCampaignStatisticsResource

Campaign performance. Every count is unique contacts rather than raw events, so a contact who opens the same email five times is counted once.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_sent** | **int** | Emails sent for this campaign, and the denominator of every rate below. | [optional] 
**estimated_total_recipients** | **int** | Recipients this campaign was estimated to reach when sending started. Null for campaigns that have not started sending. | [optional] 
**processed_count** | **int** |  | [optional] 
**delivered_count** | **int** |  | [optional] 
**dropped_count** | **int** |  | [optional] 
**bounced_count** | **int** |  | [optional] 
**soft_bounced_count** | **int** |  | [optional] 
**opened_count** | **int** | Contacts who opened this campaign. | [optional] 
**clicked_count** | **int** | Contacts who clicked a link. Only clicks from contacts who also registered an open count. | [optional] 
**unsubscribed_count** | **int** | Contacts who unsubscribed through this campaign. | [optional] 
**open_rate** | **float** | Percentage of sent emails that were opened. | [optional] 
**click_rate** | **float** | Percentage of sent emails that got a click. | [optional] 
**click_to_open_rate** | **float** | Percentage of the contacts who opened that went on to click. | [optional] 
**unsubscribe_rate** | **float** | Percentage of sent emails that led to an unsubscribe. | [optional] 
**has_bounced_contacts** | **bool** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_campaigns_campaign_statistics_resource import ReachV1CampaignsCampaignStatisticsResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1CampaignsCampaignStatisticsResource from a JSON string
reach_v1_campaigns_campaign_statistics_resource_instance = ReachV1CampaignsCampaignStatisticsResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1CampaignsCampaignStatisticsResource.to_json())

# convert the object into a dict
reach_v1_campaigns_campaign_statistics_resource_dict = reach_v1_campaigns_campaign_statistics_resource_instance.to_dict()
# create an instance of ReachV1CampaignsCampaignStatisticsResource from a dict
reach_v1_campaigns_campaign_statistics_resource_from_dict = ReachV1CampaignsCampaignStatisticsResource.from_dict(reach_v1_campaigns_campaign_statistics_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


