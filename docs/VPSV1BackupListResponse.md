# VPSV1BackupListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VPSV1BackupBackupResource]**](VPSV1BackupBackupResource.md) | Array of [&#x60;VPS.V1.Backup.BackupResource&#x60;](#model/vpsv1backupbackupresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_backup_list_response import VPSV1BackupListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1BackupListResponse from a JSON string
vpsv1_backup_list_response_instance = VPSV1BackupListResponse.from_json(json)
# print the JSON string representation of the object
print(VPSV1BackupListResponse.to_json())

# convert the object into a dict
vpsv1_backup_list_response_dict = vpsv1_backup_list_response_instance.to_dict()
# create an instance of VPSV1BackupListResponse from a dict
vpsv1_backup_list_response_from_dict = VPSV1BackupListResponse.from_dict(vpsv1_backup_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


