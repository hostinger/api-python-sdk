# hostinger_api.DomainsTransferApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**claim_free_domain_transfer_v1**](DomainsTransferApi.md#claim_free_domain_transfer_v1) | **POST** /api/domains/v1/transfers/claim | Claim free domain transfer
[**get_transfer_list_v1**](DomainsTransferApi.md#get_transfer_list_v1) | **GET** /api/domains/v1/transfers | Get transfer list
[**get_transfer_v1**](DomainsTransferApi.md#get_transfer_v1) | **GET** /api/domains/v1/transfers/{domain} | Get transfer


# **claim_free_domain_transfer_v1**
> DomainsV1TransferTransferResource claim_free_domain_transfer_v1(domains_v1_transfer_claim_request)

Claim free domain transfer

Claim a free domain transfer available on your account and start the transfer.

Unlike purchasing a transfer, this consumes a free domain transfer you already have,
so no payment method is required.

Before making request, unlock the domain at the current registrar and get its authorization
code. The transfer is validated first, so domains which cannot be transferred are rejected
before the free domain transfer is consumed.

A successful response means the transfer has been started. Completion depends on the current
registrar and can be followed with the [transfer list endpoint](#tag/domains-transfer).

If no WHOIS information is provided, default contact information for that TLD will be used.
Before making request, ensure WHOIS information for desired TLD exists in your account.

Requests which cannot be fulfilled are rejected with an error code in the response body.

Use this endpoint to transfer a domain using a free domain transfer from your account.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domains_v1_transfer_claim_request import DomainsV1TransferClaimRequest
from hostinger_api.models.domains_v1_transfer_transfer_resource import DomainsV1TransferTransferResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsTransferApi(api_client)
    domains_v1_transfer_claim_request = hostinger_api.DomainsV1TransferClaimRequest() # DomainsV1TransferClaimRequest | 

    try:
        # Claim free domain transfer
        api_response = api_instance.claim_free_domain_transfer_v1(domains_v1_transfer_claim_request)
        print("The response of DomainsTransferApi->claim_free_domain_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsTransferApi->claim_free_domain_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains_v1_transfer_claim_request** | [**DomainsV1TransferClaimRequest**](DomainsV1TransferClaimRequest.md)|  | 

### Return type

[**DomainsV1TransferTransferResource**](DomainsV1TransferTransferResource.md)

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

# **get_transfer_list_v1**
> List[DomainsV1TransferTransferResource] get_transfer_list_v1()

Get transfer list

Retrieve all domain transfers in your portfolio.

Use this endpoint to monitor incoming and outgoing registrar transfers across your domains.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domains_v1_transfer_transfer_resource import DomainsV1TransferTransferResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsTransferApi(api_client)

    try:
        # Get transfer list
        api_response = api_instance.get_transfer_list_v1()
        print("The response of DomainsTransferApi->get_transfer_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsTransferApi->get_transfer_list_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DomainsV1TransferTransferResource]**](DomainsV1TransferTransferResource.md)

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

# **get_transfer_v1**
> DomainsV1TransferTransferResource get_transfer_v1(domain)

Get transfer

Retrieve the transfer for a specified domain.

Use this endpoint to track an incoming or outgoing registrar transfer and its status.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domains_v1_transfer_transfer_resource import DomainsV1TransferTransferResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsTransferApi(api_client)
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Get transfer
        api_response = api_instance.get_transfer_v1(domain)
        print("The response of DomainsTransferApi->get_transfer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsTransferApi->get_transfer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 

### Return type

[**DomainsV1TransferTransferResource**](DomainsV1TransferTransferResource.md)

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

