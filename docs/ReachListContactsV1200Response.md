# ReachListContactsV1200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReachV1ContactsContactResource]**](ReachV1ContactsContactResource.md) | Array of [&#x60;Reach.V1.Contacts.ContactResource&#x60;](#model/reachv1contactscontactresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.reach_list_contacts_v1200_response import ReachListContactsV1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReachListContactsV1200Response from a JSON string
reach_list_contacts_v1200_response_instance = ReachListContactsV1200Response.from_json(json)
# print the JSON string representation of the object
print(ReachListContactsV1200Response.to_json())

# convert the object into a dict
reach_list_contacts_v1200_response_dict = reach_list_contacts_v1200_response_instance.to_dict()
# create an instance of ReachListContactsV1200Response from a dict
reach_list_contacts_v1200_response_from_dict = ReachListContactsV1200Response.from_dict(reach_list_contacts_v1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


