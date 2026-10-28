# ReachV1StoresConnectionResourceStore

Reach store created for the connection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**synced_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_stores_connection_resource_store import ReachV1StoresConnectionResourceStore

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1StoresConnectionResourceStore from a JSON string
reach_v1_stores_connection_resource_store_instance = ReachV1StoresConnectionResourceStore.from_json(json)
# print the JSON string representation of the object
print(ReachV1StoresConnectionResourceStore.to_json())

# convert the object into a dict
reach_v1_stores_connection_resource_store_dict = reach_v1_stores_connection_resource_store_instance.to_dict()
# create an instance of ReachV1StoresConnectionResourceStore from a dict
reach_v1_stores_connection_resource_store_from_dict = ReachV1StoresConnectionResourceStore.from_dict(reach_v1_stores_connection_resource_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


