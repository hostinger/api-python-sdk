# MailV1OrdersPlanMailboxResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_quota** | **int** | Storage quota per mailbox in megabytes | [optional] 
**messages_quota** | **int** | Maximum number of stored messages per mailbox | [optional] 
**forwarder_quota** | **int** | Maximum number of forwarders per mailbox | [optional] 
**alias_quota** | **int** | Maximum number of aliases per mailbox | [optional] 
**max_outbound_message_size** | **int** | Maximum outbound message size in bytes | [optional] 
**max_outbound_attachment_size** | **int** | Maximum outbound attachment size in bytes | [optional] 
**max_outbound_recipient_limit** | **int** | Maximum number of recipients per outbound message | [optional] 
**rate_limit_inbound** | **str** | Inbound message rate limit as &#x60;messages/seconds&#x60; | [optional] 
**rate_limit_outbound** | **str** | Outbound message rate limit as &#x60;messages/seconds&#x60; | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_orders_plan_mailbox_resource import MailV1OrdersPlanMailboxResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1OrdersPlanMailboxResource from a JSON string
mail_v1_orders_plan_mailbox_resource_instance = MailV1OrdersPlanMailboxResource.from_json(json)
# print the JSON string representation of the object
print(MailV1OrdersPlanMailboxResource.to_json())

# convert the object into a dict
mail_v1_orders_plan_mailbox_resource_dict = mail_v1_orders_plan_mailbox_resource_instance.to_dict()
# create an instance of MailV1OrdersPlanMailboxResource from a dict
mail_v1_orders_plan_mailbox_resource_from_dict = MailV1OrdersPlanMailboxResource.from_dict(mail_v1_orders_plan_mailbox_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


