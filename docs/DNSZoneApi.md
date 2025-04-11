# @hostinger/api.DNSZoneApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_records_v1**](DNSZoneApi.md#get_records_v1) | **GET** /api/dns/v1/zones/{domain} | Get records
[**reset_zone_records_v1**](DNSZoneApi.md#reset_zone_records_v1) | **POST** /api/dns/v1/zones/{domain}/reset | Reset zone records


# **get_records_v1**
> List[DNSV1ZoneNameResource] get_records_v1(domain)

Get records

This endpoint retrieves DNS zone records for a specific domain.

### Example

* Bearer Authentication (apiToken):

```python
import @hostinger/api
from @hostinger/api.models.dnsv1_zone_name_resource import DNSV1ZoneNameResource
from @hostinger/api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = @hostinger/api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with @hostinger/api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = @hostinger/api.DNSZoneApi(api_client)
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

[**List[DNSV1ZoneNameResource]**](DNSV1ZoneNameResource.md)

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
import @hostinger/api
from @hostinger/api.models.common_success_empty_resource import CommonSuccessEmptyResource
from @hostinger/api.models.dnsv1_zone_reset_request import DNSV1ZoneResetRequest
from @hostinger/api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = @hostinger/api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with @hostinger/api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = @hostinger/api.DNSZoneApi(api_client)
    domain = 'mydomain.tld' # str | Domain name
    dnsv1_zone_reset_request = @hostinger/api.DNSV1ZoneResetRequest() # DNSV1ZoneResetRequest | 

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

