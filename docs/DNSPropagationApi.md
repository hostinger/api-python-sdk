# hostinger_api.DNSPropagationApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_dns_record_propagation_v1**](DNSPropagationApi.md#check_dns_record_propagation_v1) | **GET** /api/dns/v1/propagation/{domain}/{type} | Check DNS record propagation


# **check_dns_record_propagation_v1**
> DNSV1PropagationPropagationReportResource check_dns_record_propagation_v1(domain, type)

Check DNS record propagation

Check whether a DNS record of a domain or host name has propagated to public resolvers around the world.

`authoritative` shows what the domain's authoritative nameservers serve now. It is the best signal
of the current record value. Its TTL tells how long resolvers may keep serving the old value.

`vantage_points` shows what public resolvers at different locations return. `is_propagated` is true
when the location returns the same records as the authoritative nameservers. For GeoDNS domains,
whose nameservers answer differently by region, true means the location returned a record.
A records served from the Hostinger CDN count as propagated. When every responding authoritative
nameserver returns no records, `is_propagated` is true.

Works for any domain or host name, either a domain or a subdomain. Read-only: it changes nothing.

A 404 response with error code 2025 can also mean the check could not be completed, for example
when the DNS checker is busy or timed out. It is safe to retry after a short delay.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.dnsv1_propagation_propagation_report_resource import DNSV1PropagationPropagationReportResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DNSPropagationApi(api_client)
    domain = 'www.mydomain.tld' # str | Domain or host name to check, either a domain or a subdomain
    type = 'A' # str | DNS record type to check. One of: A, AAAA, CNAME, MX, SRV, TXT, CAA

    try:
        # Check DNS record propagation
        api_response = api_instance.check_dns_record_propagation_v1(domain, type)
        print("The response of DNSPropagationApi->check_dns_record_propagation_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSPropagationApi->check_dns_record_propagation_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain or host name to check, either a domain or a subdomain | 
 **type** | **str**| DNS record type to check. One of: A, AAAA, CNAME, MX, SRV, TXT, CAA | 

### Return type

[**DNSV1PropagationPropagationReportResource**](DNSV1PropagationPropagationReportResource.md)

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
**422** | Validation error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

