# hostinger_api.DomainsPortfolioApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_domain_lock_v1**](DomainsPortfolioApi.md#disable_domain_lock_v1) | **DELETE** /api/domains/v1/portfolio/{domain}/domain-lock | Disable domain lock
[**disable_privacy_protection_v1**](DomainsPortfolioApi.md#disable_privacy_protection_v1) | **DELETE** /api/domains/v1/portfolio/{domain}/privacy-protection | Disable privacy protection
[**enable_domain_lock_v1**](DomainsPortfolioApi.md#enable_domain_lock_v1) | **PUT** /api/domains/v1/portfolio/{domain}/domain-lock | Enable domain lock
[**enable_privacy_protection_v1**](DomainsPortfolioApi.md#enable_privacy_protection_v1) | **PUT** /api/domains/v1/portfolio/{domain}/privacy-protection | Enable privacy protection
[**get_domain_list_v1**](DomainsPortfolioApi.md#get_domain_list_v1) | **GET** /api/domains/v1/portfolio | Get domain list
[**get_domain_v1**](DomainsPortfolioApi.md#get_domain_v1) | **GET** /api/domains/v1/portfolio/{domain} | Get domain
[**purchase_new_domain_v1**](DomainsPortfolioApi.md#purchase_new_domain_v1) | **POST** /api/domains/v1/portfolio | Purchase new domain
[**update_nameservers_v1**](DomainsPortfolioApi.md#update_nameservers_v1) | **PUT** /api/domains/v1/portfolio/{domain}/nameservers | Update nameservers


# **disable_domain_lock_v1**
> CommonSuccessEmptyResource disable_domain_lock_v1(domain)

Disable domain lock

This endpoint disables domain lock for the domain. Domain lock needs to be disabled 
before transferring the domain to another registrar.

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
    api_instance = hostinger_api.DomainsPortfolioApi(api_client)
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Disable domain lock
        api_response = api_instance.disable_domain_lock_v1(domain)
        print("The response of DomainsPortfolioApi->disable_domain_lock_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsPortfolioApi->disable_domain_lock_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_privacy_protection_v1**
> CommonSuccessEmptyResource disable_privacy_protection_v1(domain)

Disable privacy protection

This endpoint disables privacy protection for the domain.
When privacy protection is disabled, the domain owner's personal information is visible in the public WHOIS database.

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
    api_instance = hostinger_api.DomainsPortfolioApi(api_client)
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Disable privacy protection
        api_response = api_instance.disable_privacy_protection_v1(domain)
        print("The response of DomainsPortfolioApi->disable_privacy_protection_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsPortfolioApi->disable_privacy_protection_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_domain_lock_v1**
> CommonSuccessEmptyResource enable_domain_lock_v1(domain)

Enable domain lock

This endpoint enables domain lock for the domain. When domain lock is enabled, 
the domain cannot be transferred to another registrar without first disabling the lock.

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
    api_instance = hostinger_api.DomainsPortfolioApi(api_client)
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Enable domain lock
        api_response = api_instance.enable_domain_lock_v1(domain)
        print("The response of DomainsPortfolioApi->enable_domain_lock_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsPortfolioApi->enable_domain_lock_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_privacy_protection_v1**
> CommonSuccessEmptyResource enable_privacy_protection_v1(domain)

Enable privacy protection

This endpoint enables privacy protection for the domain.
When privacy protection is enabled, the domain owner's personal information is hidden from the public WHOIS database.

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
    api_instance = hostinger_api.DomainsPortfolioApi(api_client)
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Enable privacy protection
        api_response = api_instance.enable_privacy_protection_v1(domain)
        print("The response of DomainsPortfolioApi->enable_privacy_protection_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsPortfolioApi->enable_privacy_protection_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_list_v1**
> List[DomainsV1DomainDomainResource] get_domain_list_v1()

Get domain list

This endpoint retrieves a list of all domains associated with your account.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domains_v1_domain_domain_resource import DomainsV1DomainDomainResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsPortfolioApi(api_client)

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
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_v1**
> DomainsV1DomainDomainExtendedResource get_domain_v1(domain)

Get domain

This endpoint retrieves details for specified domain.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domains_v1_domain_domain_extended_resource import DomainsV1DomainDomainExtendedResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsPortfolioApi(api_client)
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Get domain
        api_response = api_instance.get_domain_v1(domain)
        print("The response of DomainsPortfolioApi->get_domain_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsPortfolioApi->get_domain_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 

### Return type

[**DomainsV1DomainDomainExtendedResource**](DomainsV1DomainDomainExtendedResource.md)

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

# **purchase_new_domain_v1**
> BillingV1OrderOrderResource purchase_new_domain_v1(domains_v1_portfolio_purchase_request)

Purchase new domain

This endpoint allows you to buy (purchase) and register a new domain name. 

If registration fails, login to [hPanel](https://hpanel.hostinger.com/) and check the domain registration status.

If no payment method is provided, your default payment method will be used automatically.

If no WHOIS information is provided, the default contact information for that TLD (Top-Level Domain) will be used. 
Before making a request, ensure that WHOIS information for the desired TLD exists in your account.

Some TLDs require `additional_details` to be provided and these will be validated before completing the purchase. The required additional details vary by TLD.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.billing_v1_order_order_resource import BillingV1OrderOrderResource
from hostinger_api.models.domains_v1_portfolio_purchase_request import DomainsV1PortfolioPurchaseRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsPortfolioApi(api_client)
    domains_v1_portfolio_purchase_request = hostinger_api.DomainsV1PortfolioPurchaseRequest() # DomainsV1PortfolioPurchaseRequest | 

    try:
        # Purchase new domain
        api_response = api_instance.purchase_new_domain_v1(domains_v1_portfolio_purchase_request)
        print("The response of DomainsPortfolioApi->purchase_new_domain_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsPortfolioApi->purchase_new_domain_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains_v1_portfolio_purchase_request** | [**DomainsV1PortfolioPurchaseRequest**](DomainsV1PortfolioPurchaseRequest.md)|  | 

### Return type

[**BillingV1OrderOrderResource**](BillingV1OrderOrderResource.md)

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

# **update_nameservers_v1**
> CommonSuccessEmptyResource update_nameservers_v1(domain, domains_v1_portfolio_update_nameservers_request)

Update nameservers

This endpoint sets the nameservers for a specified domain.

Be aware, that improper nameserver configuration can lead to the domain being unresolvable or unavailable. 

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.domains_v1_portfolio_update_nameservers_request import DomainsV1PortfolioUpdateNameserversRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsPortfolioApi(api_client)
    domain = 'mydomain.tld' # str | Domain name
    domains_v1_portfolio_update_nameservers_request = hostinger_api.DomainsV1PortfolioUpdateNameserversRequest() # DomainsV1PortfolioUpdateNameserversRequest | 

    try:
        # Update nameservers
        api_response = api_instance.update_nameservers_v1(domain, domains_v1_portfolio_update_nameservers_request)
        print("The response of DomainsPortfolioApi->update_nameservers_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsPortfolioApi->update_nameservers_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 
 **domains_v1_portfolio_update_nameservers_request** | [**DomainsV1PortfolioUpdateNameserversRequest**](DomainsV1PortfolioUpdateNameserversRequest.md)|  | 

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

