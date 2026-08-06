# ReachV1ContactsFieldsContactFieldValueResource

A custom contact field together with the value held by one contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**value** | **str** | Set for the scalar field types, null for the choice types | [optional] 
**selected_option_uuids** | **List[str]** | Chosen options for the choice field types, empty for the scalar types | [optional] 
**options** | [**List[ReachV1ContactsFieldsContactFieldOptionResource]**](ReachV1ContactsFieldsContactFieldOptionResource.md) | Every option the field offers, not only the selected ones | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_fields_contact_field_value_resource import ReachV1ContactsFieldsContactFieldValueResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsFieldsContactFieldValueResource from a JSON string
reach_v1_contacts_fields_contact_field_value_resource_instance = ReachV1ContactsFieldsContactFieldValueResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsFieldsContactFieldValueResource.to_json())

# convert the object into a dict
reach_v1_contacts_fields_contact_field_value_resource_dict = reach_v1_contacts_fields_contact_field_value_resource_instance.to_dict()
# create an instance of ReachV1ContactsFieldsContactFieldValueResource from a dict
reach_v1_contacts_fields_contact_field_value_resource_from_dict = ReachV1ContactsFieldsContactFieldValueResource.from_dict(reach_v1_contacts_fields_contact_field_value_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


