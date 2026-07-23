# hostinger_api.MailLogsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_access_logs_v1**](MailLogsApi.md#list_access_logs_v1) | **GET** /api/mail/v1/orders/{orderId}/logs/access | List access logs
[**list_action_logs_v1**](MailLogsApi.md#list_action_logs_v1) | **GET** /api/mail/v1/orders/{orderId}/logs/action | List action logs
[**list_inbound_logs_v1**](MailLogsApi.md#list_inbound_logs_v1) | **GET** /api/mail/v1/orders/{orderId}/logs/inbound | List inbound logs
[**list_mailbox_action_logs_v1**](MailLogsApi.md#list_mailbox_action_logs_v1) | **GET** /api/mail/v1/orders/{orderId}/logs/mailbox-actions | List mailbox action logs
[**list_outbound_logs_v1**](MailLogsApi.md#list_outbound_logs_v1) | **GET** /api/mail/v1/orders/{orderId}/logs/outbound | List outbound logs


# **list_access_logs_v1**
> MailListAccessLogsV1200Response list_access_logs_v1(order_id, account=account, var_date=var_date, from_date=from_date, to_date=to_date, status=status, protocol=protocol, has_deletions=has_deletions, page=page, per_page=per_page)

List access logs

Retrieve paginated access logs for the domain attached to the given
mail order. Supports filtering by account, date range, protocol,
status, and deletion flag. Results are sorted by timestamp descending.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_list_access_logs_v1200_response import MailListAccessLogsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailLogsApi(api_client)
    order_id = 'OR1a2b3c4d5e6f7g' # str | Order resource ID
    account = 'user@example.com' # str | Filter log entries by a specific email account (optional)
    var_date = 'Mon Mar 16 00:00:00 UTC 2026' # date | Exact date filter (YYYY-MM-DD). Takes precedence over `from_date`/`to_date` when both are given. (optional)
    from_date = '2026-03-01T00:00Z' # datetime | Date range start (RFC 3339) (optional)
    to_date = '2026-03-31T23:59:59Z' # datetime | Date range end (RFC 3339) (optional)
    status = 'Successful' # str | Filter log entries by status (optional)
    protocol = 'imap' # str | Filter access log entries by protocol (optional)
    has_deletions = false # bool | Filter access log entries by whether the session had deletions (optional)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List access logs
        api_response = api_instance.list_access_logs_v1(order_id, account=account, var_date=var_date, from_date=from_date, to_date=to_date, status=status, protocol=protocol, has_deletions=has_deletions, page=page, per_page=per_page)
        print("The response of MailLogsApi->list_access_logs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailLogsApi->list_access_logs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order resource ID | 
 **account** | **str**| Filter log entries by a specific email account | [optional] 
 **var_date** | **date**| Exact date filter (YYYY-MM-DD). Takes precedence over &#x60;from_date&#x60;/&#x60;to_date&#x60; when both are given. | [optional] 
 **from_date** | **datetime**| Date range start (RFC 3339) | [optional] 
 **to_date** | **datetime**| Date range end (RFC 3339) | [optional] 
 **status** | **str**| Filter log entries by status | [optional] 
 **protocol** | **str**| Filter access log entries by protocol | [optional] 
 **has_deletions** | **bool**| Filter access log entries by whether the session had deletions | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**MailListAccessLogsV1200Response**](MailListAccessLogsV1200Response.md)

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

# **list_action_logs_v1**
> MailListActionLogsV1200Response list_action_logs_v1(order_id, account=account, var_date=var_date, from_date=from_date, to_date=to_date, status=status, page=page, per_page=per_page)

List action logs

Retrieve paginated account action logs (administrative and user
actions) for the given mail order. Supports filtering by account,
date range, and status. Results are sorted by timestamp descending.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_list_action_logs_v1200_response import MailListActionLogsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailLogsApi(api_client)
    order_id = 'OR1a2b3c4d5e6f7g' # str | Order resource ID
    account = 'user@example.com' # str | Filter log entries by a specific email account (optional)
    var_date = 'Mon Mar 16 00:00:00 UTC 2026' # date | Exact date filter (YYYY-MM-DD). Takes precedence over `from_date`/`to_date` when both are given. (optional)
    from_date = '2026-03-01T00:00Z' # datetime | Date range start (RFC 3339) (optional)
    to_date = '2026-03-31T23:59:59Z' # datetime | Date range end (RFC 3339) (optional)
    status = 'Successful' # str | Filter log entries by status (optional)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List action logs
        api_response = api_instance.list_action_logs_v1(order_id, account=account, var_date=var_date, from_date=from_date, to_date=to_date, status=status, page=page, per_page=per_page)
        print("The response of MailLogsApi->list_action_logs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailLogsApi->list_action_logs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order resource ID | 
 **account** | **str**| Filter log entries by a specific email account | [optional] 
 **var_date** | **date**| Exact date filter (YYYY-MM-DD). Takes precedence over &#x60;from_date&#x60;/&#x60;to_date&#x60; when both are given. | [optional] 
 **from_date** | **datetime**| Date range start (RFC 3339) | [optional] 
 **to_date** | **datetime**| Date range end (RFC 3339) | [optional] 
 **status** | **str**| Filter log entries by status | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**MailListActionLogsV1200Response**](MailListActionLogsV1200Response.md)

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

# **list_inbound_logs_v1**
> MailListInboundLogsV1200Response list_inbound_logs_v1(order_id, account=account, var_date=var_date, from_date=from_date, to_date=to_date, status=status, sender=sender, recipient=recipient, page=page, per_page=per_page)

List inbound logs

Retrieve paginated inbound (received mail) delivery logs for the
domain attached to the given mail order. Supports filtering by
account, date range, status, sender, and recipient. Results are
sorted by timestamp descending.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_list_inbound_logs_v1200_response import MailListInboundLogsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailLogsApi(api_client)
    order_id = 'OR1a2b3c4d5e6f7g' # str | Order resource ID
    account = 'user@example.com' # str | Filter log entries by a specific email account (optional)
    var_date = 'Mon Mar 16 00:00:00 UTC 2026' # date | Exact date filter (YYYY-MM-DD). Takes precedence over `from_date`/`to_date` when both are given. (optional)
    from_date = '2026-03-01T00:00Z' # datetime | Date range start (RFC 3339) (optional)
    to_date = '2026-03-31T23:59:59Z' # datetime | Date range end (RFC 3339) (optional)
    status = 'Successful' # str | Filter log entries by status (optional)
    sender = 'user@example.com' # str | Filter log entries by sender. Accepts a full email address or a domain. (optional)
    recipient = 'recipient.com' # str | Filter log entries by recipient. Accepts a full email address or a domain. (optional)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List inbound logs
        api_response = api_instance.list_inbound_logs_v1(order_id, account=account, var_date=var_date, from_date=from_date, to_date=to_date, status=status, sender=sender, recipient=recipient, page=page, per_page=per_page)
        print("The response of MailLogsApi->list_inbound_logs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailLogsApi->list_inbound_logs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order resource ID | 
 **account** | **str**| Filter log entries by a specific email account | [optional] 
 **var_date** | **date**| Exact date filter (YYYY-MM-DD). Takes precedence over &#x60;from_date&#x60;/&#x60;to_date&#x60; when both are given. | [optional] 
 **from_date** | **datetime**| Date range start (RFC 3339) | [optional] 
 **to_date** | **datetime**| Date range end (RFC 3339) | [optional] 
 **status** | **str**| Filter log entries by status | [optional] 
 **sender** | **str**| Filter log entries by sender. Accepts a full email address or a domain. | [optional] 
 **recipient** | **str**| Filter log entries by recipient. Accepts a full email address or a domain. | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**MailListInboundLogsV1200Response**](MailListInboundLogsV1200Response.md)

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

# **list_mailbox_action_logs_v1**
> MailListMailboxActionLogsV1200Response list_mailbox_action_logs_v1(order_id, email, var_date=var_date, from_date=from_date, to_date=to_date, event=event, page=page, per_page=per_page)

List mailbox action logs

Retrieve paginated mailbox action logs (message and mailbox events)
for a mailbox in the given mail order. The mailbox email must belong
to the order's domain. Supports date range and event type filters.
Results are sorted by timestamp descending.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_list_mailbox_action_logs_v1200_response import MailListMailboxActionLogsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailLogsApi(api_client)
    order_id = 'OR1a2b3c4d5e6f7g' # str | Order resource ID
    email = 'user@example.com' # str | Mailbox email address. Must belong to the order's domain.
    var_date = 'Mon Mar 16 00:00:00 UTC 2026' # date | Exact date filter (YYYY-MM-DD). Takes precedence over `from_date`/`to_date` when both are given. (optional)
    from_date = '2026-03-01T00:00Z' # datetime | Date range start (RFC 3339) (optional)
    to_date = '2026-03-31T23:59:59Z' # datetime | Date range end (RFC 3339) (optional)
    event = 'MessageNew' # str | Filter mailbox action log entries by event type (optional)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List mailbox action logs
        api_response = api_instance.list_mailbox_action_logs_v1(order_id, email, var_date=var_date, from_date=from_date, to_date=to_date, event=event, page=page, per_page=per_page)
        print("The response of MailLogsApi->list_mailbox_action_logs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailLogsApi->list_mailbox_action_logs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order resource ID | 
 **email** | **str**| Mailbox email address. Must belong to the order&#39;s domain. | 
 **var_date** | **date**| Exact date filter (YYYY-MM-DD). Takes precedence over &#x60;from_date&#x60;/&#x60;to_date&#x60; when both are given. | [optional] 
 **from_date** | **datetime**| Date range start (RFC 3339) | [optional] 
 **to_date** | **datetime**| Date range end (RFC 3339) | [optional] 
 **event** | **str**| Filter mailbox action log entries by event type | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**MailListMailboxActionLogsV1200Response**](MailListMailboxActionLogsV1200Response.md)

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

# **list_outbound_logs_v1**
> MailListInboundLogsV1200Response list_outbound_logs_v1(order_id, account=account, var_date=var_date, from_date=from_date, to_date=to_date, status=status, sender=sender, recipient=recipient, page=page, per_page=per_page)

List outbound logs

Retrieve paginated outbound (sent mail) delivery logs for the domain
attached to the given mail order. Supports filtering by account, date
range, status, sender, and recipient. Results are sorted by timestamp
descending.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_list_inbound_logs_v1200_response import MailListInboundLogsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailLogsApi(api_client)
    order_id = 'OR1a2b3c4d5e6f7g' # str | Order resource ID
    account = 'user@example.com' # str | Filter log entries by a specific email account (optional)
    var_date = 'Mon Mar 16 00:00:00 UTC 2026' # date | Exact date filter (YYYY-MM-DD). Takes precedence over `from_date`/`to_date` when both are given. (optional)
    from_date = '2026-03-01T00:00Z' # datetime | Date range start (RFC 3339) (optional)
    to_date = '2026-03-31T23:59:59Z' # datetime | Date range end (RFC 3339) (optional)
    status = 'Successful' # str | Filter log entries by status (optional)
    sender = 'user@example.com' # str | Filter log entries by sender. Accepts a full email address or a domain. (optional)
    recipient = 'recipient.com' # str | Filter log entries by recipient. Accepts a full email address or a domain. (optional)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List outbound logs
        api_response = api_instance.list_outbound_logs_v1(order_id, account=account, var_date=var_date, from_date=from_date, to_date=to_date, status=status, sender=sender, recipient=recipient, page=page, per_page=per_page)
        print("The response of MailLogsApi->list_outbound_logs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailLogsApi->list_outbound_logs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order resource ID | 
 **account** | **str**| Filter log entries by a specific email account | [optional] 
 **var_date** | **date**| Exact date filter (YYYY-MM-DD). Takes precedence over &#x60;from_date&#x60;/&#x60;to_date&#x60; when both are given. | [optional] 
 **from_date** | **datetime**| Date range start (RFC 3339) | [optional] 
 **to_date** | **datetime**| Date range end (RFC 3339) | [optional] 
 **status** | **str**| Filter log entries by status | [optional] 
 **sender** | **str**| Filter log entries by sender. Accepts a full email address or a domain. | [optional] 
 **recipient** | **str**| Filter log entries by recipient. Accepts a full email address or a domain. | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**MailListInboundLogsV1200Response**](MailListInboundLogsV1200Response.md)

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

