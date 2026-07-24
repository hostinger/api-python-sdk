# hostinger_api.MailAutorepliesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_autoreply_v1**](MailAutorepliesApi.md#create_autoreply_v1) | **POST** /api/mail/v1/mailboxes/{mailboxId}/autoreplies | Create autoreply
[**delete_autoreply_v1**](MailAutorepliesApi.md#delete_autoreply_v1) | **DELETE** /api/mail/v1/autoreplies/{autoreplyId} | Delete autoreply
[**list_autoreplies_v1**](MailAutorepliesApi.md#list_autoreplies_v1) | **GET** /api/mail/v1/orders/{orderId}/autoreplies | List autoreplies
[**update_autoreply_v1**](MailAutorepliesApi.md#update_autoreply_v1) | **PUT** /api/mail/v1/autoreplies/{autoreplyId} | Update autoreply


# **create_autoreply_v1**
> MailV1AutorepliesAutoreplyResource create_autoreply_v1(mailbox_id, mail_v1_schema_upsert_autoreply_request_schema)

Create autoreply

Create an automatic reply for the given mailbox. A mailbox can have
only one autoreply. Omit `starts_at` to activate the autoreply
immediately and omit `ends_at` to keep it active indefinitely.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_v1_autoreplies_autoreply_resource import MailV1AutorepliesAutoreplyResource
from hostinger_api.models.mail_v1_schema_upsert_autoreply_request_schema import MailV1SchemaUpsertAutoreplyRequestSchema
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailAutorepliesApi(api_client)
    mailbox_id = 'AC1a2b3c4d5e6f7g' # str | Mailbox resource ID
    mail_v1_schema_upsert_autoreply_request_schema = hostinger_api.MailV1SchemaUpsertAutoreplyRequestSchema() # MailV1SchemaUpsertAutoreplyRequestSchema | 

    try:
        # Create autoreply
        api_response = api_instance.create_autoreply_v1(mailbox_id, mail_v1_schema_upsert_autoreply_request_schema)
        print("The response of MailAutorepliesApi->create_autoreply_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailAutorepliesApi->create_autoreply_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox_id** | **str**| Mailbox resource ID | 
 **mail_v1_schema_upsert_autoreply_request_schema** | [**MailV1SchemaUpsertAutoreplyRequestSchema**](MailV1SchemaUpsertAutoreplyRequestSchema.md)|  | 

### Return type

[**MailV1AutorepliesAutoreplyResource**](MailV1AutorepliesAutoreplyResource.md)

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

# **delete_autoreply_v1**
> CommonSuccessEmptyResource delete_autoreply_v1(autoreply_id)

Delete autoreply

Delete the autoreply of a mailbox. The mailbox stops sending
automatic replies immediately.

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
    api_instance = hostinger_api.MailAutorepliesApi(api_client)
    autoreply_id = 'AR1a2b3c4d5e6f7g' # str | Autoreply resource ID

    try:
        # Delete autoreply
        api_response = api_instance.delete_autoreply_v1(autoreply_id)
        print("The response of MailAutorepliesApi->delete_autoreply_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailAutorepliesApi->delete_autoreply_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **autoreply_id** | **str**| Autoreply resource ID | 

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

# **list_autoreplies_v1**
> MailListAutorepliesV1200Response list_autoreplies_v1(order_id, page=page, per_page=per_page)

List autoreplies

Retrieve a paginated list of autoreplies across all mailboxes of a
mail order.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_list_autoreplies_v1200_response import MailListAutorepliesV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailAutorepliesApi(api_client)
    order_id = 'OR1a2b3c4d5e6f7g' # str | Order resource ID
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List autoreplies
        api_response = api_instance.list_autoreplies_v1(order_id, page=page, per_page=per_page)
        print("The response of MailAutorepliesApi->list_autoreplies_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailAutorepliesApi->list_autoreplies_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order resource ID | 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**MailListAutorepliesV1200Response**](MailListAutorepliesV1200Response.md)

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

# **update_autoreply_v1**
> MailV1AutorepliesAutoreplyResource update_autoreply_v1(autoreply_id, mail_v1_schema_upsert_autoreply_request_schema)

Update autoreply

Replace the autoreply with the given content and schedule. Omitted
optional fields are cleared: omit `starts_at` to activate the
autoreply immediately and omit `ends_at` to keep it active
indefinitely.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_v1_autoreplies_autoreply_resource import MailV1AutorepliesAutoreplyResource
from hostinger_api.models.mail_v1_schema_upsert_autoreply_request_schema import MailV1SchemaUpsertAutoreplyRequestSchema
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailAutorepliesApi(api_client)
    autoreply_id = 'AR1a2b3c4d5e6f7g' # str | Autoreply resource ID
    mail_v1_schema_upsert_autoreply_request_schema = hostinger_api.MailV1SchemaUpsertAutoreplyRequestSchema() # MailV1SchemaUpsertAutoreplyRequestSchema | 

    try:
        # Update autoreply
        api_response = api_instance.update_autoreply_v1(autoreply_id, mail_v1_schema_upsert_autoreply_request_schema)
        print("The response of MailAutorepliesApi->update_autoreply_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailAutorepliesApi->update_autoreply_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **autoreply_id** | **str**| Autoreply resource ID | 
 **mail_v1_schema_upsert_autoreply_request_schema** | [**MailV1SchemaUpsertAutoreplyRequestSchema**](MailV1SchemaUpsertAutoreplyRequestSchema.md)|  | 

### Return type

[**MailV1AutorepliesAutoreplyResource**](MailV1AutorepliesAutoreplyResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
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

