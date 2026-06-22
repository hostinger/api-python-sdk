# HostingV1DatabasesDatabaseResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Database name. | [optional] 
**user** | **str** | Database user. | [optional] 
**domain** | **str** | Domain assigned to the database, or null when the database is unassigned. | [optional] 
**permissions** | **object** | Database user permissions keyed by permission name. | [optional] 
**created_at** | **datetime** | Database creation date in ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Database last update date in ISO 8601 format. | [optional] 
**disk_usage_mb** | **int** | Current database disk usage in megabytes. | [optional] 
**max_size_mb** | **int** | Maximum allowed database size in megabytes. | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_databases_database_resource import HostingV1DatabasesDatabaseResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1DatabasesDatabaseResource from a JSON string
hosting_v1_databases_database_resource_instance = HostingV1DatabasesDatabaseResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1DatabasesDatabaseResource.to_json())

# convert the object into a dict
hosting_v1_databases_database_resource_dict = hosting_v1_databases_database_resource_instance.to_dict()
# create an instance of HostingV1DatabasesDatabaseResource from a dict
hosting_v1_databases_database_resource_from_dict = HostingV1DatabasesDatabaseResource.from_dict(hosting_v1_databases_database_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


