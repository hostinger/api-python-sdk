# ReachListProfileContactsV1200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReachV1ContactsProfileContactResource]**](ReachV1ContactsProfileContactResource.md) | Array of [&#x60;Reach.V1.Contacts.ProfileContactResource&#x60;](#model/reachv1contactsprofilecontactresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.reach_list_profile_contacts_v1200_response import ReachListProfileContactsV1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReachListProfileContactsV1200Response from a JSON string
reach_list_profile_contacts_v1200_response_instance = ReachListProfileContactsV1200Response.from_json(json)
# print the JSON string representation of the object
print(ReachListProfileContactsV1200Response.to_json())

# convert the object into a dict
reach_list_profile_contacts_v1200_response_dict = reach_list_profile_contacts_v1200_response_instance.to_dict()
# create an instance of ReachListProfileContactsV1200Response from a dict
reach_list_profile_contacts_v1200_response_from_dict = ReachListProfileContactsV1200Response.from_dict(reach_list_profile_contacts_v1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


