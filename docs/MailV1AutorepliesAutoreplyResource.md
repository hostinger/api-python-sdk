# MailV1AutorepliesAutoreplyResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique autoreply identifier | [optional] 
**mailbox** | [**MailV1AutorepliesAutoreplyMailboxResource**](MailV1AutorepliesAutoreplyMailboxResource.md) |  | [optional] 
**subject** | **str** | Subject of the automatic reply | [optional] 
**body** | **str** | Body of the automatic reply | [optional] 
**display_name** | **str** | Sender display name used for the reply | [optional] 
**starts_at** | **datetime** | When the autoreply becomes active | [optional] 
**ends_at** | **datetime** | When the autoreply stops | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_autoreplies_autoreply_resource import MailV1AutorepliesAutoreplyResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1AutorepliesAutoreplyResource from a JSON string
mail_v1_autoreplies_autoreply_resource_instance = MailV1AutorepliesAutoreplyResource.from_json(json)
# print the JSON string representation of the object
print(MailV1AutorepliesAutoreplyResource.to_json())

# convert the object into a dict
mail_v1_autoreplies_autoreply_resource_dict = mail_v1_autoreplies_autoreply_resource_instance.to_dict()
# create an instance of MailV1AutorepliesAutoreplyResource from a dict
mail_v1_autoreplies_autoreply_resource_from_dict = MailV1AutorepliesAutoreplyResource.from_dict(mail_v1_autoreplies_autoreply_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


