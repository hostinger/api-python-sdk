# ReachV1ContactsProfileContactUpdateResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**surname** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**subscription_status** | **str** |  | [optional] 
**subscribed_at** | **datetime** |  | [optional] 
**unsubscribed_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_profile_contact_update_resource import ReachV1ContactsProfileContactUpdateResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsProfileContactUpdateResource from a JSON string
reach_v1_contacts_profile_contact_update_resource_instance = ReachV1ContactsProfileContactUpdateResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsProfileContactUpdateResource.to_json())

# convert the object into a dict
reach_v1_contacts_profile_contact_update_resource_dict = reach_v1_contacts_profile_contact_update_resource_instance.to_dict()
# create an instance of ReachV1ContactsProfileContactUpdateResource from a dict
reach_v1_contacts_profile_contact_update_resource_from_dict = ReachV1ContactsProfileContactUpdateResource.from_dict(reach_v1_contacts_profile_contact_update_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


