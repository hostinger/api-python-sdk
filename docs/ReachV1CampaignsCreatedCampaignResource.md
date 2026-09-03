# ReachV1CampaignsCreatedCampaignResource

The campaign as it was stored, without targeting or delivery progress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**sender_name** | **str** |  | [optional] 
**sender_email** | **str** |  | [optional] 
**template_uuid** | **str** |  | [optional] 
**status** | **str** | Always &#x60;draft&#x60; for a campaign that was just created. | [optional] 
**type** | **str** |  | [optional] 
**is_all_contacts** | **bool** | Whether the campaign targets every contact instead of selected segments. | [optional] 
**metadata** | **Dict[str, str]** | The stored extra fields, including the ones Reach sets itself. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_campaigns_created_campaign_resource import ReachV1CampaignsCreatedCampaignResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1CampaignsCreatedCampaignResource from a JSON string
reach_v1_campaigns_created_campaign_resource_instance = ReachV1CampaignsCreatedCampaignResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1CampaignsCreatedCampaignResource.to_json())

# convert the object into a dict
reach_v1_campaigns_created_campaign_resource_dict = reach_v1_campaigns_created_campaign_resource_instance.to_dict()
# create an instance of ReachV1CampaignsCreatedCampaignResource from a dict
reach_v1_campaigns_created_campaign_resource_from_dict = ReachV1CampaignsCreatedCampaignResource.from_dict(reach_v1_campaigns_created_campaign_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


