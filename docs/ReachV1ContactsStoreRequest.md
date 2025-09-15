# ReachV1ContactsStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**name** | **str** |  | [optional] 
**surname** | **str** |  | [optional] 
**group_uuids** | **List[str]** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_store_request import ReachV1ContactsStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsStoreRequest from a JSON string
reach_v1_contacts_store_request_instance = ReachV1ContactsStoreRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsStoreRequest.to_json())

# convert the object into a dict
reach_v1_contacts_store_request_dict = reach_v1_contacts_store_request_instance.to_dict()
# create an instance of ReachV1ContactsStoreRequest from a dict
reach_v1_contacts_store_request_from_dict = ReachV1ContactsStoreRequest.from_dict(reach_v1_contacts_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


