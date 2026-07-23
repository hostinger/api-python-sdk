# MailV1LogsActionActionLogResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**extra** | **object** | Arbitrary contextual payload | [optional] 
**created_at** | **datetime** |  | [optional] 
**ip_address** | **str** | Only populated for user-role logs | [optional] 
**role** | **str** |  | [optional] 
**action_context** | **str** |  | [optional] 
**response_status** | **str** |  | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_logs_action_action_log_resource import MailV1LogsActionActionLogResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1LogsActionActionLogResource from a JSON string
mail_v1_logs_action_action_log_resource_instance = MailV1LogsActionActionLogResource.from_json(json)
# print the JSON string representation of the object
print(MailV1LogsActionActionLogResource.to_json())

# convert the object into a dict
mail_v1_logs_action_action_log_resource_dict = mail_v1_logs_action_action_log_resource_instance.to_dict()
# create an instance of MailV1LogsActionActionLogResource from a dict
mail_v1_logs_action_action_log_resource_from_dict = MailV1LogsActionActionLogResource.from_dict(mail_v1_logs_action_action_log_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


