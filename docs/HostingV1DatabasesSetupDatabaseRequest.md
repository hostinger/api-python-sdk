# HostingV1DatabasesSetupDatabaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Optional database name. Generated when omitted. Letters, digits and underscores; must not start with an underscore. Up to 14 characters without the account username prefix (&#x60;u123456789_&#x60;), which is added automatically when missing. With the prefix the full name is 12 to 25 characters. | [optional] 
**user** | **str** | Optional database user. Generated when omitted. Letters, digits and underscores; must not start with an underscore. Up to 14 characters without the account username prefix (&#x60;u123456789_&#x60;), which is added automatically when missing. With the prefix the full user is 12 to 25 characters. | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_databases_setup_database_request import HostingV1DatabasesSetupDatabaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1DatabasesSetupDatabaseRequest from a JSON string
hosting_v1_databases_setup_database_request_instance = HostingV1DatabasesSetupDatabaseRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1DatabasesSetupDatabaseRequest.to_json())

# convert the object into a dict
hosting_v1_databases_setup_database_request_dict = hosting_v1_databases_setup_database_request_instance.to_dict()
# create an instance of HostingV1DatabasesSetupDatabaseRequest from a dict
hosting_v1_databases_setup_database_request_from_dict = HostingV1DatabasesSetupDatabaseRequest.from_dict(hosting_v1_databases_setup_database_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


