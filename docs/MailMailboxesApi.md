# hostinger_api.MailMailboxesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mailbox_v1**](MailMailboxesApi.md#create_mailbox_v1) | **POST** /api/mail/v1/orders/{orderId}/mailboxes | Create mailbox
[**get_mailbox_list_v1**](MailMailboxesApi.md#get_mailbox_list_v1) | **GET** /api/mail/v1/orders/{orderId}/mailboxes | Get mailbox list


# **create_mailbox_v1**
> MailV1MailboxesMailboxResource create_mailbox_v1(order_id, mail_v1_schema_create_mailbox_request_schema)

Create mailbox

Create a mailbox under the given mail order. The full email address is
composed from the given local part and the domain of the order.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_v1_mailboxes_mailbox_resource import MailV1MailboxesMailboxResource
from hostinger_api.models.mail_v1_schema_create_mailbox_request_schema import MailV1SchemaCreateMailboxRequestSchema
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailMailboxesApi(api_client)
    order_id = 'OR1a2b3c4d5e6f7g' # str | Order resource ID
    mail_v1_schema_create_mailbox_request_schema = hostinger_api.MailV1SchemaCreateMailboxRequestSchema() # MailV1SchemaCreateMailboxRequestSchema | 

    try:
        # Create mailbox
        api_response = api_instance.create_mailbox_v1(order_id, mail_v1_schema_create_mailbox_request_schema)
        print("The response of MailMailboxesApi->create_mailbox_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailMailboxesApi->create_mailbox_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order resource ID | 
 **mail_v1_schema_create_mailbox_request_schema** | [**MailV1SchemaCreateMailboxRequestSchema**](MailV1SchemaCreateMailboxRequestSchema.md)|  | 

### Return type

[**MailV1MailboxesMailboxResource**](MailV1MailboxesMailboxResource.md)

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

# **get_mailbox_list_v1**
> MailGetMailboxListV1200Response get_mailbox_list_v1(order_id, search=search, sort=sort, page=page, per_page=per_page)

Get mailbox list

Retrieve a paginated list of mailboxes belonging to a mail order.

Use this endpoint to monitor mailboxes of your mail service, including
their status, enabled protocols, attached resource counts, and
periodically synced usage numbers (usage may lag behind live values).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_get_mailbox_list_v1200_response import MailGetMailboxListV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailMailboxesApi(api_client)
    order_id = 'OR1a2b3c4d5e6f7g' # str | Order resource ID
    search = 'info' # str | Filter mailboxes whose email address contains the given string (optional)
    sort = address # str | Sort mailboxes by field. Prefix with `-` for descending order. (optional) (default to address)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # Get mailbox list
        api_response = api_instance.get_mailbox_list_v1(order_id, search=search, sort=sort, page=page, per_page=per_page)
        print("The response of MailMailboxesApi->get_mailbox_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailMailboxesApi->get_mailbox_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order resource ID | 
 **search** | **str**| Filter mailboxes whose email address contains the given string | [optional] 
 **sort** | **str**| Sort mailboxes by field. Prefix with &#x60;-&#x60; for descending order. | [optional] [default to address]
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**MailGetMailboxListV1200Response**](MailGetMailboxListV1200Response.md)

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

