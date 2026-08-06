# ReachV1ContactsUpdateRequest

Fields to change on a contact. Omitted properties are left untouched.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**surname** | **str** |  | [optional] 
**phone** | **str** | Phone number in E.164 format (leading \&quot;+\&quot; then 7-15 digits) | [optional] 
**subscription_status** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**fields** | [**List[ReachV1ContactsUpdateRequestFieldsInner]**](ReachV1ContactsUpdateRequestFieldsInner.md) | Set custom field values. Omit to leave untouched, send an empty array to clear them all. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_update_request import ReachV1ContactsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsUpdateRequest from a JSON string
reach_v1_contacts_update_request_instance = ReachV1ContactsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsUpdateRequest.to_json())

# convert the object into a dict
reach_v1_contacts_update_request_dict = reach_v1_contacts_update_request_instance.to_dict()
# create an instance of ReachV1ContactsUpdateRequest from a dict
reach_v1_contacts_update_request_from_dict = ReachV1ContactsUpdateRequest.from_dict(reach_v1_contacts_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


