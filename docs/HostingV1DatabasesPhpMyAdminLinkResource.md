# HostingV1DatabasesPhpMyAdminLinkResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** | Direct sign-on URL to phpMyAdmin for the specified database. | 

## Example

```python
from hostinger_api.models.hosting_v1_databases_php_my_admin_link_resource import HostingV1DatabasesPhpMyAdminLinkResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1DatabasesPhpMyAdminLinkResource from a JSON string
hosting_v1_databases_php_my_admin_link_resource_instance = HostingV1DatabasesPhpMyAdminLinkResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1DatabasesPhpMyAdminLinkResource.to_json())

# convert the object into a dict
hosting_v1_databases_php_my_admin_link_resource_dict = hosting_v1_databases_php_my_admin_link_resource_instance.to_dict()
# create an instance of HostingV1DatabasesPhpMyAdminLinkResource from a dict
hosting_v1_databases_php_my_admin_link_resource_from_dict = HostingV1DatabasesPhpMyAdminLinkResource.from_dict(hosting_v1_databases_php_my_admin_link_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


