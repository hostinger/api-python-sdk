# hostinger_api.MailCatchallsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_catch_all_v1**](MailCatchallsApi.md#create_catch_all_v1) | **POST** /api/mail/v1/mailboxes/{mailboxId}/catchalls | Create catch-all
[**delete_catch_all_v1**](MailCatchallsApi.md#delete_catch_all_v1) | **DELETE** /api/mail/v1/catchalls/{catchallId} | Delete catch-all
[**list_catch_alls_v1**](MailCatchallsApi.md#list_catch_alls_v1) | **GET** /api/mail/v1/orders/{orderId}/catchalls | List catch-alls
[**resend_catch_all_confirmation_v1**](MailCatchallsApi.md#resend_catch_all_confirmation_v1) | **POST** /api/mail/v1/catchalls/{catchallId}/confirmation/resend | Resend catch-all confirmation


# **create_catch_all_v1**
> MailV1CatchallsCatchallResource create_catch_all_v1(mailbox_id)

Create catch-all

Create a catch-all that routes all messages sent to unknown addresses
of the domain to the given mailbox. The mailbox address receives a
confirmation email and the catch-all becomes active only after it is
confirmed. A domain can have only one catch-all.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_v1_catchalls_catchall_resource import MailV1CatchallsCatchallResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailCatchallsApi(api_client)
    mailbox_id = 'AC1a2b3c4d5e6f7g' # str | Mailbox resource ID

    try:
        # Create catch-all
        api_response = api_instance.create_catch_all_v1(mailbox_id)
        print("The response of MailCatchallsApi->create_catch_all_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailCatchallsApi->create_catch_all_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox_id** | **str**| Mailbox resource ID | 

### Return type

[**MailV1CatchallsCatchallResource**](MailV1CatchallsCatchallResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **delete_catch_all_v1**
> CommonSuccessEmptyResource delete_catch_all_v1(catchall_id)

Delete catch-all

Delete a catch-all. Messages sent to unknown addresses of the domain
are no longer routed to the mailbox.

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
    api_instance = hostinger_api.MailCatchallsApi(api_client)
    catchall_id = 'CA1a2b3c4d5e6f7g' # str | Catch-all resource ID

    try:
        # Delete catch-all
        api_response = api_instance.delete_catch_all_v1(catchall_id)
        print("The response of MailCatchallsApi->delete_catch_all_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailCatchallsApi->delete_catch_all_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catchall_id** | **str**| Catch-all resource ID | 

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

# **list_catch_alls_v1**
> MailListCatchAllsV1200Response list_catch_alls_v1(order_id, page=page, per_page=per_page)

List catch-alls

Retrieve a paginated list of catch-alls across all mailboxes of a
mail order.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_list_catch_alls_v1200_response import MailListCatchAllsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailCatchallsApi(api_client)
    order_id = 'OR1a2b3c4d5e6f7g' # str | Order resource ID
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List catch-alls
        api_response = api_instance.list_catch_alls_v1(order_id, page=page, per_page=per_page)
        print("The response of MailCatchallsApi->list_catch_alls_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailCatchallsApi->list_catch_alls_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order resource ID | 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**MailListCatchAllsV1200Response**](MailListCatchAllsV1200Response.md)

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

# **resend_catch_all_confirmation_v1**
> CommonSuccessEmptyResource resend_catch_all_confirmation_v1(catchall_id)

Resend catch-all confirmation

Resend the confirmation email to the mailbox address of an
unconfirmed catch-all.

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
    api_instance = hostinger_api.MailCatchallsApi(api_client)
    catchall_id = 'CA1a2b3c4d5e6f7g' # str | Catch-all resource ID

    try:
        # Resend catch-all confirmation
        api_response = api_instance.resend_catch_all_confirmation_v1(catchall_id)
        print("The response of MailCatchallsApi->resend_catch_all_confirmation_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailCatchallsApi->resend_catch_all_confirmation_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catchall_id** | **str**| Catch-all resource ID | 

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
**409** | Error response |  -  |
**422** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

