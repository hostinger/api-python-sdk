# hostinger_api.DomainsAvailabilityApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_domain_availability_v1**](DomainsAvailabilityApi.md#check_domain_availability_v1) | **POST** /api/domains/v1/availability | Check domain availability


# **check_domain_availability_v1**
> List[DomainsV1AvailabilityAvailabilityResource] check_domain_availability_v1(domains_v1_availability_availability_request)

Check domain availability

This endpoint checks the availability of a domain name. Multiple TLDs can be checked at once.
If you want to get alternative domains with response, provide only one TLD in the request and set `with_alternatives` to `true`.
TLDs should be provided without the leading dot (e.g. `com`, `net`, `org`).

Endpoint has rate limit of 10 requests per minute.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domains_v1_availability_availability_request import DomainsV1AvailabilityAvailabilityRequest
from hostinger_api.models.domains_v1_availability_availability_resource import DomainsV1AvailabilityAvailabilityResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsAvailabilityApi(api_client)
    domains_v1_availability_availability_request = hostinger_api.DomainsV1AvailabilityAvailabilityRequest() # DomainsV1AvailabilityAvailabilityRequest | 

    try:
        # Check domain availability
        api_response = api_instance.check_domain_availability_v1(domains_v1_availability_availability_request)
        print("The response of DomainsAvailabilityApi->check_domain_availability_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsAvailabilityApi->check_domain_availability_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains_v1_availability_availability_request** | [**DomainsV1AvailabilityAvailabilityRequest**](DomainsV1AvailabilityAvailabilityRequest.md)|  | 

### Return type

[**List[DomainsV1AvailabilityAvailabilityResource]**](DomainsV1AvailabilityAvailabilityResource.md)

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

