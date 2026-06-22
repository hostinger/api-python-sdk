# HostingV1WebsitesCreateWebsiteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name for the website. Cannot start with \&quot;www.\&quot; | 
**order_id** | **int** | ID of the associated order | 
**datacenter_code** | **str** | Datacenter code. This parameter is required when creating the first website on a new hosting plan. | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_websites_create_website_request import HostingV1WebsitesCreateWebsiteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1WebsitesCreateWebsiteRequest from a JSON string
hosting_v1_websites_create_website_request_instance = HostingV1WebsitesCreateWebsiteRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1WebsitesCreateWebsiteRequest.to_json())

# convert the object into a dict
hosting_v1_websites_create_website_request_dict = hosting_v1_websites_create_website_request_instance.to_dict()
# create an instance of HostingV1WebsitesCreateWebsiteRequest from a dict
hosting_v1_websites_create_website_request_from_dict = HostingV1WebsitesCreateWebsiteRequest.from_dict(hosting_v1_websites_create_website_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


