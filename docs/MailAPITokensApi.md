# hostinger_api.MailAPITokensApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_token_v1**](MailAPITokensApi.md#create_api_token_v1) | **POST** /api/mail/v1/orders/{orderId}/api-tokens | Create API token
[**list_api_tokens_v1**](MailAPITokensApi.md#list_api_tokens_v1) | **GET** /api/mail/v1/api-tokens | List API tokens
[**revoke_api_token_v1**](MailAPITokensApi.md#revoke_api_token_v1) | **DELETE** /api/mail/v1/api-tokens/{tokenId} | Revoke API token


# **create_api_token_v1**
> MailV1ApiTokensApiTokenCreatedResource create_api_token_v1(order_id, mail_v1_schema_create_api_token_request_schema)

Create API token

Create an API token for the given mail order. The token grants access
to the [Hostinger Email API](https://api.mail.hostinger.com/), where
you can provision and manage the mailboxes it is scoped to.

The plaintext token is returned only in this response, never again.
A maximum of 10 tokens can exist per order. Use
`scope.has_all_mailboxes` to cover all current and future mailboxes,
or list specific mailboxes in `scope.mailbox_ids`.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_v1_api_tokens_api_token_created_resource import MailV1ApiTokensApiTokenCreatedResource
from hostinger_api.models.mail_v1_schema_create_api_token_request_schema import MailV1SchemaCreateApiTokenRequestSchema
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailAPITokensApi(api_client)
    order_id = 'OR1a2b3c4d5e6f7g' # str | Order resource ID
    mail_v1_schema_create_api_token_request_schema = hostinger_api.MailV1SchemaCreateApiTokenRequestSchema() # MailV1SchemaCreateApiTokenRequestSchema | 

    try:
        # Create API token
        api_response = api_instance.create_api_token_v1(order_id, mail_v1_schema_create_api_token_request_schema)
        print("The response of MailAPITokensApi->create_api_token_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailAPITokensApi->create_api_token_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order resource ID | 
 **mail_v1_schema_create_api_token_request_schema** | [**MailV1SchemaCreateApiTokenRequestSchema**](MailV1SchemaCreateApiTokenRequestSchema.md)|  | 

### Return type

[**MailV1ApiTokensApiTokenCreatedResource**](MailV1ApiTokensApiTokenCreatedResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created response |  -  |
**401** | Unauthenticated response |  -  |
**404** | Error response |  -  |
**409** | Error response |  -  |
**422** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_api_tokens_v1**
> MailListAPITokensV1200Response list_api_tokens_v1(order_id=order_id, page=page, per_page=per_page)

List API tokens

Retrieve a paginated list of
[Hostinger Email API](https://api.mail.hostinger.com/) tokens across
all your mail orders, optionally filtered by order. Plaintext tokens
are never included; they are returned only when a token is created.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_list_api_tokens_v1200_response import MailListAPITokensV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailAPITokensApi(api_client)
    order_id = 'OR1a2b3c4d5e6f7g,OR9z8y7x6w5v4u3t' # str | Filter tokens by order resource ID. Single value or comma-separated list. (optional)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List API tokens
        api_response = api_instance.list_api_tokens_v1(order_id=order_id, page=page, per_page=per_page)
        print("The response of MailAPITokensApi->list_api_tokens_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailAPITokensApi->list_api_tokens_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Filter tokens by order resource ID. Single value or comma-separated list. | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**MailListAPITokensV1200Response**](MailListAPITokensV1200Response.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Unauthenticated response |  -  |
**422** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_api_token_v1**
> CommonSuccessEmptyResource revoke_api_token_v1(token_id)

Revoke API token

Revoke an API token. The token immediately loses access to the
[Hostinger Email API](https://api.mail.hostinger.com/). This action
cannot be undone.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailAPITokensApi(api_client)
    token_id = '019683f8-1234-7abc-8def-0123456789ab' # str | API token ID (returned when the token was created)

    try:
        # Revoke API token
        api_response = api_instance.revoke_api_token_v1(token_id)
        print("The response of MailAPITokensApi->revoke_api_token_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailAPITokensApi->revoke_api_token_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| API token ID (returned when the token was created) | 

### Return type

[**CommonSuccessEmptyResource**](CommonSuccessEmptyResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Unauthenticated response |  -  |
**404** | Error response |  -  |
**422** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

