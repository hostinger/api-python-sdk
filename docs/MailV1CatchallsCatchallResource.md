# MailV1CatchallsCatchallResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique catch-all identifier | [optional] 
**mailbox** | [**MailV1CatchallsCatchallMailboxResource**](MailV1CatchallsCatchallMailboxResource.md) |  | [optional] 
**domain** | **str** | Domain whose unrouted messages are caught | [optional] 
**is_active** | **bool** | Whether the catch-all is active | [optional] 
**is_confirmed** | **bool** | Whether the mailbox address has confirmed the catch-all | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_catchalls_catchall_resource import MailV1CatchallsCatchallResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1CatchallsCatchallResource from a JSON string
mail_v1_catchalls_catchall_resource_instance = MailV1CatchallsCatchallResource.from_json(json)
# print the JSON string representation of the object
print(MailV1CatchallsCatchallResource.to_json())

# convert the object into a dict
mail_v1_catchalls_catchall_resource_dict = mail_v1_catchalls_catchall_resource_instance.to_dict()
# create an instance of MailV1CatchallsCatchallResource from a dict
mail_v1_catchalls_catchall_resource_from_dict = MailV1CatchallsCatchallResource.from_dict(mail_v1_catchalls_catchall_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


