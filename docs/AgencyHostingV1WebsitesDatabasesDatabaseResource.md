# AgencyHostingV1WebsitesDatabasesDatabaseResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Database name. | [optional] 
**created_at** | **datetime** | Database creation date in ISO 8601 format. | [optional] 
**users** | [**List[AgencyHostingV1WebsitesDatabasesDatabaseUserResource]**](AgencyHostingV1WebsitesDatabasesDatabaseUserResource.md) | Non-system users that can access the database. | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_databases_database_resource import AgencyHostingV1WebsitesDatabasesDatabaseResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesDatabasesDatabaseResource from a JSON string
agency_hosting_v1_websites_databases_database_resource_instance = AgencyHostingV1WebsitesDatabasesDatabaseResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesDatabasesDatabaseResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_databases_database_resource_dict = agency_hosting_v1_websites_databases_database_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesDatabasesDatabaseResource from a dict
agency_hosting_v1_websites_databases_database_resource_from_dict = AgencyHostingV1WebsitesDatabasesDatabaseResource.from_dict(agency_hosting_v1_websites_databases_database_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


