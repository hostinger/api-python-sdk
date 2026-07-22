# MailV1MailboxesMailboxResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Mailbox resource ID | [optional] 
**address** | **str** | Email address of the mailbox | [optional] 
**status** | **str** | Mailbox status | [optional] 
**status_reason** | **str** | Reason the mailbox was suspended | [optional] 
**protocols** | [**MailV1MailboxesMailboxProtocolsResource**](MailV1MailboxesMailboxProtocolsResource.md) |  | [optional] 
**counts** | [**MailV1MailboxesMailboxCountsResource**](MailV1MailboxesMailboxCountsResource.md) |  | [optional] 
**is_catchall** | **bool** | Whether the mailbox is the catch-all destination for its domain | [optional] 
**usage** | [**MailV1MailboxesMailboxUsageResource**](MailV1MailboxesMailboxUsageResource.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_mailboxes_mailbox_resource import MailV1MailboxesMailboxResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1MailboxesMailboxResource from a JSON string
mail_v1_mailboxes_mailbox_resource_instance = MailV1MailboxesMailboxResource.from_json(json)
# print the JSON string representation of the object
print(MailV1MailboxesMailboxResource.to_json())

# convert the object into a dict
mail_v1_mailboxes_mailbox_resource_dict = mail_v1_mailboxes_mailbox_resource_instance.to_dict()
# create an instance of MailV1MailboxesMailboxResource from a dict
mail_v1_mailboxes_mailbox_resource_from_dict = MailV1MailboxesMailboxResource.from_dict(mail_v1_mailboxes_mailbox_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


