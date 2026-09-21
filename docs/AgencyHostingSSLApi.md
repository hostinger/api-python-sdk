# hostinger_api.AgencyHostingSSLApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_website_ssl_status_v1**](AgencyHostingSSLApi.md#get_website_ssl_status_v1) | **GET** /api/agency-hosting/v1/websites/{website_uid}/domains/{domain}/ssl/status | Get website SSL status
[**install_website_sslv1**](AgencyHostingSSLApi.md#install_website_sslv1) | **POST** /api/agency-hosting/v1/websites/{website_uid}/domains/{domain}/ssl/setup | Install website SSL
[**reinstall_website_sslv1**](AgencyHostingSSLApi.md#reinstall_website_sslv1) | **POST** /api/agency-hosting/v1/websites/{website_uid}/domains/{domain}/ssl/reinstall | Reinstall website SSL
[**uninstall_website_sslv1**](AgencyHostingSSLApi.md#uninstall_website_sslv1) | **DELETE** /api/agency-hosting/v1/websites/{website_uid}/domains/{domain}/ssl | Uninstall website SSL


# **get_website_ssl_status_v1**
> AgencyHostingV1SslSslStatusResource get_website_ssl_status_v1(website_uid, domain)

Get website SSL status

Returns the SSL state of one domain of an Agency Plan website: the certificate `status`,
whether the certificate was uploaded by the customer, and when it stops being valid.

`installing` means a certificate setup is running or retrying; the `ssl_setup` entry of
`List website processes` shows the same progress. `active` means a valid certificate is in
place: uploaded by the customer, issued by the platform, or a lifetime certificate bought for
the domain. `failed` means the last setup gave up and no valid certificate is in place.
`expired` means the certificate has run out. `not_installed` means the domain has no
certificate and no setup process. Returns 404 when the website or the domain does not exist.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_ssl_ssl_status_resource import AgencyHostingV1SslSslStatusResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingSSLApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Get website SSL status
        api_response = api_instance.get_website_ssl_status_v1(website_uid, domain)
        print("The response of AgencyHostingSSLApi->get_website_ssl_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingSSLApi->get_website_ssl_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
 **domain** | **str**| Domain name | 

### Return type

[**AgencyHostingV1SslSslStatusResource**](AgencyHostingV1SslSslStatusResource.md)

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

# **install_website_sslv1**
> CommonSuccessEmptyResource install_website_sslv1(website_uid, domain)

Install website SSL

Starts a Let's Encrypt certificate setup for the domain and returns at once; the setup runs in
the background. `Get website SSL status` reports `installing` while it runs, then `active` or
`failed`; the `ssl_setup` entry of `List website processes` shows the same progress.

Returns 422 when the domain already has a platform certificate that is not expired, when a
certificate process is recorded for the domain (a failed setup counts until it is cleaned up),
or when the domain hit its limit of three setups per seven days. Returns 429 when the same
domain was requested less than a minute ago, 403 when the website is suspended or locked, and
404 when the website or the domain does not exist.

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
    api_instance = hostinger_api.AgencyHostingSSLApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Install website SSL
        api_response = api_instance.install_website_sslv1(website_uid, domain)
        print("The response of AgencyHostingSSLApi->install_website_sslv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingSSLApi->install_website_sslv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
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

# **reinstall_website_sslv1**
> CommonSuccessEmptyResource reinstall_website_sslv1(website_uid, domain)

Reinstall website SSL

Replaces the Let's Encrypt certificate of the domain: the current platform certificate, when
one is recorded, is revoked and removed, then a new setup starts in the background. Returns at
once; `Get website SSL status` reports `installing` while it runs, then `active` or `failed`.

Returns 422 for free subdomains, when a certificate process is recorded for the domain (a
failed setup counts until it is cleaned up), or when the domain hit its limit of three setups
per seven days. Returns 429 when the same domain was requested less than a minute ago, and 403
when the website is suspended or locked, and 404 when the website or the domain does not exist.

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
    api_instance = hostinger_api.AgencyHostingSSLApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Reinstall website SSL
        api_response = api_instance.reinstall_website_sslv1(website_uid, domain)
        print("The response of AgencyHostingSSLApi->reinstall_website_sslv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingSSLApi->reinstall_website_sslv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
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

# **uninstall_website_sslv1**
> CommonSuccessEmptyResource uninstall_website_sslv1(website_uid, domain)

Uninstall website SSL

Removes the platform-issued Let's Encrypt certificate of the domain: the certificate is revoked
and deleted before the response, so the domain is no longer served with a platform certificate
until a new setup completes. Also succeeds when the domain has no platform certificate to
remove. Uploaded (custom) certificates are not affected.

Returns 422 when a certificate process is recorded for the domain (a failed setup counts until
it is cleaned up), 429 when the same domain was requested less than a minute ago, and 403 when
the website is suspended or locked, and 404 when the website or the domain does not exist.

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
    api_instance = hostinger_api.AgencyHostingSSLApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Uninstall website SSL
        api_response = api_instance.uninstall_website_sslv1(website_uid, domain)
        print("The response of AgencyHostingSSLApi->uninstall_website_sslv1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingSSLApi->uninstall_website_sslv1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
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

