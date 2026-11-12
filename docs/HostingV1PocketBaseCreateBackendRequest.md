# HostingV1PocketBaseCreateBackendRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**superuser_email** | **str** | Email of the PocketBase superuser. Defaults to the email of the website owner. | [optional] 
**superuser_password** | **str** | Password for the PocketBase superuser, 10-128 characters. Leave it out to have a strong one generated. Either way it is returned once in the response and never stored. | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_pocket_base_create_backend_request import HostingV1PocketBaseCreateBackendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1PocketBaseCreateBackendRequest from a JSON string
hosting_v1_pocket_base_create_backend_request_instance = HostingV1PocketBaseCreateBackendRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1PocketBaseCreateBackendRequest.to_json())

# convert the object into a dict
hosting_v1_pocket_base_create_backend_request_dict = hosting_v1_pocket_base_create_backend_request_instance.to_dict()
# create an instance of HostingV1PocketBaseCreateBackendRequest from a dict
hosting_v1_pocket_base_create_backend_request_from_dict = HostingV1PocketBaseCreateBackendRequest.from_dict(hosting_v1_pocket_base_create_backend_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


