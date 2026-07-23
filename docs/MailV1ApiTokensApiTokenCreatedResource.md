# MailV1ApiTokensApiTokenCreatedResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique API token identifier | [optional] 
**token** | **str** | Plaintext API token, returned only in this response. Grants access to the [Hostinger Email API](https://api.mail.hostinger.com/) for mailbox provisioning and management. | [optional] 
**name** | **str** | Human-readable label for this token | [optional] 
**scope** | [**MailV1ApiTokensApiTokenScopeResource**](MailV1ApiTokensApiTokenScopeResource.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from hostinger_api.models.mail_v1_api_tokens_api_token_created_resource import MailV1ApiTokensApiTokenCreatedResource

# TODO update the JSON string below
json = "{}"
# create an instance of MailV1ApiTokensApiTokenCreatedResource from a JSON string
mail_v1_api_tokens_api_token_created_resource_instance = MailV1ApiTokensApiTokenCreatedResource.from_json(json)
# print the JSON string representation of the object
print(MailV1ApiTokensApiTokenCreatedResource.to_json())

# convert the object into a dict
mail_v1_api_tokens_api_token_created_resource_dict = mail_v1_api_tokens_api_token_created_resource_instance.to_dict()
# create an instance of MailV1ApiTokensApiTokenCreatedResource from a dict
mail_v1_api_tokens_api_token_created_resource_from_dict = MailV1ApiTokensApiTokenCreatedResource.from_dict(mail_v1_api_tokens_api_token_created_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


