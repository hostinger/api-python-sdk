# MailV1ApiTokensApiTokenScopeResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_all_mailboxes** | **bool** | Whether the token covers all current and future mailboxes of the order | [optional] 
**mailboxes** | [**List[MailV1ApiTokensApiTokenMailboxResource]**](MailV1ApiTokensApiTokenMailboxResource.md) | Mailboxes this token grants access to. Empty when &#x60;has_all_mailboxes&#x60; is true. | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_api_tokens_api_token_scope_resource import MailV1ApiTokensApiTokenScopeResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1ApiTokensApiTokenScopeResource from a JSON string
mail_v1_api_tokens_api_token_scope_resource_instance = MailV1ApiTokensApiTokenScopeResource.from_json(json)
# print the JSON string representation of the object
print(MailV1ApiTokensApiTokenScopeResource.to_json())

# convert the object into a dict
mail_v1_api_tokens_api_token_scope_resource_dict = mail_v1_api_tokens_api_token_scope_resource_instance.to_dict()
# create an instance of MailV1ApiTokensApiTokenScopeResource from a dict
mail_v1_api_tokens_api_token_scope_resource_from_dict = MailV1ApiTokensApiTokenScopeResource.from_dict(mail_v1_api_tokens_api_token_scope_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


