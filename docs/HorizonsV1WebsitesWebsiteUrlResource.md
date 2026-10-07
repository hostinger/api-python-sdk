# HorizonsV1WebsitesWebsiteUrlResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**website_url** | **str** | The website URL for the user to access their website in Hostinger Horizons interface | 
**published_at** | **datetime** | When the website was last published, or null if it has never been published | [optional] 
**is_template** | **bool** | Whether the website is published as a template, so its published pages show a \&quot;Use template\&quot; banner | [optional] 
**is_in_progress** | **bool** | Whether Hostinger Horizons is still generating changes or publishing the website. Publishing is refused while it is true, and editing while changes are being generated. An unfinished template migration also refuses publishing, with its own error, without setting this flag. | [optional] 
**has_ecommerce_store** | **bool** | Whether the website has an ecommerce store | [optional] 

## Example

```python
from hostinger_api.models.horizons_v1_websites_website_url_resource import HorizonsV1WebsitesWebsiteUrlResource

# TODO update the JSON string below
json = "{}"
# create an instance of HorizonsV1WebsitesWebsiteUrlResource from a JSON string
horizons_v1_websites_website_url_resource_instance = HorizonsV1WebsitesWebsiteUrlResource.from_json(json)
# print the JSON string representation of the object
print(HorizonsV1WebsitesWebsiteUrlResource.to_json())

# convert the object into a dict
horizons_v1_websites_website_url_resource_dict = horizons_v1_websites_website_url_resource_instance.to_dict()
# create an instance of HorizonsV1WebsitesWebsiteUrlResource from a dict
horizons_v1_websites_website_url_resource_from_dict = HorizonsV1WebsitesWebsiteUrlResource.from_dict(horizons_v1_websites_website_url_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


