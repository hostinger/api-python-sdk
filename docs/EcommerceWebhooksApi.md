# hostinger_api.EcommerceWebhooksApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_an_ecommerce_webhook_v1**](EcommerceWebhooksApi.md#create_an_ecommerce_webhook_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/webhooks | Create an ecommerce webhook
[**delete_an_ecommerce_webhook_v1**](EcommerceWebhooksApi.md#delete_an_ecommerce_webhook_v1) | **DELETE** /api/ecommerce/v1/stores/{store_id}/webhooks/{endpoint_id} | Delete an ecommerce webhook
[**get_an_ecommerce_webhook_v1**](EcommerceWebhooksApi.md#get_an_ecommerce_webhook_v1) | **GET** /api/ecommerce/v1/stores/{store_id}/webhooks/{endpoint_id} | Get an ecommerce webhook
[**list_ecommerce_webhooks_v1**](EcommerceWebhooksApi.md#list_ecommerce_webhooks_v1) | **GET** /api/ecommerce/v1/stores/{store_id}/webhooks | List ecommerce webhooks
[**rotate_an_ecommerce_webhook_secret_v1**](EcommerceWebhooksApi.md#rotate_an_ecommerce_webhook_secret_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/webhooks/{endpoint_id}/rotate-secret | Rotate an ecommerce webhook secret
[**update_an_ecommerce_webhook_v1**](EcommerceWebhooksApi.md#update_an_ecommerce_webhook_v1) | **PATCH** /api/ecommerce/v1/stores/{store_id}/webhooks/{endpoint_id} | Update an ecommerce webhook


# **create_an_ecommerce_webhook_v1**
> EcommerceV1WebhookWebhookCreationResource create_an_ecommerce_webhook_v1(store_id, ecommerce_v1_webhook_store_request)

Create an ecommerce webhook

Create an enabled subscription for your store to receive ecommerce events in external automation
systems. Save the whsec_ signing secret securely; it is returned once. Up to ten endpoints, including
disabled endpoints, may exist per store. Deliveries follow Standard Webhooks: verify the webhook-id,
webhook-timestamp and webhook-signature headers against the raw body with an official Standard Webhooks
library before parsing. Events can arrive out of order or more than once; deduplicate by event id.

400: the URL is not a public destination, or webhook_sales_channel_invalid (a channel ID does not
belong to this store). 409 codes: webhook_endpoint_limit_reached, webhook_store_inactive,
webhook_endpoint_catalog_busy (a catalog change is in progress; retry). Errors return the upstream code in
`message`, as `[Ecommerce:<code>] <reason>`.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_webhook_store_request import EcommerceV1WebhookStoreRequest
from hostinger_api.models.ecommerce_v1_webhook_webhook_creation_resource import EcommerceV1WebhookWebhookCreationResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceWebhooksApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | ID of the store owned by your account.
    ecommerce_v1_webhook_store_request = hostinger_api.EcommerceV1WebhookStoreRequest() # EcommerceV1WebhookStoreRequest | 

    try:
        # Create an ecommerce webhook
        api_response = api_instance.create_an_ecommerce_webhook_v1(store_id, ecommerce_v1_webhook_store_request)
        print("The response of EcommerceWebhooksApi->create_an_ecommerce_webhook_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceWebhooksApi->create_an_ecommerce_webhook_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| ID of the store owned by your account. | 
 **ecommerce_v1_webhook_store_request** | [**EcommerceV1WebhookStoreRequest**](EcommerceV1WebhookStoreRequest.md)|  | 

### Return type

[**EcommerceV1WebhookWebhookCreationResource**](EcommerceV1WebhookWebhookCreationResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created response |  -  |
**400** | Error response |  -  |
**401** | Unauthenticated response |  -  |
**409** | Conflict response. &#x60;Retry-After&#x60;, when present, is the number of seconds to wait before retrying. |  * Retry-After - Seconds to wait before retrying the request <br>  |
**422** | Validation error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_an_ecommerce_webhook_v1**
> CommonSuccessEmptyResource delete_an_ecommerce_webhook_v1(store_id, endpoint_id)

Delete an ecommerce webhook

Delete a subscription owned by your store, retaining delivery audit records.

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
    api_instance = hostinger_api.EcommerceWebhooksApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | ID of the store owned by your account.
    endpoint_id = 'whep_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | Webhook endpoint ID belonging to this store.

    try:
        # Delete an ecommerce webhook
        api_response = api_instance.delete_an_ecommerce_webhook_v1(store_id, endpoint_id)
        print("The response of EcommerceWebhooksApi->delete_an_ecommerce_webhook_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceWebhooksApi->delete_an_ecommerce_webhook_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| ID of the store owned by your account. | 
 **endpoint_id** | **str**| Webhook endpoint ID belonging to this store. | 

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
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_an_ecommerce_webhook_v1**
> EcommerceV1WebhookWebhookResource get_an_ecommerce_webhook_v1(store_id, endpoint_id)

Get an ecommerce webhook

Get a subscription owned by your store, without signing secrets.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_webhook_webhook_resource import EcommerceV1WebhookWebhookResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceWebhooksApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | ID of the store owned by your account.
    endpoint_id = 'whep_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | Webhook endpoint ID belonging to this store.

    try:
        # Get an ecommerce webhook
        api_response = api_instance.get_an_ecommerce_webhook_v1(store_id, endpoint_id)
        print("The response of EcommerceWebhooksApi->get_an_ecommerce_webhook_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceWebhooksApi->get_an_ecommerce_webhook_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| ID of the store owned by your account. | 
 **endpoint_id** | **str**| Webhook endpoint ID belonging to this store. | 

### Return type

[**EcommerceV1WebhookWebhookResource**](EcommerceV1WebhookWebhookResource.md)

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
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ecommerce_webhooks_v1**
> EcommerceV1WebhookWebhookListResource list_ecommerce_webhooks_v1(store_id)

List ecommerce webhooks

List your store's subscriptions for external automation systems, without signing secrets.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_webhook_webhook_list_resource import EcommerceV1WebhookWebhookListResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceWebhooksApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | ID of the store owned by your account.

    try:
        # List ecommerce webhooks
        api_response = api_instance.list_ecommerce_webhooks_v1(store_id)
        print("The response of EcommerceWebhooksApi->list_ecommerce_webhooks_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceWebhooksApi->list_ecommerce_webhooks_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| ID of the store owned by your account. | 

### Return type

[**EcommerceV1WebhookWebhookListResource**](EcommerceV1WebhookWebhookListResource.md)

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
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_an_ecommerce_webhook_secret_v1**
> EcommerceV1WebhookWebhookSecretResource rotate_an_ecommerce_webhook_secret_v1(store_id, endpoint_id)

Rotate an ecommerce webhook secret

Explicitly rotate the signing secret of an enabled endpoint on an active store. Save the new secret
securely. Prior secrets retain their original 24-hour overlap deadlines. Repeated calls create
distinct secrets, up to five live secrets. Wait for an old secret to expire at the limit. After a lost
response, explicitly rotate again; stored secrets cannot be retrieved. No daily renewal is required.

409 codes: webhook_endpoint_disabled (endpoint is disabled or revoked), webhook_store_inactive,
webhook_secret_rotation_limit_reached (five live secrets). Errors return the upstream code in
`message`, as `[Ecommerce:<code>] <reason>`.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_webhook_webhook_secret_resource import EcommerceV1WebhookWebhookSecretResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceWebhooksApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | ID of the store owned by your account.
    endpoint_id = 'whep_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | Webhook endpoint ID belonging to this store.

    try:
        # Rotate an ecommerce webhook secret
        api_response = api_instance.rotate_an_ecommerce_webhook_secret_v1(store_id, endpoint_id)
        print("The response of EcommerceWebhooksApi->rotate_an_ecommerce_webhook_secret_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceWebhooksApi->rotate_an_ecommerce_webhook_secret_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| ID of the store owned by your account. | 
 **endpoint_id** | **str**| Webhook endpoint ID belonging to this store. | 

### Return type

[**EcommerceV1WebhookWebhookSecretResource**](EcommerceV1WebhookWebhookSecretResource.md)

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
**409** | Conflict response. &#x60;Retry-After&#x60;, when present, is the number of seconds to wait before retrying. |  * Retry-After - Seconds to wait before retrying the request <br>  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_an_ecommerce_webhook_v1**
> EcommerceV1WebhookWebhookResource update_an_ecommerce_webhook_v1(store_id, endpoint_id, ecommerce_v1_webhook_update_request)

Update an ecommerce webhook

Change the receiver, events, channel filter or enabled state. Omitted fields are preserved; a null
channel filter restores store-wide delivery. Endpoints disabled automatically after a 410 Gone
(receiver_gone) or persistent delivery failures (receiver_failing) resume with enabled: true; events
from the disabled period are not sent. Lifecycle-revoked endpoints cannot be enabled again: delete
them and create fresh subscriptions after recovery.

400 codes: webhook_destination_not_allowed (the new URL, or the saved URL when enabling, is not a public
destination), webhook_sales_channel_invalid. 409 codes: webhook_endpoint_revoked, webhook_store_inactive,
webhook_endpoint_catalog_busy (retry). Errors return the upstream code in `message`, as
`[Ecommerce:<code>] <reason>`.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_webhook_update_request import EcommerceV1WebhookUpdateRequest
from hostinger_api.models.ecommerce_v1_webhook_webhook_resource import EcommerceV1WebhookWebhookResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommerceWebhooksApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | ID of the store owned by your account.
    endpoint_id = 'whep_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | Webhook endpoint ID belonging to this store.
    ecommerce_v1_webhook_update_request = hostinger_api.EcommerceV1WebhookUpdateRequest() # EcommerceV1WebhookUpdateRequest | 

    try:
        # Update an ecommerce webhook
        api_response = api_instance.update_an_ecommerce_webhook_v1(store_id, endpoint_id, ecommerce_v1_webhook_update_request)
        print("The response of EcommerceWebhooksApi->update_an_ecommerce_webhook_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommerceWebhooksApi->update_an_ecommerce_webhook_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| ID of the store owned by your account. | 
 **endpoint_id** | **str**| Webhook endpoint ID belonging to this store. | 
 **ecommerce_v1_webhook_update_request** | [**EcommerceV1WebhookUpdateRequest**](EcommerceV1WebhookUpdateRequest.md)|  | 

### Return type

[**EcommerceV1WebhookWebhookResource**](EcommerceV1WebhookWebhookResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**400** | Error response |  -  |
**401** | Unauthenticated response |  -  |
**404** | Error response |  -  |
**409** | Conflict response. &#x60;Retry-After&#x60;, when present, is the number of seconds to wait before retrying. |  * Retry-After - Seconds to wait before retrying the request <br>  |
**422** | Validation error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

