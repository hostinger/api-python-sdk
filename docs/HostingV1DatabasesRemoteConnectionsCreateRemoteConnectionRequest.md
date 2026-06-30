# HostingV1DatabasesRemoteConnectionsCreateRemoteConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | Remote host to allow: an IPv4/IPv6 address, or \&quot;%\&quot; for any host. | 

## Example

```python
from hostinger_api.models.hosting_v1_databases_remote_connections_create_remote_connection_request import HostingV1DatabasesRemoteConnectionsCreateRemoteConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1DatabasesRemoteConnectionsCreateRemoteConnectionRequest from a JSON string
hosting_v1_databases_remote_connections_create_remote_connection_request_instance = HostingV1DatabasesRemoteConnectionsCreateRemoteConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1DatabasesRemoteConnectionsCreateRemoteConnectionRequest.to_json())

# convert the object into a dict
hosting_v1_databases_remote_connections_create_remote_connection_request_dict = hosting_v1_databases_remote_connections_create_remote_connection_request_instance.to_dict()
# create an instance of HostingV1DatabasesRemoteConnectionsCreateRemoteConnectionRequest from a dict
hosting_v1_databases_remote_connections_create_remote_connection_request_from_dict = HostingV1DatabasesRemoteConnectionsCreateRemoteConnectionRequest.from_dict(hosting_v1_databases_remote_connections_create_remote_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


