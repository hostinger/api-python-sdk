# MailV1AliasesAliasResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique alias identifier | [optional] 
**address** | **str** | Email address of the alias | [optional] 
**mailbox** | [**MailV1AliasesAliasMailboxResource**](MailV1AliasesAliasMailboxResource.md) |  | [optional] 
**is_active** | **bool** | Whether the alias is active and not suspended | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_aliases_alias_resource import MailV1AliasesAliasResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1AliasesAliasResource from a JSON string
mail_v1_aliases_alias_resource_instance = MailV1AliasesAliasResource.from_json(json)
# print the JSON string representation of the object
print(MailV1AliasesAliasResource.to_json())

# convert the object into a dict
mail_v1_aliases_alias_resource_dict = mail_v1_aliases_alias_resource_instance.to_dict()
# create an instance of MailV1AliasesAliasResource from a dict
mail_v1_aliases_alias_resource_from_dict = MailV1AliasesAliasResource.from_dict(mail_v1_aliases_alias_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


