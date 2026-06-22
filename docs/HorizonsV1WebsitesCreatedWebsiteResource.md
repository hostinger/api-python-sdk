# HorizonsV1WebsitesCreatedWebsiteResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**website_url** | **str** | The website URL for the user to access their website in Hostinger Horizons interface | 
**website_id** | **str** | The website ID | 

## Example

```python
from hostinger_api.models.horizons_v1_websites_created_website_resource import HorizonsV1WebsitesCreatedWebsiteResource

# TODO update the JSON string below
json = "{}"
# create an instance of HorizonsV1WebsitesCreatedWebsiteResource from a JSON string
horizons_v1_websites_created_website_resource_instance = HorizonsV1WebsitesCreatedWebsiteResource.from_json(json)
# print the JSON string representation of the object
print(HorizonsV1WebsitesCreatedWebsiteResource.to_json())

# convert the object into a dict
horizons_v1_websites_created_website_resource_dict = horizons_v1_websites_created_website_resource_instance.to_dict()
# create an instance of HorizonsV1WebsitesCreatedWebsiteResource from a dict
horizons_v1_websites_created_website_resource_from_dict = HorizonsV1WebsitesCreatedWebsiteResource.from_dict(horizons_v1_websites_created_website_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


