# MailListMailboxActionLogsV1200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MailV1LogsMailboxActionsMailboxActionLogResource]**](MailV1LogsMailboxActionsMailboxActionLogResource.md) | Array of [&#x60;Mail.V1.Logs.MailboxActions.MailboxActionLogResource&#x60;](#model/mailv1logsmailboxactionsmailboxactionlogresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.mail_list_mailbox_action_logs_v1200_response import MailListMailboxActionLogsV1200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MailListMailboxActionLogsV1200Response from a JSON string
mail_list_mailbox_action_logs_v1200_response_instance = MailListMailboxActionLogsV1200Response.from_json(json)
# print the JSON string representation of the object
print(MailListMailboxActionLogsV1200Response.to_json())

# convert the object into a dict
mail_list_mailbox_action_logs_v1200_response_dict = mail_list_mailbox_action_logs_v1200_response_instance.to_dict()
# create an instance of MailListMailboxActionLogsV1200Response from a dict
mail_list_mailbox_action_logs_v1200_response_from_dict = MailListMailboxActionLogsV1200Response.from_dict(mail_list_mailbox_action_logs_v1200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


