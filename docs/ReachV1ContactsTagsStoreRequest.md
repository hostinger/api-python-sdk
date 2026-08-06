# ReachV1ContactsTagsStoreRequest

Names to create. Names that already exist in the profile are returned as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** |  | 

## Example

```python
from hostinger_api.models.reach_v1_contacts_tags_store_request import ReachV1ContactsTagsStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsTagsStoreRequest from a JSON string
reach_v1_contacts_tags_store_request_instance = ReachV1ContactsTagsStoreRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsTagsStoreRequest.to_json())

# convert the object into a dict
reach_v1_contacts_tags_store_request_dict = reach_v1_contacts_tags_store_request_instance.to_dict()
# create an instance of ReachV1ContactsTagsStoreRequest from a dict
reach_v1_contacts_tags_store_request_from_dict = ReachV1ContactsTagsStoreRequest.from_dict(reach_v1_contacts_tags_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


