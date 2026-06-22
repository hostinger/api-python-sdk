# HostingV1WebsitesWebsiteResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Website domain | [optional] 
**vhost_type** | **str** | Virtual host type | [optional] 
**is_enabled** | **bool** | Whether website is enabled | [optional] 
**username** | **str** | Username | [optional] 
**client_id** | **int** | Client ID | [optional] 
**order_id** | **int** | Order ID | [optional] 
**created_at** | **datetime** | Creation date | [optional] 
**root_directory** | **str** | Root directory path | [optional] 
**parent_domain** | **str** | Parent domain | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_websites_website_resource import HostingV1WebsitesWebsiteResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1WebsitesWebsiteResource from a JSON string
hosting_v1_websites_website_resource_instance = HostingV1WebsitesWebsiteResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1WebsitesWebsiteResource.to_json())

# convert the object into a dict
hosting_v1_websites_website_resource_dict = hosting_v1_websites_website_resource_instance.to_dict()
# create an instance of HostingV1WebsitesWebsiteResource from a dict
hosting_v1_websites_website_resource_from_dict = HostingV1WebsitesWebsiteResource.from_dict(hosting_v1_websites_website_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


