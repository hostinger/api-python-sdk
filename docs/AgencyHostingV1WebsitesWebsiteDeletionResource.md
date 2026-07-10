# AgencyHostingV1WebsitesWebsiteDeletionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**website_uid** | **str** | Deleted website UID | [optional] 
**status** | **str** | Deletion status | [optional] 
**message** | **str** | Human-readable result message | [optional] 
**deleted_at** | **datetime** |  | [optional] 
**is_cleanup_scheduled** | **bool** | Whether background cleanup has been scheduled | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_website_deletion_resource import AgencyHostingV1WebsitesWebsiteDeletionResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesWebsiteDeletionResource from a JSON string
agency_hosting_v1_websites_website_deletion_resource_instance = AgencyHostingV1WebsitesWebsiteDeletionResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesWebsiteDeletionResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_website_deletion_resource_dict = agency_hosting_v1_websites_website_deletion_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesWebsiteDeletionResource from a dict
agency_hosting_v1_websites_website_deletion_resource_from_dict = AgencyHostingV1WebsitesWebsiteDeletionResource.from_dict(agency_hosting_v1_websites_website_deletion_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


