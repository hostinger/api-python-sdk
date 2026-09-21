# HostingV1DatabasesWebsiteDatabaseConnectionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Database name, as written into DB_NAME | 
**user** | **str** | Database user, as written into DB_USER | 
**host** | **str** | MySQL host as written into DB_HOST. The application connects over the loopback. | 
**port** | **int** | MySQL port as written into DB_PORT | 

## Example

```python
from hostinger_api.models.hosting_v1_databases_website_database_connection_resource import HostingV1DatabasesWebsiteDatabaseConnectionResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1DatabasesWebsiteDatabaseConnectionResource from a JSON string
hosting_v1_databases_website_database_connection_resource_instance = HostingV1DatabasesWebsiteDatabaseConnectionResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1DatabasesWebsiteDatabaseConnectionResource.to_json())

# convert the object into a dict
hosting_v1_databases_website_database_connection_resource_dict = hosting_v1_databases_website_database_connection_resource_instance.to_dict()
# create an instance of HostingV1DatabasesWebsiteDatabaseConnectionResource from a dict
hosting_v1_databases_website_database_connection_resource_from_dict = HostingV1DatabasesWebsiteDatabaseConnectionResource.from_dict(hosting_v1_databases_website_database_connection_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


