# HorizonsV1WebsitesPublishedWebsiteResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Always &#x60;publishing&#x60; - the build runs asynchronously after this response | 
**published_url** | **str** | The URL the published website will be live on in a few minutes | 
**website_url** | **str** | The website URL for the user to track progress in Hostinger Horizons interface | 
**website_id** | **str** | The website ID | 

## Example

```python
from hostinger_api.models.horizons_v1_websites_published_website_resource import HorizonsV1WebsitesPublishedWebsiteResource

# TODO update the JSON string below
json = "{}"
# create an instance of HorizonsV1WebsitesPublishedWebsiteResource from a JSON string
horizons_v1_websites_published_website_resource_instance = HorizonsV1WebsitesPublishedWebsiteResource.from_json(json)
# print the JSON string representation of the object
print(HorizonsV1WebsitesPublishedWebsiteResource.to_json())

# convert the object into a dict
horizons_v1_websites_published_website_resource_dict = horizons_v1_websites_published_website_resource_instance.to_dict()
# create an instance of HorizonsV1WebsitesPublishedWebsiteResource from a dict
horizons_v1_websites_published_website_resource_from_dict = HorizonsV1WebsitesPublishedWebsiteResource.from_dict(horizons_v1_websites_published_website_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


