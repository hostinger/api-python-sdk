# HostingListAccountDatabasesV1200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HostingV1DatabasesDatabaseResource]**](HostingV1DatabasesDatabaseResource.md) | Array of [&#x60;Hosting.V1.Databases.DatabaseResource&#x60;](#model/hostingv1databasesdatabaseresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.hosting_list_account_databases_v1200_response import HostingListAccountDatabasesV1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of HostingListAccountDatabasesV1200Response from a JSON string
hosting_list_account_databases_v1200_response_instance = HostingListAccountDatabasesV1200Response.from_json(json)
# print the JSON string representation of the object
print(HostingListAccountDatabasesV1200Response.to_json())

# convert the object into a dict
hosting_list_account_databases_v1200_response_dict = hosting_list_account_databases_v1200_response_instance.to_dict()
# create an instance of HostingListAccountDatabasesV1200Response from a dict
hosting_list_account_databases_v1200_response_from_dict = HostingListAccountDatabasesV1200Response.from_dict(hosting_list_account_databases_v1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


