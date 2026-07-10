# AgencyHostingV1WebsitesWebsiteOrderPlanResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Plan name | [optional] 
**parameters** | [**AgencyHostingV1WebsitesWebsiteOrderPlanResourceParameters**](AgencyHostingV1WebsitesWebsiteOrderPlanResourceParameters.md) |  | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_website_order_plan_resource import AgencyHostingV1WebsitesWebsiteOrderPlanResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesWebsiteOrderPlanResource from a JSON string
agency_hosting_v1_websites_website_order_plan_resource_instance = AgencyHostingV1WebsitesWebsiteOrderPlanResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesWebsiteOrderPlanResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_website_order_plan_resource_dict = agency_hosting_v1_websites_website_order_plan_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesWebsiteOrderPlanResource from a dict
agency_hosting_v1_websites_website_order_plan_resource_from_dict = AgencyHostingV1WebsitesWebsiteOrderPlanResource.from_dict(agency_hosting_v1_websites_website_order_plan_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


