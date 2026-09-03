# ReachV1CampaignsStoreRequestMetadata

Extra campaign fields. Any key outside the listed ones is rejected.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preheader** | **str** | Preview text shown after the subject line in the inbox. | [optional] 
**source** | **str** | Where the campaign was created from. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_campaigns_store_request_metadata import ReachV1CampaignsStoreRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1CampaignsStoreRequestMetadata from a JSON string
reach_v1_campaigns_store_request_metadata_instance = ReachV1CampaignsStoreRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(ReachV1CampaignsStoreRequestMetadata.to_json())

# convert the object into a dict
reach_v1_campaigns_store_request_metadata_dict = reach_v1_campaigns_store_request_metadata_instance.to_dict()
# create an instance of ReachV1CampaignsStoreRequestMetadata from a dict
reach_v1_campaigns_store_request_metadata_from_dict = ReachV1CampaignsStoreRequestMetadata.from_dict(reach_v1_campaigns_store_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


