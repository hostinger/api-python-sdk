# MailV1MailboxesMailboxProtocolsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_imap_enabled** | **bool** |  | [optional] 
**is_pop3_enabled** | **bool** |  | [optional] 
**is_smtp_in_enabled** | **bool** |  | [optional] 
**is_smtp_out_enabled** | **bool** |  | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_mailboxes_mailbox_protocols_resource import MailV1MailboxesMailboxProtocolsResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1MailboxesMailboxProtocolsResource from a JSON string
mail_v1_mailboxes_mailbox_protocols_resource_instance = MailV1MailboxesMailboxProtocolsResource.from_json(json)
# print the JSON string representation of the object
print(MailV1MailboxesMailboxProtocolsResource.to_json())

# convert the object into a dict
mail_v1_mailboxes_mailbox_protocols_resource_dict = mail_v1_mailboxes_mailbox_protocols_resource_instance.to_dict()
# create an instance of MailV1MailboxesMailboxProtocolsResource from a dict
mail_v1_mailboxes_mailbox_protocols_resource_from_dict = MailV1MailboxesMailboxProtocolsResource.from_dict(mail_v1_mailboxes_mailbox_protocols_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


