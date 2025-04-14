# hostinger-api.DomainsPortfolioApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_domain_list_v1**](DomainsPortfolioApi.md#get_domain_list_v1) | **GET** /api/domains/v1/portfolio | Get domain list


# **get_domain_list_v1**
> List[DomainsV1DomainDomainResource] get_domain_list_v1()

Get domain list

This endpoint retrieves a list of all domains associated with your account.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger-api
from hostinger-api.models.domains_v1_domain_domain_resource import DomainsV1DomainDomainResource
from hostinger-api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger-api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger-api.DomainsPortfolioApi(api_client)

    try:
        # Get domain list
        api_response = api_instance.get_domain_list_v1()
        print("The response of DomainsPortfolioApi->get_domain_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsPortfolioApi->get_domain_list_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DomainsV1DomainDomainResource]**](DomainsV1DomainDomainResource.md)

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

