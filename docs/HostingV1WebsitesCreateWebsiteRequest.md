# HostingV1WebsitesCreateWebsiteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name for the website. Cannot start with \&quot;www.\&quot; and can have at most one subdomain level, e.g. &#x60;blog.example.com&#x60;. | 
**order_id** | **int** | Hosting order ID to create this website on. Choose the order whose hosting plan should host the new website. List orders to find available IDs. | 
**datacenter_code** | **str** | Datacenter for the hosting account when the order does not have one yet. Omit to use the order&#39;s default datacenter. Ignored when the order already has a hosting account. Must be an available datacenter; list available datacenters to find valid codes. | [optional] 

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


