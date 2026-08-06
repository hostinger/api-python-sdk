# ReachV1ContactsUpdateRequestFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**value** | **str** | For the scalar field types | [optional] 
**selected_option_uuids** | **List[str]** | For the choice field types | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_update_request_fields_inner import ReachV1ContactsUpdateRequestFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsUpdateRequestFieldsInner from a JSON string
reach_v1_contacts_update_request_fields_inner_instance = ReachV1ContactsUpdateRequestFieldsInner.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsUpdateRequestFieldsInner.to_json())

# convert the object into a dict
reach_v1_contacts_update_request_fields_inner_dict = reach_v1_contacts_update_request_fields_inner_instance.to_dict()
# create an instance of ReachV1ContactsUpdateRequestFieldsInner from a dict
reach_v1_contacts_update_request_fields_inner_from_dict = ReachV1ContactsUpdateRequestFieldsInner.from_dict(reach_v1_contacts_update_request_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


