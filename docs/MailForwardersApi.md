# hostinger_api.MailForwardersApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_forwarder_v1**](MailForwardersApi.md#create_forwarder_v1) | **POST** /api/mail/v1/mailboxes/{mailboxId}/forwarders | Create forwarder
[**delete_forwarder_v1**](MailForwardersApi.md#delete_forwarder_v1) | **DELETE** /api/mail/v1/forwarders/{forwarderId} | Delete forwarder
[**list_forwarders_v1**](MailForwardersApi.md#list_forwarders_v1) | **GET** /api/mail/v1/orders/{orderId}/forwarders | List forwarders
[**resend_forwarder_confirmation_v1**](MailForwardersApi.md#resend_forwarder_confirmation_v1) | **POST** /api/mail/v1/forwarders/{forwarderId}/confirmation/resend | Resend forwarder confirmation
[**update_forwarder_keep_copy_setting_v1**](MailForwardersApi.md#update_forwarder_keep_copy_setting_v1) | **PATCH** /api/mail/v1/forwarders/{forwarderId}/keep-copy | Update forwarder keep-copy setting


# **create_forwarder_v1**
> MailV1ForwardersForwarderResource create_forwarder_v1(mailbox_id, mail_v1_schema_create_forwarder_request_schema)

Create forwarder

Create a forwarder from the given mailbox to the destination address.
The destination receives a confirmation email and forwarding becomes
active only after it is confirmed.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_v1_forwarders_forwarder_resource import MailV1ForwardersForwarderResource
from hostinger_api.models.mail_v1_schema_create_forwarder_request_schema import MailV1SchemaCreateForwarderRequestSchema
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailForwardersApi(api_client)
    mailbox_id = 'AC1a2b3c4d5e6f7g' # str | Mailbox resource ID
    mail_v1_schema_create_forwarder_request_schema = hostinger_api.MailV1SchemaCreateForwarderRequestSchema() # MailV1SchemaCreateForwarderRequestSchema | 

    try:
        # Create forwarder
        api_response = api_instance.create_forwarder_v1(mailbox_id, mail_v1_schema_create_forwarder_request_schema)
        print("The response of MailForwardersApi->create_forwarder_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailForwardersApi->create_forwarder_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox_id** | **str**| Mailbox resource ID | 
 **mail_v1_schema_create_forwarder_request_schema** | [**MailV1SchemaCreateForwarderRequestSchema**](MailV1SchemaCreateForwarderRequestSchema.md)|  | 

### Return type

[**MailV1ForwardersForwarderResource**](MailV1ForwardersForwarderResource.md)

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
**400** | Error response |  -  |
**404** | Error response |  -  |
**409** | Error response |  -  |
**422** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_forwarder_v1**
> CommonSuccessEmptyResource delete_forwarder_v1(forwarder_id)

Delete forwarder

Delete a forwarder. The mailbox stops forwarding messages to the
destination address immediately.

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
    api_instance = hostinger_api.MailForwardersApi(api_client)
    forwarder_id = 'FW1a2b3c4d5e6f7g' # str | Forwarder resource ID

    try:
        # Delete forwarder
        api_response = api_instance.delete_forwarder_v1(forwarder_id)
        print("The response of MailForwardersApi->delete_forwarder_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailForwardersApi->delete_forwarder_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forwarder_id** | **str**| Forwarder resource ID | 

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

# **list_forwarders_v1**
> MailListForwardersV1200Response list_forwarders_v1(order_id, page=page, per_page=per_page)

List forwarders

Retrieve a paginated list of forwarders across all mailboxes of a
mail order.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_list_forwarders_v1200_response import MailListForwardersV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailForwardersApi(api_client)
    order_id = 'OR1a2b3c4d5e6f7g' # str | Order resource ID
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List forwarders
        api_response = api_instance.list_forwarders_v1(order_id, page=page, per_page=per_page)
        print("The response of MailForwardersApi->list_forwarders_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailForwardersApi->list_forwarders_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order resource ID | 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**MailListForwardersV1200Response**](MailListForwardersV1200Response.md)

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

# **resend_forwarder_confirmation_v1**
> CommonSuccessEmptyResource resend_forwarder_confirmation_v1(forwarder_id)

Resend forwarder confirmation

Resend the confirmation email to the destination address of an
unconfirmed forwarder.

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
    api_instance = hostinger_api.MailForwardersApi(api_client)
    forwarder_id = 'FW1a2b3c4d5e6f7g' # str | Forwarder resource ID

    try:
        # Resend forwarder confirmation
        api_response = api_instance.resend_forwarder_confirmation_v1(forwarder_id)
        print("The response of MailForwardersApi->resend_forwarder_confirmation_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailForwardersApi->resend_forwarder_confirmation_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forwarder_id** | **str**| Forwarder resource ID | 

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

# **update_forwarder_keep_copy_setting_v1**
> CommonSuccessEmptyResource update_forwarder_keep_copy_setting_v1(forwarder_id, mail_v1_schema_update_forwarder_keep_copy_request_schema)

Update forwarder keep-copy setting

Enable or disable keeping a copy of forwarded messages in the
mailbox.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.mail_v1_schema_update_forwarder_keep_copy_request_schema import MailV1SchemaUpdateForwarderKeepCopyRequestSchema
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailForwardersApi(api_client)
    forwarder_id = 'FW1a2b3c4d5e6f7g' # str | Forwarder resource ID
    mail_v1_schema_update_forwarder_keep_copy_request_schema = hostinger_api.MailV1SchemaUpdateForwarderKeepCopyRequestSchema() # MailV1SchemaUpdateForwarderKeepCopyRequestSchema | 

    try:
        # Update forwarder keep-copy setting
        api_response = api_instance.update_forwarder_keep_copy_setting_v1(forwarder_id, mail_v1_schema_update_forwarder_keep_copy_request_schema)
        print("The response of MailForwardersApi->update_forwarder_keep_copy_setting_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailForwardersApi->update_forwarder_keep_copy_setting_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forwarder_id** | **str**| Forwarder resource ID | 
 **mail_v1_schema_update_forwarder_keep_copy_request_schema** | [**MailV1SchemaUpdateForwarderKeepCopyRequestSchema**](MailV1SchemaUpdateForwarderKeepCopyRequestSchema.md)|  | 

### Return type

[**CommonSuccessEmptyResource**](CommonSuccessEmptyResource.md)

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

