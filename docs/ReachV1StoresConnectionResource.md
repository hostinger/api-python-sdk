# ReachV1StoresConnectionResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the connection between the store and the profile. | [optional] 
**store_id** | **str** |  | [optional] 
**store** | [**ReachV1StoresConnectionResourceStore**](ReachV1StoresConnectionResourceStore.md) |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_stores_connection_resource import ReachV1StoresConnectionResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1StoresConnectionResource from a JSON string
reach_v1_stores_connection_resource_instance = ReachV1StoresConnectionResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1StoresConnectionResource.to_json())

# convert the object into a dict
reach_v1_stores_connection_resource_dict = reach_v1_stores_connection_resource_instance.to_dict()
# create an instance of ReachV1StoresConnectionResource from a dict
reach_v1_stores_connection_resource_from_dict = ReachV1StoresConnectionResource.from_dict(reach_v1_stores_connection_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


