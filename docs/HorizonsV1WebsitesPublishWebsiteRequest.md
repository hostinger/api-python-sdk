# HorizonsV1WebsitesPublishWebsiteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_template** | **bool** | Set to true to publish the website as a template: its published pages show a \&quot;Use template\&quot; banner that copies the website into the visitor&#39;s own account. Set to false to remove the banner. Leave it out to keep the current setting. | [optional] 

## Example

```python
from hostinger_api.models.horizons_v1_websites_publish_website_request import HorizonsV1WebsitesPublishWebsiteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HorizonsV1WebsitesPublishWebsiteRequest from a JSON string
horizons_v1_websites_publish_website_request_instance = HorizonsV1WebsitesPublishWebsiteRequest.from_json(json)
# print the JSON string representation of the object
print(HorizonsV1WebsitesPublishWebsiteRequest.to_json())

# convert the object into a dict
horizons_v1_websites_publish_website_request_dict = horizons_v1_websites_publish_website_request_instance.to_dict()
# create an instance of HorizonsV1WebsitesPublishWebsiteRequest from a dict
horizons_v1_websites_publish_website_request_from_dict = HorizonsV1WebsitesPublishWebsiteRequest.from_dict(horizons_v1_websites_publish_website_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


