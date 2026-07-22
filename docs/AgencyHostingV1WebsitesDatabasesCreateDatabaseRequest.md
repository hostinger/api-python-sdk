# AgencyHostingV1WebsitesDatabasesCreateDatabaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_name** | **str** | Database name to create (alphanumeric characters). | 
**database_user** | **str** | Database username to create alongside the database (alphanumeric characters). | 
**password** | **str** | Password for the database user (requires mixed case, letters, and numbers). | 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_databases_create_database_request import AgencyHostingV1WebsitesDatabasesCreateDatabaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesDatabasesCreateDatabaseRequest from a JSON string
agency_hosting_v1_websites_databases_create_database_request_instance = AgencyHostingV1WebsitesDatabasesCreateDatabaseRequest.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesDatabasesCreateDatabaseRequest.to_json())

# convert the object into a dict
agency_hosting_v1_websites_databases_create_database_request_dict = agency_hosting_v1_websites_databases_create_database_request_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesDatabasesCreateDatabaseRequest from a dict
agency_hosting_v1_websites_databases_create_database_request_from_dict = AgencyHostingV1WebsitesDatabasesCreateDatabaseRequest.from_dict(agency_hosting_v1_websites_databases_create_database_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


