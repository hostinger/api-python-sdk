# AgencyHostingV1WebsitesDatabasesUsersCreateDatabaseUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_user** | **str** | Database username to create (alphanumeric and underscores). | 
**password** | **str** | Password for the database user (requires mixed case, letters, and numbers). | 
**host** | **str** | Host the user connects from (IPv4, IPv6, % wildcard, or localhost). Defaults to localhost. | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_databases_users_create_database_user_request import AgencyHostingV1WebsitesDatabasesUsersCreateDatabaseUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesDatabasesUsersCreateDatabaseUserRequest from a JSON string
agency_hosting_v1_websites_databases_users_create_database_user_request_instance = AgencyHostingV1WebsitesDatabasesUsersCreateDatabaseUserRequest.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesDatabasesUsersCreateDatabaseUserRequest.to_json())

# convert the object into a dict
agency_hosting_v1_websites_databases_users_create_database_user_request_dict = agency_hosting_v1_websites_databases_users_create_database_user_request_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesDatabasesUsersCreateDatabaseUserRequest from a dict
agency_hosting_v1_websites_databases_users_create_database_user_request_from_dict = AgencyHostingV1WebsitesDatabasesUsersCreateDatabaseUserRequest.from_dict(agency_hosting_v1_websites_databases_users_create_database_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


