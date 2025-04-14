# DNSV1SnapshotSnapshotResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Snapshot ID | [optional] 
**reason** | **str** | Reason of the update | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.dnsv1_snapshot_snapshot_resource import DNSV1SnapshotSnapshotResource

# TODO update the JSON string below
json = "{}"
# create an instance of DNSV1SnapshotSnapshotResource from a JSON string
dnsv1_snapshot_snapshot_resource_instance = DNSV1SnapshotSnapshotResource.from_json(json)
# print the JSON string representation of the object
print(DNSV1SnapshotSnapshotResource.to_json())

# convert the object into a dict
dnsv1_snapshot_snapshot_resource_dict = dnsv1_snapshot_snapshot_resource_instance.to_dict()
# create an instance of DNSV1SnapshotSnapshotResource from a dict
dnsv1_snapshot_snapshot_resource_from_dict = DNSV1SnapshotSnapshotResource.from_dict(dnsv1_snapshot_snapshot_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


