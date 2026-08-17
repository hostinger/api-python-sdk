# ReachV1CampaignsCampaignSummaryStatisticsResource

Headline engagement rates. The statistics endpoint carries the full breakdown.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_sent** | **int** | Emails sent for this campaign, and the denominator of the rates below. | [optional] 
**open_rate** | **float** | Percentage of sent emails that were opened. | [optional] 
**click_rate** | **float** | Percentage of sent emails that got a click. | [optional] 
**click_to_open_rate** | **float** | Percentage of the contacts who opened that went on to click. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_campaigns_campaign_summary_statistics_resource import ReachV1CampaignsCampaignSummaryStatisticsResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1CampaignsCampaignSummaryStatisticsResource from a JSON string
reach_v1_campaigns_campaign_summary_statistics_resource_instance = ReachV1CampaignsCampaignSummaryStatisticsResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1CampaignsCampaignSummaryStatisticsResource.to_json())

# convert the object into a dict
reach_v1_campaigns_campaign_summary_statistics_resource_dict = reach_v1_campaigns_campaign_summary_statistics_resource_instance.to_dict()
# create an instance of ReachV1CampaignsCampaignSummaryStatisticsResource from a dict
reach_v1_campaigns_campaign_summary_statistics_resource_from_dict = ReachV1CampaignsCampaignSummaryStatisticsResource.from_dict(reach_v1_campaigns_campaign_summary_statistics_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


