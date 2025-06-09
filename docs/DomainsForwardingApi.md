# hostinger_api.DomainsForwardingApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_forwarding_data_v1**](DomainsForwardingApi.md#create_forwarding_data_v1) | **POST** /api/domains/v1/forwarding | Create forwarding data
[**delete_forwarding_data_v1**](DomainsForwardingApi.md#delete_forwarding_data_v1) | **DELETE** /api/domains/v1/forwarding/{domain} | Delete forwarding data
[**get_forwarding_data_v1**](DomainsForwardingApi.md#get_forwarding_data_v1) | **GET** /api/domains/v1/forwarding/{domain} | Get forwarding data


# **create_forwarding_data_v1**
> DomainsV1ForwardingForwardingResource create_forwarding_data_v1(domains_v1_forwarding_store_request)

Create forwarding data

This endpoint creates domain forwarding data.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domains_v1_forwarding_forwarding_resource import DomainsV1ForwardingForwardingResource
from hostinger_api.models.domains_v1_forwarding_store_request import DomainsV1ForwardingStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsForwardingApi(api_client)
    domains_v1_forwarding_store_request = hostinger_api.DomainsV1ForwardingStoreRequest() # DomainsV1ForwardingStoreRequest | 

    try:
        # Create forwarding data
        api_response = api_instance.create_forwarding_data_v1(domains_v1_forwarding_store_request)
        print("The response of DomainsForwardingApi->create_forwarding_data_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsForwardingApi->create_forwarding_data_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains_v1_forwarding_store_request** | [**DomainsV1ForwardingStoreRequest**](DomainsV1ForwardingStoreRequest.md)|  | 

### Return type

[**DomainsV1ForwardingForwardingResource**](DomainsV1ForwardingForwardingResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_forwarding_data_v1**
> CommonSuccessEmptyResource delete_forwarding_data_v1(domain)

Delete forwarding data

This endpoint deletes domain forwarding data.

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
    api_instance = hostinger_api.DomainsForwardingApi(api_client)
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Delete forwarding data
        api_response = api_instance.delete_forwarding_data_v1(domain)
        print("The response of DomainsForwardingApi->delete_forwarding_data_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsForwardingApi->delete_forwarding_data_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 

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
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forwarding_data_v1**
> DomainsV1ForwardingForwardingResource get_forwarding_data_v1(domain)

Get forwarding data

This endpoint retrieves domain forwarding data.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domains_v1_forwarding_forwarding_resource import DomainsV1ForwardingForwardingResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsForwardingApi(api_client)
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Get forwarding data
        api_response = api_instance.get_forwarding_data_v1(domain)
        print("The response of DomainsForwardingApi->get_forwarding_data_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsForwardingApi->get_forwarding_data_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 

### Return type

[**DomainsV1ForwardingForwardingResource**](DomainsV1ForwardingForwardingResource.md)

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

