# HostingV1PocketBaseUpdateSuperuserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**superuser_email** | **str** | Email of the superuser to create or update. Defaults to the email of the website owner. | [optional] 
**superuser_password** | **str** | New password of the PocketBase superuser, 10-128 characters. Leave it out to have a strong one generated. Either way it is returned once in the response and never stored. | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_pocket_base_update_superuser_request import HostingV1PocketBaseUpdateSuperuserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1PocketBaseUpdateSuperuserRequest from a JSON string
hosting_v1_pocket_base_update_superuser_request_instance = HostingV1PocketBaseUpdateSuperuserRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1PocketBaseUpdateSuperuserRequest.to_json())

# convert the object into a dict
hosting_v1_pocket_base_update_superuser_request_dict = hosting_v1_pocket_base_update_superuser_request_instance.to_dict()
# create an instance of HostingV1PocketBaseUpdateSuperuserRequest from a dict
hosting_v1_pocket_base_update_superuser_request_from_dict = HostingV1PocketBaseUpdateSuperuserRequest.from_dict(hosting_v1_pocket_base_update_superuser_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


