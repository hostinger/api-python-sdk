# AgencyHostingV1WebsitesWebsiteProcessResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Process ID | [optional] 
**type** | **str** | Process type | [optional] 
**status** | **str** | Process status | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_website_process_resource import AgencyHostingV1WebsitesWebsiteProcessResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesWebsiteProcessResource from a JSON string
agency_hosting_v1_websites_website_process_resource_instance = AgencyHostingV1WebsitesWebsiteProcessResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesWebsiteProcessResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_website_process_resource_dict = agency_hosting_v1_websites_website_process_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesWebsiteProcessResource from a dict
agency_hosting_v1_websites_website_process_resource_from_dict = AgencyHostingV1WebsitesWebsiteProcessResource.from_dict(agency_hosting_v1_websites_website_process_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


