# ReachV1ContactsContactResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**surname** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**subscription_status** | **str** |  | [optional] 
**subscribed_at** | **datetime** |  | [optional] 
**source** | **str** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_contact_resource import ReachV1ContactsContactResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsContactResource from a JSON string
reach_v1_contacts_contact_resource_instance = ReachV1ContactsContactResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsContactResource.to_json())

# convert the object into a dict
reach_v1_contacts_contact_resource_dict = reach_v1_contacts_contact_resource_instance.to_dict()
# create an instance of ReachV1ContactsContactResource from a dict
reach_v1_contacts_contact_resource_from_dict = ReachV1ContactsContactResource.from_dict(reach_v1_contacts_contact_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


