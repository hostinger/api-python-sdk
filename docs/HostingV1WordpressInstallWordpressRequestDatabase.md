# HostingV1WordpressInstallWordpressRequestDatabase

Optional. If the named database already exists, it will be used for this WordPress install. Otherwise a new database is created with a generated name and random credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Database name (username prefix added if missing) | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_wordpress_install_wordpress_request_database import HostingV1WordpressInstallWordpressRequestDatabase

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1WordpressInstallWordpressRequestDatabase from a JSON string
hosting_v1_wordpress_install_wordpress_request_database_instance = HostingV1WordpressInstallWordpressRequestDatabase.from_json(json)
# print the JSON string representation of the object
print(HostingV1WordpressInstallWordpressRequestDatabase.to_json())

# convert the object into a dict
hosting_v1_wordpress_install_wordpress_request_database_dict = hosting_v1_wordpress_install_wordpress_request_database_instance.to_dict()
# create an instance of HostingV1WordpressInstallWordpressRequestDatabase from a dict
hosting_v1_wordpress_install_wordpress_request_database_from_dict = HostingV1WordpressInstallWordpressRequestDatabase.from_dict(hosting_v1_wordpress_install_wordpress_request_database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


