# ReachV1ContactsBulkStoreRequestContactsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**name** | **str** |  | [optional] 
**surname** | **str** |  | [optional] 
**phone** | **str** | Phone number in E.164 format (leading \&quot;+\&quot; then 7-15 digits) | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_bulk_store_request_contacts_inner import ReachV1ContactsBulkStoreRequestContactsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsBulkStoreRequestContactsInner from a JSON string
reach_v1_contacts_bulk_store_request_contacts_inner_instance = ReachV1ContactsBulkStoreRequestContactsInner.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsBulkStoreRequestContactsInner.to_json())

# convert the object into a dict
reach_v1_contacts_bulk_store_request_contacts_inner_dict = reach_v1_contacts_bulk_store_request_contacts_inner_instance.to_dict()
# create an instance of ReachV1ContactsBulkStoreRequestContactsInner from a dict
reach_v1_contacts_bulk_store_request_contacts_inner_from_dict = ReachV1ContactsBulkStoreRequestContactsInner.from_dict(reach_v1_contacts_bulk_store_request_contacts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


