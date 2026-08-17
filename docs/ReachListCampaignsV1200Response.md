# ReachListCampaignsV1200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReachV1CampaignsCampaignResource]**](ReachV1CampaignsCampaignResource.md) | Array of [&#x60;Reach.V1.Campaigns.CampaignResource&#x60;](#model/reachv1campaignscampaignresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.reach_list_campaigns_v1200_response import ReachListCampaignsV1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReachListCampaignsV1200Response from a JSON string
reach_list_campaigns_v1200_response_instance = ReachListCampaignsV1200Response.from_json(json)
# print the JSON string representation of the object
print(ReachListCampaignsV1200Response.to_json())

# convert the object into a dict
reach_list_campaigns_v1200_response_dict = reach_list_campaigns_v1200_response_instance.to_dict()
# create an instance of ReachListCampaignsV1200Response from a dict
reach_list_campaigns_v1200_response_from_dict = ReachListCampaignsV1200Response.from_dict(reach_list_campaigns_v1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


