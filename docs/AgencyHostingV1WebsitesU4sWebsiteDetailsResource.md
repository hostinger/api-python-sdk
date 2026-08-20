# AgencyHostingV1WebsitesU4sWebsiteDetailsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Application UUID | [optional] 
**title** | **str** | Application title | [optional] 
**port** | **int** | Application port | [optional] 
**type** | **str** | Detected website type | [optional] 
**runtime** | **str** | Application runtime | [optional] 
**state** | **str** | Application state | [optional] 
**domains** | **List[object]** | Application domains | [optional] 
**horizons_uuid** | **str** | Horizons UUID | [optional] 
**preview_domain** | **object** | Preview domain | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_u4s_website_details_resource import AgencyHostingV1WebsitesU4sWebsiteDetailsResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesU4sWebsiteDetailsResource from a JSON string
agency_hosting_v1_websites_u4s_website_details_resource_instance = AgencyHostingV1WebsitesU4sWebsiteDetailsResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesU4sWebsiteDetailsResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_u4s_website_details_resource_dict = agency_hosting_v1_websites_u4s_website_details_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesU4sWebsiteDetailsResource from a dict
agency_hosting_v1_websites_u4s_website_details_resource_from_dict = AgencyHostingV1WebsitesU4sWebsiteDetailsResource.from_dict(agency_hosting_v1_websites_u4s_website_details_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


