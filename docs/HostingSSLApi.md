# hostinger_api.HostingSSLApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ssl_status_v1**](HostingSSLApi.md#get_ssl_status_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/ssl/status | Get SSL status
[**install_sslv1**](HostingSSLApi.md#install_sslv1) | **POST** /api/hosting/v1/accounts/{username}/websites/{domain}/ssl/setup | Install SSL
[**toggle_https_redirect_v1**](HostingSSLApi.md#toggle_https_redirect_v1) | **PATCH** /api/hosting/v1/accounts/{username}/websites/{domain}/ssl/https-redirect/toggle | Toggle HTTPS redirect
[**uninstall_sslv1**](HostingSSLApi.md#uninstall_sslv1) | **DELETE** /api/hosting/v1/accounts/{username}/websites/{domain}/ssl | Uninstall SSL


# **get_ssl_status_v1**
> HostingV1SslSslStatusResource get_ssl_status_v1(username, domain)

Get SSL status

Returns the SSL state of the website: the certificate `status` and `provider`, whether the
certificate is a lifetime one managed by the platform, whether HTTP requests are redirected to
HTTPS, when the certificate stops being valid and the last installation error.

`installing` and `waiting_for_retry` mean an installation is in progress. `failed` means the
last installation gave up, or the website was not updated for 60 minutes while `installing`;
`last_error` holds the reason when it is a known message, otherwise it is null. `expired`
means the assigned certificate's validity has ended. `not_installed` means no certificate is
assigned. Free subdomains use a platform-managed certificate: with no installation recorded
they report `active` with `provider` and `expires_at` null.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_ssl_ssl_status_resource import HostingV1SslSslStatusResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingSSLApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Get SSL status
        api_response = api_instance.get_ssl_status_v1(username, domain)
        print("The response of HostingSSLApi->get_ssl_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingSSLApi->get_ssl_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 

### Return type

[**HostingV1SslSslStatusResource**](HostingV1SslSslStatusResource.md)

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

# **install_sslv1**
> CommonSuccessEmptyResource install_sslv1(username, domain)

Install SSL

Requests a lifetime SSL certificate for the website. The installation runs in the background;
`Get SSL status` reports `active` or `failed` when it ends. An `active` lifetime certificate
does not block the request: a new installation is requested, which is how a certificate is
reinstalled.

Returns 422 for free subdomains (their certificate is managed by the platform), while an
installation is `installing` or `waiting_for_retry`, when the website's certificate was
revoked (it cannot be reissued), and when an uploaded custom certificate is installed; that
one has to be uninstalled first.

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
    api_instance = hostinger_api.HostingSSLApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Install SSL
        api_response = api_instance.install_sslv1(username, domain)
        print("The response of HostingSSLApi->install_sslv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingSSLApi->install_sslv1: %s\n" % e)
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

# **toggle_https_redirect_v1**
> CommonSuccessEmptyResource toggle_https_redirect_v1(username, domain, hosting_v1_ssl_toggle_https_redirect_request)

Toggle HTTPS redirect

Turns the HTTP to HTTPS redirect of the website on or off, based on `is_enabled`. Does
nothing when the redirect is already in the requested state. Turning it on requires an
installed certificate (`status` `active` or `expired` on `Get SSL status`) and returns 422
when there is none; turning it off is always accepted.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.hosting_v1_ssl_toggle_https_redirect_request import HostingV1SslToggleHttpsRedirectRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingSSLApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    hosting_v1_ssl_toggle_https_redirect_request = hostinger_api.HostingV1SslToggleHttpsRedirectRequest() # HostingV1SslToggleHttpsRedirectRequest | 

    try:
        # Toggle HTTPS redirect
        api_response = api_instance.toggle_https_redirect_v1(username, domain, hosting_v1_ssl_toggle_https_redirect_request)
        print("The response of HostingSSLApi->toggle_https_redirect_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingSSLApi->toggle_https_redirect_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **hosting_v1_ssl_toggle_https_redirect_request** | [**HostingV1SslToggleHttpsRedirectRequest**](HostingV1SslToggleHttpsRedirectRequest.md)|  | 

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
**200** | Success empty response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uninstall_sslv1**
> CommonSuccessEmptyResource uninstall_sslv1(username, domain)

Uninstall SSL

Removes the SSL certificate assigned to the website, turns the HTTPS redirect off and cancels
a pending installation retry. The website serves plain HTTP until a new installation
completes. `Get SSL status` reports `not_installed` as soon as the call returns; the call also
succeeds when no certificate is assigned, so repeating it is safe.

Returns 422 for free subdomains (their certificate is managed by the platform) and while an
installation is `installing`.

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
    api_instance = hostinger_api.HostingSSLApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Uninstall SSL
        api_response = api_instance.uninstall_sslv1(username, domain)
        print("The response of HostingSSLApi->uninstall_sslv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingSSLApi->uninstall_sslv1: %s\n" % e)
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

