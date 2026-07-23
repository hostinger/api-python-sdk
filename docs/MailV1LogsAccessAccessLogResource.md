# MailV1LogsAccessAccessLogResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**session** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**remote_ip** | **str** |  | [optional] 
**login_time** | **datetime** |  | [optional] 
**var_in** | **int** | Bytes received | [optional] 
**out** | **int** | Bytes sent | [optional] 
**deleted** | **int** |  | [optional] 
**expunged** | **int** |  | [optional] 
**trashed** | **int** |  | [optional] 
**logout_time** | **datetime** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**app_name** | **str** |  | [optional] 
**has_deletions** | **bool** |  | [optional] 
**result** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**is_important** | **bool** | True when the session deleted, expunged or trashed messages | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_logs_access_access_log_resource import MailV1LogsAccessAccessLogResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1LogsAccessAccessLogResource from a JSON string
mail_v1_logs_access_access_log_resource_instance = MailV1LogsAccessAccessLogResource.from_json(json)
# print the JSON string representation of the object
print(MailV1LogsAccessAccessLogResource.to_json())

# convert the object into a dict
mail_v1_logs_access_access_log_resource_dict = mail_v1_logs_access_access_log_resource_instance.to_dict()
# create an instance of MailV1LogsAccessAccessLogResource from a dict
mail_v1_logs_access_access_log_resource_from_dict = MailV1LogsAccessAccessLogResource.from_dict(mail_v1_logs_access_access_log_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


