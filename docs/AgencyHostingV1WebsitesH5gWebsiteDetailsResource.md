# AgencyHostingV1WebsitesH5gWebsiteDetailsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Website UID | [optional] 
**ipv4** | **str** | IPv4 address | [optional] 
**flavor** | **str** | Setup flavor | [optional] 
**type** | **str** | Detected website type | [optional] 
**username** | **str** | Username for this order | [optional] 
**description** | **str** | Description | [optional] 
**state** | **str** | Website state | [optional] 
**created_at** | **datetime** |  | [optional] 
**settings** | **object** | Website settings, e.g. PHP configuration | [optional] 
**wordpress** | **object** | WordPress installation details | [optional] 
**domains** | **List[object]** | Website domains | [optional] 
**preview_domain** | **object** | Preview domain | [optional] 
**processes** | **List[object]** | Ongoing website processes | [optional] 
**horizons_uuid** | **str** | Horizons UUID (only for horizons websites) | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_h5g_website_details_resource import AgencyHostingV1WebsitesH5gWebsiteDetailsResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesH5gWebsiteDetailsResource from a JSON string
agency_hosting_v1_websites_h5g_website_details_resource_instance = AgencyHostingV1WebsitesH5gWebsiteDetailsResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesH5gWebsiteDetailsResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_h5g_website_details_resource_dict = agency_hosting_v1_websites_h5g_website_details_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesH5gWebsiteDetailsResource from a dict
agency_hosting_v1_websites_h5g_website_details_resource_from_dict = AgencyHostingV1WebsitesH5gWebsiteDetailsResource.from_dict(agency_hosting_v1_websites_h5g_website_details_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


