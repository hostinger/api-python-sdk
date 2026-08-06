# ReachV1ContactsTagsManageContactsRequest

Contacts to assign to, or remove from, a tag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_uuids** | **List[str]** | Contacts to apply the change to. Required unless all_contacts is true. | [optional] 
**all_contacts** | **bool** | Apply to every contact in the profile | [optional] [default to False]

## Example

```python
from hostinger_api.models.reach_v1_contacts_tags_manage_contacts_request import ReachV1ContactsTagsManageContactsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsTagsManageContactsRequest from a JSON string
reach_v1_contacts_tags_manage_contacts_request_instance = ReachV1ContactsTagsManageContactsRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsTagsManageContactsRequest.to_json())

# convert the object into a dict
reach_v1_contacts_tags_manage_contacts_request_dict = reach_v1_contacts_tags_manage_contacts_request_instance.to_dict()
# create an instance of ReachV1ContactsTagsManageContactsRequest from a dict
reach_v1_contacts_tags_manage_contacts_request_from_dict = ReachV1ContactsTagsManageContactsRequest.from_dict(reach_v1_contacts_tags_manage_contacts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


