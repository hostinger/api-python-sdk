# hostinger_api.MailWebhooksApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook_v1**](MailWebhooksApi.md#create_webhook_v1) | **POST** /api/mail/v1/mailboxes/{mailboxId}/webhooks | Create webhook
[**delete_webhook_v1**](MailWebhooksApi.md#delete_webhook_v1) | **DELETE** /api/mail/v1/webhooks/{webhookId} | Delete webhook
[**get_webhook_v1**](MailWebhooksApi.md#get_webhook_v1) | **GET** /api/mail/v1/webhooks/{webhookId} | Get webhook
[**list_webhook_delivery_logs_v1**](MailWebhooksApi.md#list_webhook_delivery_logs_v1) | **GET** /api/mail/v1/orders/{orderId}/webhooks/delivery-logs | List webhook delivery logs
[**list_webhooks_v1**](MailWebhooksApi.md#list_webhooks_v1) | **GET** /api/mail/v1/orders/{orderId}/webhooks | List webhooks
[**regenerate_webhook_secret_v1**](MailWebhooksApi.md#regenerate_webhook_secret_v1) | **POST** /api/mail/v1/webhooks/{webhookId}/regenerate-secret | Regenerate webhook secret
[**test_webhook_v1**](MailWebhooksApi.md#test_webhook_v1) | **POST** /api/mail/v1/webhooks/{webhookId}/test | Test webhook
[**update_webhook_v1**](MailWebhooksApi.md#update_webhook_v1) | **PATCH** /api/mail/v1/webhooks/{webhookId} | Update webhook


# **create_webhook_v1**
> MailV1WebhooksWebhookCreatedResource create_webhook_v1(mailbox_id, mail_v1_schema_create_webhook_request_schema)

Create webhook

Create a webhook for the given mailbox. The generated secret is
returned only in this response and is sent as a bearer token with
every delivery.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_v1_schema_create_webhook_request_schema import MailV1SchemaCreateWebhookRequestSchema
from hostinger_api.models.mail_v1_webhooks_webhook_created_resource import MailV1WebhooksWebhookCreatedResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailWebhooksApi(api_client)
    mailbox_id = 'AC1a2b3c4d5e6f7g' # str | Mailbox resource ID
    mail_v1_schema_create_webhook_request_schema = hostinger_api.MailV1SchemaCreateWebhookRequestSchema() # MailV1SchemaCreateWebhookRequestSchema | 

    try:
        # Create webhook
        api_response = api_instance.create_webhook_v1(mailbox_id, mail_v1_schema_create_webhook_request_schema)
        print("The response of MailWebhooksApi->create_webhook_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailWebhooksApi->create_webhook_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox_id** | **str**| Mailbox resource ID | 
 **mail_v1_schema_create_webhook_request_schema** | [**MailV1SchemaCreateWebhookRequestSchema**](MailV1SchemaCreateWebhookRequestSchema.md)|  | 

### Return type

[**MailV1WebhooksWebhookCreatedResource**](MailV1WebhooksWebhookCreatedResource.md)

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

# **delete_webhook_v1**
> CommonSuccessEmptyResource delete_webhook_v1(webhook_id)

Delete webhook

Permanently delete a webhook. This action cannot be undone. After
deletion the URL no longer receives event notifications.

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
    api_instance = hostinger_api.MailWebhooksApi(api_client)
    webhook_id = '019683f8-1234-7abc-8def-0123456789ab' # str | Webhook ID (returned when the webhook was created)

    try:
        # Delete webhook
        api_response = api_instance.delete_webhook_v1(webhook_id)
        print("The response of MailWebhooksApi->delete_webhook_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailWebhooksApi->delete_webhook_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Webhook ID (returned when the webhook was created) | 

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

# **get_webhook_v1**
> MailV1WebhooksWebhookResource get_webhook_v1(webhook_id)

Get webhook

Retrieve the details of a single webhook. The webhook secret is never
included; it is returned only when a webhook is created or its secret
is regenerated.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_v1_webhooks_webhook_resource import MailV1WebhooksWebhookResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailWebhooksApi(api_client)
    webhook_id = '019683f8-1234-7abc-8def-0123456789ab' # str | Webhook ID (returned when the webhook was created)

    try:
        # Get webhook
        api_response = api_instance.get_webhook_v1(webhook_id)
        print("The response of MailWebhooksApi->get_webhook_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailWebhooksApi->get_webhook_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Webhook ID (returned when the webhook was created) | 

### Return type

[**MailV1WebhooksWebhookResource**](MailV1WebhooksWebhookResource.md)

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

# **list_webhook_delivery_logs_v1**
> MailListWebhookDeliveryLogsV1200Response list_webhook_delivery_logs_v1(order_id, mailbox_id=mailbox_id, page=page, per_page=per_page)

List webhook delivery logs

Retrieve a paginated list of webhook delivery logs for the given mail
order, including delivery outcome, duration, and retry counts.
Supports filtering by mailbox.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_list_webhook_delivery_logs_v1200_response import MailListWebhookDeliveryLogsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailWebhooksApi(api_client)
    order_id = 'OR1a2b3c4d5e6f7g' # str | Order resource ID
    mailbox_id = 'AC1a2b3c4d5e6f7g' # str | Filter by the mailbox resource ID the webhooks are attached to (optional)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List webhook delivery logs
        api_response = api_instance.list_webhook_delivery_logs_v1(order_id, mailbox_id=mailbox_id, page=page, per_page=per_page)
        print("The response of MailWebhooksApi->list_webhook_delivery_logs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailWebhooksApi->list_webhook_delivery_logs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order resource ID | 
 **mailbox_id** | **str**| Filter by the mailbox resource ID the webhooks are attached to | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**MailListWebhookDeliveryLogsV1200Response**](MailListWebhookDeliveryLogsV1200Response.md)

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

# **list_webhooks_v1**
> MailListWebhooksV1200Response list_webhooks_v1(order_id, mailbox_id=mailbox_id, status=status, page=page, per_page=per_page)

List webhooks

Retrieve a paginated list of webhooks belonging to the given mail
order. Supports filtering by mailbox and status. The webhook secret
is never included; it is returned only when a webhook is created or
its secret is regenerated.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_list_webhooks_v1200_response import MailListWebhooksV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailWebhooksApi(api_client)
    order_id = 'OR1a2b3c4d5e6f7g' # str | Order resource ID
    mailbox_id = 'AC1a2b3c4d5e6f7g' # str | Filter by the mailbox resource ID the webhooks are attached to (optional)
    status = 'active' # str | Filter webhooks by status (optional)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List webhooks
        api_response = api_instance.list_webhooks_v1(order_id, mailbox_id=mailbox_id, status=status, page=page, per_page=per_page)
        print("The response of MailWebhooksApi->list_webhooks_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailWebhooksApi->list_webhooks_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order resource ID | 
 **mailbox_id** | **str**| Filter by the mailbox resource ID the webhooks are attached to | [optional] 
 **status** | **str**| Filter webhooks by status | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**MailListWebhooksV1200Response**](MailListWebhooksV1200Response.md)

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

# **regenerate_webhook_secret_v1**
> MailV1WebhooksWebhookSecretResource regenerate_webhook_secret_v1(webhook_id)

Regenerate webhook secret

Regenerate the secret of a webhook. The previous secret is
immediately invalidated. The new secret is returned only in this
response and is sent as a bearer token with every delivery.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_v1_webhooks_webhook_secret_resource import MailV1WebhooksWebhookSecretResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailWebhooksApi(api_client)
    webhook_id = '019683f8-1234-7abc-8def-0123456789ab' # str | Webhook ID (returned when the webhook was created)

    try:
        # Regenerate webhook secret
        api_response = api_instance.regenerate_webhook_secret_v1(webhook_id)
        print("The response of MailWebhooksApi->regenerate_webhook_secret_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailWebhooksApi->regenerate_webhook_secret_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Webhook ID (returned when the webhook was created) | 

### Return type

[**MailV1WebhooksWebhookSecretResource**](MailV1WebhooksWebhookSecretResource.md)

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

# **test_webhook_v1**
> MailV1WebhooksWebhookTestResultResource test_webhook_v1(webhook_id)

Test webhook

Send a test delivery to the webhook URL and return the result. Test
requests are rate limited upstream.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_v1_webhooks_webhook_test_result_resource import MailV1WebhooksWebhookTestResultResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailWebhooksApi(api_client)
    webhook_id = '019683f8-1234-7abc-8def-0123456789ab' # str | Webhook ID (returned when the webhook was created)

    try:
        # Test webhook
        api_response = api_instance.test_webhook_v1(webhook_id)
        print("The response of MailWebhooksApi->test_webhook_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailWebhooksApi->test_webhook_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Webhook ID (returned when the webhook was created) | 

### Return type

[**MailV1WebhooksWebhookTestResultResource**](MailV1WebhooksWebhookTestResultResource.md)

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
**429** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_v1**
> MailV1WebhooksWebhookResource update_webhook_v1(webhook_id, mail_v1_schema_update_webhook_request_schema)

Update webhook

Partially update a webhook. Only the fields included in the request
body are changed; omitted fields retain their current values. Pass
`"description": null` to clear the description.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.mail_v1_schema_update_webhook_request_schema import MailV1SchemaUpdateWebhookRequestSchema
from hostinger_api.models.mail_v1_webhooks_webhook_resource import MailV1WebhooksWebhookResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.MailWebhooksApi(api_client)
    webhook_id = '019683f8-1234-7abc-8def-0123456789ab' # str | Webhook ID (returned when the webhook was created)
    mail_v1_schema_update_webhook_request_schema = hostinger_api.MailV1SchemaUpdateWebhookRequestSchema() # MailV1SchemaUpdateWebhookRequestSchema | 

    try:
        # Update webhook
        api_response = api_instance.update_webhook_v1(webhook_id, mail_v1_schema_update_webhook_request_schema)
        print("The response of MailWebhooksApi->update_webhook_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailWebhooksApi->update_webhook_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Webhook ID (returned when the webhook was created) | 
 **mail_v1_schema_update_webhook_request_schema** | [**MailV1SchemaUpdateWebhookRequestSchema**](MailV1SchemaUpdateWebhookRequestSchema.md)|  | 

### Return type

[**MailV1WebhooksWebhookResource**](MailV1WebhooksWebhookResource.md)

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
**400** | Error response |  -  |
**404** | Error response |  -  |
**422** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

