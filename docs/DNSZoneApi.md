# hostinger_api.DNSZoneApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_zone_records_v1**](DNSZoneApi.md#delete_zone_records_v1) | **DELETE** /api/dns/v1/zones/{domain} | Delete zone records
[**get_records_v1**](DNSZoneApi.md#get_records_v1) | **GET** /api/dns/v1/zones/{domain} | Get records
[**reset_zone_records_v1**](DNSZoneApi.md#reset_zone_records_v1) | **POST** /api/dns/v1/zones/{domain}/reset | Reset zone records
[**update_zone_records_v1**](DNSZoneApi.md#update_zone_records_v1) | **PUT** /api/dns/v1/zones/{domain} | Update zone records
[**validate_zone_records_v1**](DNSZoneApi.md#validate_zone_records_v1) | **POST** /api/dns/v1/zones/{domain}/validate | Validate zone records


# **delete_zone_records_v1**
> CommonSuccessEmptyResource delete_zone_records_v1(domain, dnsv1_zone_destroy_request)

Delete zone records

This endpoint deletes selected DNS records for the selected domain.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.dnsv1_zone_destroy_request import DNSV1ZoneDestroyRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DNSZoneApi(api_client)
    domain = 'mydomain.tld' # str | Domain name
    dnsv1_zone_destroy_request = hostinger_api.DNSV1ZoneDestroyRequest() # DNSV1ZoneDestroyRequest | 

    try:
        # Delete zone records
        api_response = api_instance.delete_zone_records_v1(domain, dnsv1_zone_destroy_request)
        print("The response of DNSZoneApi->delete_zone_records_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSZoneApi->delete_zone_records_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 
 **dnsv1_zone_destroy_request** | [**DNSV1ZoneDestroyRequest**](DNSV1ZoneDestroyRequest.md)|  | 

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
**422** | Validation error response |  -  |
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_records_v1**
> List[DNSV1ZoneRecordResource] get_records_v1(domain)

Get records

This endpoint retrieves DNS zone records for a specific domain.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.dnsv1_zone_record_resource import DNSV1ZoneRecordResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DNSZoneApi(api_client)
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Get records
        api_response = api_instance.get_records_v1(domain)
        print("The response of DNSZoneApi->get_records_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSZoneApi->get_records_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 

### Return type

[**List[DNSV1ZoneRecordResource]**](DNSV1ZoneRecordResource.md)

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

# **reset_zone_records_v1**
> CommonSuccessEmptyResource reset_zone_records_v1(domain, dnsv1_zone_reset_request)

Reset zone records

This endpoint resets DNS zone to the default records.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.dnsv1_zone_reset_request import DNSV1ZoneResetRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DNSZoneApi(api_client)
    domain = 'mydomain.tld' # str | Domain name
    dnsv1_zone_reset_request = hostinger_api.DNSV1ZoneResetRequest() # DNSV1ZoneResetRequest | 

    try:
        # Reset zone records
        api_response = api_instance.reset_zone_records_v1(domain, dnsv1_zone_reset_request)
        print("The response of DNSZoneApi->reset_zone_records_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSZoneApi->reset_zone_records_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 
 **dnsv1_zone_reset_request** | [**DNSV1ZoneResetRequest**](DNSV1ZoneResetRequest.md)|  | 

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
**422** | Validation error response |  -  |
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_zone_records_v1**
> CommonSuccessEmptyResource update_zone_records_v1(domain, dnsv1_zone_update_request)

Update zone records

This endpoint updates DNS records for the selected domain. This endpoint could also be used
to delete single record when multiple records exist under same name. In that case use `overwrite` flag
and provide records which should remain. All other records under same name will be deleted.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.dnsv1_zone_update_request import DNSV1ZoneUpdateRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DNSZoneApi(api_client)
    domain = 'mydomain.tld' # str | Domain name
    dnsv1_zone_update_request = hostinger_api.DNSV1ZoneUpdateRequest() # DNSV1ZoneUpdateRequest | 

    try:
        # Update zone records
        api_response = api_instance.update_zone_records_v1(domain, dnsv1_zone_update_request)
        print("The response of DNSZoneApi->update_zone_records_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSZoneApi->update_zone_records_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 
 **dnsv1_zone_update_request** | [**DNSV1ZoneUpdateRequest**](DNSV1ZoneUpdateRequest.md)|  | 

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
**422** | Validation error response |  -  |
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_zone_records_v1**
> CommonSuccessEmptyResource validate_zone_records_v1(domain, dnsv1_zone_update_request)

Validate zone records

This endpoint used to validate DNS records prior update for the selected domain. 

If the validation is successful, the response will contain `200 Success` code.
If there is validation error, the response will fail with `422 Validation error` code.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.dnsv1_zone_update_request import DNSV1ZoneUpdateRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DNSZoneApi(api_client)
    domain = 'mydomain.tld' # str | Domain name
    dnsv1_zone_update_request = hostinger_api.DNSV1ZoneUpdateRequest() # DNSV1ZoneUpdateRequest | 

    try:
        # Validate zone records
        api_response = api_instance.validate_zone_records_v1(domain, dnsv1_zone_update_request)
        print("The response of DNSZoneApi->validate_zone_records_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSZoneApi->validate_zone_records_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 
 **dnsv1_zone_update_request** | [**DNSV1ZoneUpdateRequest**](DNSV1ZoneUpdateRequest.md)|  | 

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
**422** | Validation error response |  -  |
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

