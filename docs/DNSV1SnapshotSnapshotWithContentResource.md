# DNSV1SnapshotSnapshotWithContentResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Snapshot ID | [optional] 
**reason** | **str** | Reason of the update | [optional] 
**snapshot** | **str** | Contents of the DNS zone | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from @hostinger/api.models.dnsv1_snapshot_snapshot_with_content_resource import DNSV1SnapshotSnapshotWithContentResource

# TODO update the JSON string below
json = "{}"
# create an instance of DNSV1SnapshotSnapshotWithContentResource from a JSON string
dnsv1_snapshot_snapshot_with_content_resource_instance = DNSV1SnapshotSnapshotWithContentResource.from_json(json)
# print the JSON string representation of the object
print(DNSV1SnapshotSnapshotWithContentResource.to_json())

# convert the object into a dict
dnsv1_snapshot_snapshot_with_content_resource_dict = dnsv1_snapshot_snapshot_with_content_resource_instance.to_dict()
# create an instance of DNSV1SnapshotSnapshotWithContentResource from a dict
dnsv1_snapshot_snapshot_with_content_resource_from_dict = DNSV1SnapshotSnapshotWithContentResource.from_dict(dnsv1_snapshot_snapshot_with_content_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


