# HorizonsV1WebsitesWebsiteResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**website_id** | **str** | The website ID | 
**description** | **str** | The website description | [optional] 
**domain** | **str** | The domain the website is published on, if it has been published | [optional] 
**status** | **str** | The website status | 
**created_at** | **datetime** | The website creation date | 
**website_url** | **str** | The website URL for the user to access their website in Hostinger Horizons interface | 

## Example

```python
from hostinger_api.models.horizons_v1_websites_website_resource import HorizonsV1WebsitesWebsiteResource

# TODO update the JSON string below
json = "{}"
# create an instance of HorizonsV1WebsitesWebsiteResource from a JSON string
horizons_v1_websites_website_resource_instance = HorizonsV1WebsitesWebsiteResource.from_json(json)
# print the JSON string representation of the object
print(HorizonsV1WebsitesWebsiteResource.to_json())

# convert the object into a dict
horizons_v1_websites_website_resource_dict = horizons_v1_websites_website_resource_instance.to_dict()
# create an instance of HorizonsV1WebsitesWebsiteResource from a dict
horizons_v1_websites_website_resource_from_dict = HorizonsV1WebsitesWebsiteResource.from_dict(horizons_v1_websites_website_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


