# HostingV1WordpressInstallWordpressRequestCredentials

WordPress admin credentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**login** | **str** | WordPress admin username | 
**password** | **str** |  | 

## Example

```python
from hostinger_api.models.hosting_v1_wordpress_install_wordpress_request_credentials import HostingV1WordpressInstallWordpressRequestCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1WordpressInstallWordpressRequestCredentials from a JSON string
hosting_v1_wordpress_install_wordpress_request_credentials_instance = HostingV1WordpressInstallWordpressRequestCredentials.from_json(json)
# print the JSON string representation of the object
print(HostingV1WordpressInstallWordpressRequestCredentials.to_json())

# convert the object into a dict
hosting_v1_wordpress_install_wordpress_request_credentials_dict = hosting_v1_wordpress_install_wordpress_request_credentials_instance.to_dict()
# create an instance of HostingV1WordpressInstallWordpressRequestCredentials from a dict
hosting_v1_wordpress_install_wordpress_request_credentials_from_dict = HostingV1WordpressInstallWordpressRequestCredentials.from_dict(hosting_v1_wordpress_install_wordpress_request_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


