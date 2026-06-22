# HostingV1WordpressInstallWordpressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain of the existing website where WordPress will be installed | 
**site_title** | **str** | Title of the WordPress site | 
**language** | **str** | WordPress locale. Defaults to en_US when omitted. | [optional] 
**directory** | **str** | Relative directory to install WordPress into. Defaults to the website root when omitted. | [optional] 
**overwrite** | **bool** | When false (default), does not replace an existing installation. If WordPress is already installed on the domain/path, the async install job fails unless true. | [optional] 
**auto_updates** | **str** | WordPress core auto-update policy | [optional] 
**version** | **str** | WordPress core version to install. If omitted, the latest core version compatible with the account vhost PHP version is selected. | [optional] 
**credentials** | [**HostingV1WordpressInstallWordpressRequestCredentials**](HostingV1WordpressInstallWordpressRequestCredentials.md) |  | 
**database** | [**HostingV1WordpressInstallWordpressRequestDatabase**](HostingV1WordpressInstallWordpressRequestDatabase.md) |  | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_wordpress_install_wordpress_request import HostingV1WordpressInstallWordpressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1WordpressInstallWordpressRequest from a JSON string
hosting_v1_wordpress_install_wordpress_request_instance = HostingV1WordpressInstallWordpressRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1WordpressInstallWordpressRequest.to_json())

# convert the object into a dict
hosting_v1_wordpress_install_wordpress_request_dict = hosting_v1_wordpress_install_wordpress_request_instance.to_dict()
# create an instance of HostingV1WordpressInstallWordpressRequest from a dict
hosting_v1_wordpress_install_wordpress_request_from_dict = HostingV1WordpressInstallWordpressRequest.from_dict(hosting_v1_wordpress_install_wordpress_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


