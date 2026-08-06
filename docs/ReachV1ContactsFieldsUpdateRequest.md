# ReachV1ContactsFieldsUpdateRequest

Rename a custom contact field and, for the choice types, replace its option set. The field type and slug are immutable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**options** | [**List[ReachV1ContactsFieldsUpdateRequestOptionsInner]**](ReachV1ContactsFieldsUpdateRequestOptionsInner.md) | Replaces the option set when provided. Entries carrying a uuid are kept and relabelled, entries without one are created, and any existing option missing from the list is deleted along with the values contacts hold for it. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_fields_update_request import ReachV1ContactsFieldsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsFieldsUpdateRequest from a JSON string
reach_v1_contacts_fields_update_request_instance = ReachV1ContactsFieldsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsFieldsUpdateRequest.to_json())

# convert the object into a dict
reach_v1_contacts_fields_update_request_dict = reach_v1_contacts_fields_update_request_instance.to_dict()
# create an instance of ReachV1ContactsFieldsUpdateRequest from a dict
reach_v1_contacts_fields_update_request_from_dict = ReachV1ContactsFieldsUpdateRequest.from_dict(reach_v1_contacts_fields_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


