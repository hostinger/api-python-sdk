# MailV1MailboxesMailboxCountsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forwarders** | **int** | Number of attached forwarders | [optional] 
**aliases** | **int** | Number of attached aliases | [optional] 
**autoreplies** | **int** | Number of attached auto-replies | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_mailboxes_mailbox_counts_resource import MailV1MailboxesMailboxCountsResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1MailboxesMailboxCountsResource from a JSON string
mail_v1_mailboxes_mailbox_counts_resource_instance = MailV1MailboxesMailboxCountsResource.from_json(json)
# print the JSON string representation of the object
print(MailV1MailboxesMailboxCountsResource.to_json())

# convert the object into a dict
mail_v1_mailboxes_mailbox_counts_resource_dict = mail_v1_mailboxes_mailbox_counts_resource_instance.to_dict()
# create an instance of MailV1MailboxesMailboxCountsResource from a dict
mail_v1_mailboxes_mailbox_counts_resource_from_dict = MailV1MailboxesMailboxCountsResource.from_dict(mail_v1_mailboxes_mailbox_counts_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


