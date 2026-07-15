# HostingV1WebsitesDeleteWebsiteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirm** | **bool** | Must be boolean true to confirm the permanent deletion of the website. | 

## Example

```python
from hostinger_api.models.hosting_v1_websites_delete_website_request import HostingV1WebsitesDeleteWebsiteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1WebsitesDeleteWebsiteRequest from a JSON string
hosting_v1_websites_delete_website_request_instance = HostingV1WebsitesDeleteWebsiteRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1WebsitesDeleteWebsiteRequest.to_json())

# convert the object into a dict
hosting_v1_websites_delete_website_request_dict = hosting_v1_websites_delete_website_request_instance.to_dict()
# create an instance of HostingV1WebsitesDeleteWebsiteRequest from a dict
hosting_v1_websites_delete_website_request_from_dict = HostingV1WebsitesDeleteWebsiteRequest.from_dict(hosting_v1_websites_delete_website_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


