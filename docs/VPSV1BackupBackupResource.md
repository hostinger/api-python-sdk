# VPSV1BackupBackupResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Backup ID | [optional] 
**location** | **str** | Location of the backup | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger-api.models.vpsv1_backup_backup_resource import VPSV1BackupBackupResource

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1BackupBackupResource from a JSON string
vpsv1_backup_backup_resource_instance = VPSV1BackupBackupResource.from_json(json)
# print the JSON string representation of the object
print(VPSV1BackupBackupResource.to_json())

# convert the object into a dict
vpsv1_backup_backup_resource_dict = vpsv1_backup_backup_resource_instance.to_dict()
# create an instance of VPSV1BackupBackupResource from a dict
vpsv1_backup_backup_resource_from_dict = VPSV1BackupBackupResource.from_dict(vpsv1_backup_backup_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


