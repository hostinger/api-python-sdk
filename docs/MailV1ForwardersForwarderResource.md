# MailV1ForwardersForwarderResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique forwarder identifier | [optional] 
**mailbox** | [**MailV1ForwardersForwarderMailboxResource**](MailV1ForwardersForwarderMailboxResource.md) |  | [optional] 
**destination** | **str** | Email address the messages are forwarded to | [optional] 
**is_keep_copy_enabled** | **bool** | Whether a copy of forwarded messages is kept in the mailbox | [optional] 
**is_active** | **bool** | Whether the forwarder is active | [optional] 
**is_confirmed** | **bool** | Whether the destination address has confirmed the forwarding | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_forwarders_forwarder_resource import MailV1ForwardersForwarderResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1ForwardersForwarderResource from a JSON string
mail_v1_forwarders_forwarder_resource_instance = MailV1ForwardersForwarderResource.from_json(json)
# print the JSON string representation of the object
print(MailV1ForwardersForwarderResource.to_json())

# convert the object into a dict
mail_v1_forwarders_forwarder_resource_dict = mail_v1_forwarders_forwarder_resource_instance.to_dict()
# create an instance of MailV1ForwardersForwarderResource from a dict
mail_v1_forwarders_forwarder_resource_from_dict = MailV1ForwardersForwarderResource.from_dict(mail_v1_forwarders_forwarder_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


