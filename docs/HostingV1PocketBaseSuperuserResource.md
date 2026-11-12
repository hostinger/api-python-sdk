# HostingV1PocketBaseSuperuserResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Website domain that serves the PocketBase API | 
**superuser_email** | **str** | Email of the superuser that was created or got the new password | 
**superuser_password** | **str** | The new password of that superuser, generated when the request had none. Hostinger does not store it and will not show it again, so save it right away. | 

## Example

```python
from hostinger_api.models.hosting_v1_pocket_base_superuser_resource import HostingV1PocketBaseSuperuserResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1PocketBaseSuperuserResource from a JSON string
hosting_v1_pocket_base_superuser_resource_instance = HostingV1PocketBaseSuperuserResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1PocketBaseSuperuserResource.to_json())

# convert the object into a dict
hosting_v1_pocket_base_superuser_resource_dict = hosting_v1_pocket_base_superuser_resource_instance.to_dict()
# create an instance of HostingV1PocketBaseSuperuserResource from a dict
hosting_v1_pocket_base_superuser_resource_from_dict = HostingV1PocketBaseSuperuserResource.from_dict(hosting_v1_pocket_base_superuser_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


