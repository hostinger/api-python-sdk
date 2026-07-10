# AgencyHostingV1WebsitesWebsiteOrderResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Order ID | [optional] 
**status** | **str** | Order status | [optional] 
**created_at** | **datetime** |  | [optional] 
**plan** | [**AgencyHostingV1WebsitesWebsiteOrderPlanResource**](AgencyHostingV1WebsitesWebsiteOrderPlanResource.md) |  | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_website_order_resource import AgencyHostingV1WebsitesWebsiteOrderResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesWebsiteOrderResource from a JSON string
agency_hosting_v1_websites_website_order_resource_instance = AgencyHostingV1WebsitesWebsiteOrderResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesWebsiteOrderResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_website_order_resource_dict = agency_hosting_v1_websites_website_order_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesWebsiteOrderResource from a dict
agency_hosting_v1_websites_website_order_resource_from_dict = AgencyHostingV1WebsitesWebsiteOrderResource.from_dict(agency_hosting_v1_websites_website_order_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


