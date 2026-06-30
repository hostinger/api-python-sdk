# HostingV1DatabasesRemoteConnectionsRemoteConnectionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_name** | **str** | Full name of the database the rule applies to. | [optional] 
**database_user** | **str** | Database user the rule applies to. | [optional] 
**ip** | **str** | Allowed remote host: an IPv4/IPv6 address, or \&quot;%\&quot; for any host. | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_databases_remote_connections_remote_connection_resource import HostingV1DatabasesRemoteConnectionsRemoteConnectionResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1DatabasesRemoteConnectionsRemoteConnectionResource from a JSON string
hosting_v1_databases_remote_connections_remote_connection_resource_instance = HostingV1DatabasesRemoteConnectionsRemoteConnectionResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1DatabasesRemoteConnectionsRemoteConnectionResource.to_json())

# convert the object into a dict
hosting_v1_databases_remote_connections_remote_connection_resource_dict = hosting_v1_databases_remote_connections_remote_connection_resource_instance.to_dict()
# create an instance of HostingV1DatabasesRemoteConnectionsRemoteConnectionResource from a dict
hosting_v1_databases_remote_connections_remote_connection_resource_from_dict = HostingV1DatabasesRemoteConnectionsRemoteConnectionResource.from_dict(hosting_v1_databases_remote_connections_remote_connection_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


