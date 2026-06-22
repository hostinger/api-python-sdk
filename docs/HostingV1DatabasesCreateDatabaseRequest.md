# HostingV1DatabasesCreateDatabaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Database name. If the account username prefix is omitted, it is added automatically. | 
**user** | **str** | Database user. If the account username prefix is omitted, it is added automatically. | 
**password** | **str** | Database user password. | 
**website_domain** | **str** | Website domain assigned to the database. | 

## Example

```python
from hostinger_api.models.hosting_v1_databases_create_database_request import HostingV1DatabasesCreateDatabaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1DatabasesCreateDatabaseRequest from a JSON string
hosting_v1_databases_create_database_request_instance = HostingV1DatabasesCreateDatabaseRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1DatabasesCreateDatabaseRequest.to_json())

# convert the object into a dict
hosting_v1_databases_create_database_request_dict = hosting_v1_databases_create_database_request_instance.to_dict()
# create an instance of HostingV1DatabasesCreateDatabaseRequest from a dict
hosting_v1_databases_create_database_request_from_dict = HostingV1DatabasesCreateDatabaseRequest.from_dict(hosting_v1_databases_create_database_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


