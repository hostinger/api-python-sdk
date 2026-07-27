# hostinger_api.MailAliasesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alias_v1**](MailAliasesApi.md#create_alias_v1) | **POST** /api/mail/v1/mailboxes/{mailboxId}/aliases | Create alias
[**delete_alias_v1**](MailAliasesApi.md#delete_alias_v1) | **DELETE** /api/mail/v1/aliases/{aliasId} | Delete alias
[**list_aliases_v1**](MailAliasesApi.md#list_aliases_v1) | **GET** /api/mail/v1/orders/{orderId}/aliases | List aliases


# **create_alias_v1**
> MailV1AliasesAliasResource create_alias_v1(mailbox_id, mail_v1_schema_create_alias_request_schema)

Create alias

Create an alias for the given mailbox. The alias address is formed
from the given local part and the domain of the mailbox. Messages
sent to the alias are delivered to the mailbox.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_v1_aliases_alias_resource import MailV1AliasesAliasResource
from hostinger_api.models.mail_v1_schema_create_alias_request_schema import MailV1SchemaCreateAliasRequestSchema
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailAliasesApi(api_client)
    mailbox_id = 'AC1a2b3c4d5e6f7g' # str | Mailbox resource ID
    mail_v1_schema_create_alias_request_schema = hostinger_api.MailV1SchemaCreateAliasRequestSchema() # MailV1SchemaCreateAliasRequestSchema | 

    try:
        # Create alias
        api_response = api_instance.create_alias_v1(mailbox_id, mail_v1_schema_create_alias_request_schema)
        print("The response of MailAliasesApi->create_alias_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailAliasesApi->create_alias_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox_id** | **str**| Mailbox resource ID | 
 **mail_v1_schema_create_alias_request_schema** | [**MailV1SchemaCreateAliasRequestSchema**](MailV1SchemaCreateAliasRequestSchema.md)|  | 

### Return type

[**MailV1AliasesAliasResource**](MailV1AliasesAliasResource.md)

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

# **delete_alias_v1**
> CommonSuccessEmptyResource delete_alias_v1(alias_id)

Delete alias

Delete an alias. Messages sent to the alias address are no longer
delivered to the mailbox.

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
    api_instance = hostinger_api.MailAliasesApi(api_client)
    alias_id = 'AA1a2b3c4d5e6f7g' # str | Alias resource ID

    try:
        # Delete alias
        api_response = api_instance.delete_alias_v1(alias_id)
        print("The response of MailAliasesApi->delete_alias_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailAliasesApi->delete_alias_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias_id** | **str**| Alias resource ID | 

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

# **list_aliases_v1**
> MailListAliasesV1200Response list_aliases_v1(order_id, page=page, per_page=per_page)

List aliases

Retrieve a paginated list of aliases across all mailboxes of a mail
order.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_list_aliases_v1200_response import MailListAliasesV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailAliasesApi(api_client)
    order_id = 'OR1a2b3c4d5e6f7g' # str | Order resource ID
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List aliases
        api_response = api_instance.list_aliases_v1(order_id, page=page, per_page=per_page)
        print("The response of MailAliasesApi->list_aliases_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailAliasesApi->list_aliases_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order resource ID | 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**MailListAliasesV1200Response**](MailListAliasesV1200Response.md)

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

