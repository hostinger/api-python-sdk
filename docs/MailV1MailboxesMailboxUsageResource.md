# MailV1MailboxesMailboxUsageResource

Periodically synced usage numbers (may lag behind live values)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_used** | **int** | Storage used in kilobytes | [optional] 
**storage_quota** | **int** | Storage quota in kilobytes | [optional] 
**messages_used** | **int** |  | [optional] 
**messages_quota** | **int** |  | [optional] 
**synced_at** | **datetime** | When the usage numbers were last synced; null if never synced | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_mailboxes_mailbox_usage_resource import MailV1MailboxesMailboxUsageResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1MailboxesMailboxUsageResource from a JSON string
mail_v1_mailboxes_mailbox_usage_resource_instance = MailV1MailboxesMailboxUsageResource.from_json(json)
# print the JSON string representation of the object
print(MailV1MailboxesMailboxUsageResource.to_json())

# convert the object into a dict
mail_v1_mailboxes_mailbox_usage_resource_dict = mail_v1_mailboxes_mailbox_usage_resource_instance.to_dict()
# create an instance of MailV1MailboxesMailboxUsageResource from a dict
mail_v1_mailboxes_mailbox_usage_resource_from_dict = MailV1MailboxesMailboxUsageResource.from_dict(mail_v1_mailboxes_mailbox_usage_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


