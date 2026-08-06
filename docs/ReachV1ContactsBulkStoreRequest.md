# ReachV1ContactsBulkStoreRequest

Create many contacts in one call

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contacts** | [**List[ReachV1ContactsBulkStoreRequestContactsInner]**](ReachV1ContactsBulkStoreRequestContactsInner.md) |  | 
**tag_uuids** | **List[str]** | Existing tags to attach to every created contact | [optional] 
**note** | **str** | Note applied to every created contact | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_bulk_store_request import ReachV1ContactsBulkStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsBulkStoreRequest from a JSON string
reach_v1_contacts_bulk_store_request_instance = ReachV1ContactsBulkStoreRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsBulkStoreRequest.to_json())

# convert the object into a dict
reach_v1_contacts_bulk_store_request_dict = reach_v1_contacts_bulk_store_request_instance.to_dict()
# create an instance of ReachV1ContactsBulkStoreRequest from a dict
reach_v1_contacts_bulk_store_request_from_dict = ReachV1ContactsBulkStoreRequest.from_dict(reach_v1_contacts_bulk_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


