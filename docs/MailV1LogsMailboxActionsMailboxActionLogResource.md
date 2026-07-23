# MailV1LogsMailboxActionsMailboxActionLogResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** | **str** |  | [optional] 
**time** | **int** | Unix timestamp of the event | [optional] 
**event** | **str** |  | [optional] 
**mailbox** | **str** | Mailbox email address | [optional] 
**hostname** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_logs_mailbox_actions_mailbox_action_log_resource import MailV1LogsMailboxActionsMailboxActionLogResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1LogsMailboxActionsMailboxActionLogResource from a JSON string
mail_v1_logs_mailbox_actions_mailbox_action_log_resource_instance = MailV1LogsMailboxActionsMailboxActionLogResource.from_json(json)
# print the JSON string representation of the object
print(MailV1LogsMailboxActionsMailboxActionLogResource.to_json())

# convert the object into a dict
mail_v1_logs_mailbox_actions_mailbox_action_log_resource_dict = mail_v1_logs_mailbox_actions_mailbox_action_log_resource_instance.to_dict()
# create an instance of MailV1LogsMailboxActionsMailboxActionLogResource from a dict
mail_v1_logs_mailbox_actions_mailbox_action_log_resource_from_dict = MailV1LogsMailboxActionsMailboxActionLogResource.from_dict(mail_v1_logs_mailbox_actions_mailbox_action_log_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


