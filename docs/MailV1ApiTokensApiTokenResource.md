# MailV1ApiTokensApiTokenResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique API token identifier | [optional] 
**order_id** | **str** | Resource ID of the owning mail order | [optional] 
**name** | **str** | Human-readable label for this token | [optional] 
**scope** | [**MailV1ApiTokensApiTokenScopeResource**](MailV1ApiTokensApiTokenScopeResource.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**last_used_at** | **datetime** | Last successful authentication using this token | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_api_tokens_api_token_resource import MailV1ApiTokensApiTokenResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1ApiTokensApiTokenResource from a JSON string
mail_v1_api_tokens_api_token_resource_instance = MailV1ApiTokensApiTokenResource.from_json(json)
# print the JSON string representation of the object
print(MailV1ApiTokensApiTokenResource.to_json())

# convert the object into a dict
mail_v1_api_tokens_api_token_resource_dict = mail_v1_api_tokens_api_token_resource_instance.to_dict()
# create an instance of MailV1ApiTokensApiTokenResource from a dict
mail_v1_api_tokens_api_token_resource_from_dict = MailV1ApiTokensApiTokenResource.from_dict(mail_v1_api_tokens_api_token_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


