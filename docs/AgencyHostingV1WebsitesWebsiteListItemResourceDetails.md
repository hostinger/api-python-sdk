# AgencyHostingV1WebsitesWebsiteListItemResourceDetails

Platform-specific website details. Shape depends on `platform`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Website UID | [optional] 
**ipv4** | **str** | IPv4 address | [optional] 
**flavor** | **str** | Setup flavor | [optional] 
**type** | **str** | Detected website type | [optional] 
**username** | **str** | Account username | [optional] 
**description** | **str** | Description | [optional] 
**state** | **str** | Application state | [optional] 
**created_at** | **datetime** |  | [optional] 
**settings** | **object** | Website settings, e.g. PHP configuration | [optional] 
**wordpress** | **object** | WordPress installation details | [optional] 
**domains** | **List[object]** | Application domains | [optional] 
**preview_domain** | **object** | Preview domain | [optional] 
**processes** | **List[object]** | Ongoing website processes | [optional] 
**horizons_uuid** | **str** | Horizons UUID | [optional] 
**id** | **str** | Builder ID | [optional] 
**vhost** | **str** | Domain name | [optional] 
**uuid** | **str** | Application UUID | [optional] 
**title** | **str** | Application title | [optional] 
**port** | **int** | Application port | [optional] 
**runtime** | **str** | Application runtime | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_website_list_item_resource_details import AgencyHostingV1WebsitesWebsiteListItemResourceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesWebsiteListItemResourceDetails from a JSON string
agency_hosting_v1_websites_website_list_item_resource_details_instance = AgencyHostingV1WebsitesWebsiteListItemResourceDetails.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesWebsiteListItemResourceDetails.to_json())

# convert the object into a dict
agency_hosting_v1_websites_website_list_item_resource_details_dict = agency_hosting_v1_websites_website_list_item_resource_details_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesWebsiteListItemResourceDetails from a dict
agency_hosting_v1_websites_website_list_item_resource_details_from_dict = AgencyHostingV1WebsitesWebsiteListItemResourceDetails.from_dict(agency_hosting_v1_websites_website_list_item_resource_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


