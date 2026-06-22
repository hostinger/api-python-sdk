# HostingV1DatabasesChangeDatabasePasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | New database user password. | 

## Example

```python
from hostinger_api.models.hosting_v1_databases_change_database_password_request import HostingV1DatabasesChangeDatabasePasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1DatabasesChangeDatabasePasswordRequest from a JSON string
hosting_v1_databases_change_database_password_request_instance = HostingV1DatabasesChangeDatabasePasswordRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1DatabasesChangeDatabasePasswordRequest.to_json())

# convert the object into a dict
hosting_v1_databases_change_database_password_request_dict = hosting_v1_databases_change_database_password_request_instance.to_dict()
# create an instance of HostingV1DatabasesChangeDatabasePasswordRequest from a dict
hosting_v1_databases_change_database_password_request_from_dict = HostingV1DatabasesChangeDatabasePasswordRequest.from_dict(hosting_v1_databases_change_database_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


