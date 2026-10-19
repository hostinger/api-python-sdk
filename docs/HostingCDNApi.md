# hostinger_api.HostingCDNApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_cdnv1**](HostingCDNApi.md#disable_cdnv1) | **POST** /api/hosting/v1/accounts/{username}/websites/{domain}/cdn/disable | Disable CDN
[**enable_cdnv1**](HostingCDNApi.md#enable_cdnv1) | **POST** /api/hosting/v1/accounts/{username}/websites/{domain}/cdn/enable | Enable CDN
[**get_cdn_status_v1**](HostingCDNApi.md#get_cdn_status_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/cdn/status | Get CDN status
[**purge_cdn_cache_v1**](HostingCDNApi.md#purge_cdn_cache_v1) | **DELETE** /api/hosting/v1/accounts/{username}/websites/{domain}/cdn/purge | Purge CDN cache


# **disable_cdnv1**
> CommonSuccessEmptyResource disable_cdnv1(username, domain)

Disable CDN

Turns off the Hostinger CDN for the website domain. Once DNS propagation completes, the
website content is served directly from the origin server. Repeating the call is safe; when
CDN is already disabled, it applies the DNS change again.

Returns 422 for platform-managed domains (for example `*.hostingersite.com` and
`*.app-preview.com`), where CDN cannot be disabled, even when CDN is already off. Also returns
422 while the account is being moved to another server (retry after the move finishes), or
when the CDN provider rejects the change. Returns 404 when the domain is not a website on the
account.

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
    api_instance = hostinger_api.HostingCDNApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Disable CDN
        api_response = api_instance.disable_cdnv1(username, domain)
        print("The response of HostingCDNApi->disable_cdnv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingCDNApi->disable_cdnv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
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
**200** | Success empty response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_cdnv1**
> CommonSuccessEmptyResource enable_cdnv1(username, domain)

Enable CDN

Turns on the Hostinger CDN for the website domain, which speeds up page loads and reduces the
load on the server. Works for the main domain, parked domains and subdomains of the account.

Enabling changes the domain's DNS records and usually takes a few seconds. After that, DNS
propagation can take a few more minutes before visitors are served through the CDN.

Repeating the call is safe, for example after a timeout. When CDN is already enabled, it
applies the DNS change again and refreshes the CDN SSL certificate.

Returns 422 when the account is disabled, while the account is being moved to another
server (retry after the move finishes), or when the CDN provider rejects the change.
Returns 404 when the domain is not a website on the account.

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
    api_instance = hostinger_api.HostingCDNApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Enable CDN
        api_response = api_instance.enable_cdnv1(username, domain)
        print("The response of HostingCDNApi->enable_cdnv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingCDNApi->enable_cdnv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
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
**200** | Success empty response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cdn_status_v1**
> HostingV1CdnCdnStatusResource get_cdn_status_v1(username, domain)

Get CDN status

Returns whether the Hostinger CDN is enabled for the website domain. Works for the main
domain, parked domains and subdomains of the account.

The domain must be the exact website name as listed on the account, without a `www.` prefix.
Returns 404 when the domain is not a website on the account.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_cdn_cdn_status_resource import HostingV1CdnCdnStatusResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingCDNApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Get CDN status
        api_response = api_instance.get_cdn_status_v1(username, domain)
        print("The response of HostingCDNApi->get_cdn_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingCDNApi->get_cdn_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 

### Return type

[**HostingV1CdnCdnStatusResource**](HostingV1CdnCdnStatusResource.md)

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

# **purge_cdn_cache_v1**
> CommonSuccessEmptyResource purge_cdn_cache_v1(username, domain)

Purge CDN cache

Purges the website's content from the Hostinger CDN edge cache only. The origin server cache
is not touched; to clear both, use `Clear website cache`.

Returns 422 when CDN is not enabled on the website. Returns 404 when the domain is not a
website on the account.

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
    api_instance = hostinger_api.HostingCDNApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Purge CDN cache
        api_response = api_instance.purge_cdn_cache_v1(username, domain)
        print("The response of HostingCDNApi->purge_cdn_cache_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingCDNApi->purge_cdn_cache_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
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
**200** | Success empty response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

