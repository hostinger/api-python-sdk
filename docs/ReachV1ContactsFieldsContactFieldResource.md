# ReachV1ContactsFieldsContactFieldResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**slug** | **str** | Derived from the label on creation and immutable afterwards | [optional] 
**options** | [**List[ReachV1ContactsFieldsContactFieldOptionResource]**](ReachV1ContactsFieldsContactFieldOptionResource.md) | Available choices. Always empty for the scalar field types. | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_fields_contact_field_resource import ReachV1ContactsFieldsContactFieldResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsFieldsContactFieldResource from a JSON string
reach_v1_contacts_fields_contact_field_resource_instance = ReachV1ContactsFieldsContactFieldResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsFieldsContactFieldResource.to_json())

# convert the object into a dict
reach_v1_contacts_fields_contact_field_resource_dict = reach_v1_contacts_fields_contact_field_resource_instance.to_dict()
# create an instance of ReachV1ContactsFieldsContactFieldResource from a dict
reach_v1_contacts_fields_contact_field_resource_from_dict = ReachV1ContactsFieldsContactFieldResource.from_dict(reach_v1_contacts_fields_contact_field_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


