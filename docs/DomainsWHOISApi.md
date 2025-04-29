# hostinger_api.DomainsWHOISApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_whois_profile_v1**](DomainsWHOISApi.md#create_whois_profile_v1) | **POST** /api/domains/v1/whois | Create WHOIS profile
[**delete_whois_profile_v1**](DomainsWHOISApi.md#delete_whois_profile_v1) | **DELETE** /api/domains/v1/whois/{whoisId} | Delete WHOIS profile
[**get_whois_profile_list_v1**](DomainsWHOISApi.md#get_whois_profile_list_v1) | **GET** /api/domains/v1/whois | Get WHOIS profile list
[**get_whois_profile_usage_v1**](DomainsWHOISApi.md#get_whois_profile_usage_v1) | **GET** /api/domains/v1/whois/{whoisId}/usage | Get WHOIS profile usage
[**get_whois_profile_v1**](DomainsWHOISApi.md#get_whois_profile_v1) | **GET** /api/domains/v1/whois/{whoisId} | Get WHOIS profile


# **create_whois_profile_v1**
> DomainsV1WHOISProfileResource create_whois_profile_v1(domains_v1_whois_store_request)

Create WHOIS profile

This endpoint creates WHOIS contact profile.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domains_v1_whois_profile_resource import DomainsV1WHOISProfileResource
from hostinger_api.models.domains_v1_whois_store_request import DomainsV1WHOISStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsWHOISApi(api_client)
    domains_v1_whois_store_request = hostinger_api.DomainsV1WHOISStoreRequest() # DomainsV1WHOISStoreRequest | 

    try:
        # Create WHOIS profile
        api_response = api_instance.create_whois_profile_v1(domains_v1_whois_store_request)
        print("The response of DomainsWHOISApi->create_whois_profile_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsWHOISApi->create_whois_profile_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains_v1_whois_store_request** | [**DomainsV1WHOISStoreRequest**](DomainsV1WHOISStoreRequest.md)|  | 

### Return type

[**DomainsV1WHOISProfileResource**](DomainsV1WHOISProfileResource.md)

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
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_whois_profile_v1**
> CommonSuccessEmptyResource delete_whois_profile_v1(whois_id)

Delete WHOIS profile

This endpoint deletes WHOIS contact profile.

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
    api_instance = hostinger_api.DomainsWHOISApi(api_client)
    whois_id = 564651 # int | WHOIS ID

    try:
        # Delete WHOIS profile
        api_response = api_instance.delete_whois_profile_v1(whois_id)
        print("The response of DomainsWHOISApi->delete_whois_profile_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsWHOISApi->delete_whois_profile_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whois_id** | **int**| WHOIS ID | 

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
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_whois_profile_list_v1**
> List[DomainsV1WHOISProfileResource] get_whois_profile_list_v1(tld=tld)

Get WHOIS profile list

This endpoint retrieves a list of WHOIS contact profiles.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domains_v1_whois_profile_resource import DomainsV1WHOISProfileResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsWHOISApi(api_client)
    tld = 'com' # str | Filter by TLD (without trailing dot) (optional)

    try:
        # Get WHOIS profile list
        api_response = api_instance.get_whois_profile_list_v1(tld=tld)
        print("The response of DomainsWHOISApi->get_whois_profile_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsWHOISApi->get_whois_profile_list_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tld** | **str**| Filter by TLD (without trailing dot) | [optional] 

### Return type

[**List[DomainsV1WHOISProfileResource]**](DomainsV1WHOISProfileResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_whois_profile_usage_v1**
> List[str] get_whois_profile_usage_v1(whois_id)

Get WHOIS profile usage

This endpoint retrieves a domain list where provided WHOIS contact profile is used.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsWHOISApi(api_client)
    whois_id = 564651 # int | WHOIS ID

    try:
        # Get WHOIS profile usage
        api_response = api_instance.get_whois_profile_usage_v1(whois_id)
        print("The response of DomainsWHOISApi->get_whois_profile_usage_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsWHOISApi->get_whois_profile_usage_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whois_id** | **int**| WHOIS ID | 

### Return type

**List[str]**

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_whois_profile_v1**
> DomainsV1WHOISProfileResource get_whois_profile_v1(whois_id)

Get WHOIS profile

This endpoint retrieves a WHOIS contact profile.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domains_v1_whois_profile_resource import DomainsV1WHOISProfileResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsWHOISApi(api_client)
    whois_id = 564651 # int | WHOIS ID

    try:
        # Get WHOIS profile
        api_response = api_instance.get_whois_profile_v1(whois_id)
        print("The response of DomainsWHOISApi->get_whois_profile_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsWHOISApi->get_whois_profile_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whois_id** | **int**| WHOIS ID | 

### Return type

[**DomainsV1WHOISProfileResource**](DomainsV1WHOISProfileResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

