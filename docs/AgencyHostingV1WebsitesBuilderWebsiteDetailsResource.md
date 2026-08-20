# AgencyHostingV1WebsitesBuilderWebsiteDetailsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Builder ID | [optional] 
**vhost** | **str** | Domain name | [optional] 
**type** | **str** | Detected website type | [optional] 
**username** | **str** | Account username | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_builder_website_details_resource import AgencyHostingV1WebsitesBuilderWebsiteDetailsResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesBuilderWebsiteDetailsResource from a JSON string
agency_hosting_v1_websites_builder_website_details_resource_instance = AgencyHostingV1WebsitesBuilderWebsiteDetailsResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesBuilderWebsiteDetailsResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_builder_website_details_resource_dict = agency_hosting_v1_websites_builder_website_details_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesBuilderWebsiteDetailsResource from a dict
agency_hosting_v1_websites_builder_website_details_resource_from_dict = AgencyHostingV1WebsitesBuilderWebsiteDetailsResource.from_dict(agency_hosting_v1_websites_builder_website_details_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


