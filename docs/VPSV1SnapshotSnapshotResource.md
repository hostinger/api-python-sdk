# VPSV1SnapshotSnapshotResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Snapshot ID | [optional] 
**created_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_snapshot_snapshot_resource import VPSV1SnapshotSnapshotResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1SnapshotSnapshotResource from a JSON string
vpsv1_snapshot_snapshot_resource_instance = VPSV1SnapshotSnapshotResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1SnapshotSnapshotResource.to_json())

# convert the object into a dict
vpsv1_snapshot_snapshot_resource_dict = vpsv1_snapshot_snapshot_resource_instance.to_dict()
# create an instance of VPSV1SnapshotSnapshotResource from a dict
vpsv1_snapshot_snapshot_resource_from_dict = VPSV1SnapshotSnapshotResource.from_dict(vpsv1_snapshot_snapshot_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


