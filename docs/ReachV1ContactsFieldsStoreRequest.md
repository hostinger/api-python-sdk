# ReachV1ContactsFieldsStoreRequest

Define a custom contact field for the profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Immutable once the field exists | 
**label** | **str** |  | 
**options** | **List[str]** | Required for single_choice and multi_choice, ignored for the scalar types. Labels must be unique regardless of casing. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_fields_store_request import ReachV1ContactsFieldsStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsFieldsStoreRequest from a JSON string
reach_v1_contacts_fields_store_request_instance = ReachV1ContactsFieldsStoreRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsFieldsStoreRequest.to_json())

# convert the object into a dict
reach_v1_contacts_fields_store_request_dict = reach_v1_contacts_fields_store_request_instance.to_dict()
# create an instance of ReachV1ContactsFieldsStoreRequest from a dict
reach_v1_contacts_fields_store_request_from_dict = ReachV1ContactsFieldsStoreRequest.from_dict(reach_v1_contacts_fields_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


