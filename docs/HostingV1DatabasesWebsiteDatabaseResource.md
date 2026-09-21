# HostingV1DatabasesWebsiteDatabaseResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | [**HostingV1DatabasesWebsiteDatabaseConnectionResource**](HostingV1DatabasesWebsiteDatabaseConnectionResource.md) |  | 
**env_var_keys** | **List[str]** | Names of the environment variables written for this database. Values are never returned. | 

## Example

```python
from hostinger_api.models.hosting_v1_databases_website_database_resource import HostingV1DatabasesWebsiteDatabaseResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1DatabasesWebsiteDatabaseResource from a JSON string
hosting_v1_databases_website_database_resource_instance = HostingV1DatabasesWebsiteDatabaseResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1DatabasesWebsiteDatabaseResource.to_json())

# convert the object into a dict
hosting_v1_databases_website_database_resource_dict = hosting_v1_databases_website_database_resource_instance.to_dict()
# create an instance of HostingV1DatabasesWebsiteDatabaseResource from a dict
hosting_v1_databases_website_database_resource_from_dict = HostingV1DatabasesWebsiteDatabaseResource.from_dict(hosting_v1_databases_website_database_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


