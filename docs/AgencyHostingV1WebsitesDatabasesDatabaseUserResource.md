# AgencyHostingV1WebsitesDatabasesDatabaseUserResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Database username. | [optional] 
**host** | **str** | Database host the user is allowed to connect from. | [optional] 
**created_at** | **datetime** | Database user creation date in ISO 8601 format. | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_databases_database_user_resource import AgencyHostingV1WebsitesDatabasesDatabaseUserResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesDatabasesDatabaseUserResource from a JSON string
agency_hosting_v1_websites_databases_database_user_resource_instance = AgencyHostingV1WebsitesDatabasesDatabaseUserResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesDatabasesDatabaseUserResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_databases_database_user_resource_dict = agency_hosting_v1_websites_databases_database_user_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesDatabasesDatabaseUserResource from a dict
agency_hosting_v1_websites_databases_database_user_resource_from_dict = AgencyHostingV1WebsitesDatabasesDatabaseUserResource.from_dict(agency_hosting_v1_websites_databases_database_user_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


