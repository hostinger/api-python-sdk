# AgencyHostingV1WebsitesWebsiteListItemResource

Website item. The `details` shape differs per platform — see the `platform` field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**client_id** | **int** |  | 
**order_id** | **int** |  | 
**platform** | **str** | Website platform | 
**state** | **str** | Website state | 
**created_at** | **datetime** |  | 
**plan** | [**AgencyHostingV1WebsitesPlanResource**](AgencyHostingV1WebsitesPlanResource.md) |  | 
**details** | [**AgencyHostingV1WebsitesWebsiteListItemResourceDetails**](AgencyHostingV1WebsitesWebsiteListItemResourceDetails.md) |  | 
**suspension_reason** | **str** | Reason for suspension, only populated for payment related suspensions | 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_website_list_item_resource import AgencyHostingV1WebsitesWebsiteListItemResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesWebsiteListItemResource from a JSON string
agency_hosting_v1_websites_website_list_item_resource_instance = AgencyHostingV1WebsitesWebsiteListItemResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesWebsiteListItemResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_website_list_item_resource_dict = agency_hosting_v1_websites_website_list_item_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesWebsiteListItemResource from a dict
agency_hosting_v1_websites_website_list_item_resource_from_dict = AgencyHostingV1WebsitesWebsiteListItemResource.from_dict(agency_hosting_v1_websites_website_list_item_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


