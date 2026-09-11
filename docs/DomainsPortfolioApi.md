# hostinger_api.DomainsPortfolioApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**claim_free_domain_v1**](DomainsPortfolioApi.md#claim_free_domain_v1) | **POST** /api/domains/v1/portfolio/claim | Claim free domain
[**complete_domain_setup_v1**](DomainsPortfolioApi.md#complete_domain_setup_v1) | **POST** /api/domains/v1/portfolio/{domain}/setup | Complete domain setup
[**disable_domain_lock_v1**](DomainsPortfolioApi.md#disable_domain_lock_v1) | **DELETE** /api/domains/v1/portfolio/{domain}/domain-lock | Disable domain lock
[**disable_privacy_protection_v1**](DomainsPortfolioApi.md#disable_privacy_protection_v1) | **DELETE** /api/domains/v1/portfolio/{domain}/privacy-protection | Disable privacy protection
[**enable_domain_lock_v1**](DomainsPortfolioApi.md#enable_domain_lock_v1) | **PUT** /api/domains/v1/portfolio/{domain}/domain-lock | Enable domain lock
[**enable_privacy_protection_v1**](DomainsPortfolioApi.md#enable_privacy_protection_v1) | **PUT** /api/domains/v1/portfolio/{domain}/privacy-protection | Enable privacy protection
[**get_domain_authorization_code_v1**](DomainsPortfolioApi.md#get_domain_authorization_code_v1) | **GET** /api/domains/v1/portfolio/{domain}/auth-code | Get domain authorization code
[**get_domain_details_v1**](DomainsPortfolioApi.md#get_domain_details_v1) | **GET** /api/domains/v1/portfolio/{domain} | Get domain details
[**get_domain_list_v1**](DomainsPortfolioApi.md#get_domain_list_v1) | **GET** /api/domains/v1/portfolio | Get domain list
[**get_domain_renewal_information_v1**](DomainsPortfolioApi.md#get_domain_renewal_information_v1) | **GET** /api/domains/v1/portfolio/{domain}/renewal | Get domain renewal information
[**purchase_new_domain_v1**](DomainsPortfolioApi.md#purchase_new_domain_v1) | **POST** /api/domains/v1/portfolio | Purchase new domain
[**update_domain_nameservers_v1**](DomainsPortfolioApi.md#update_domain_nameservers_v1) | **PUT** /api/domains/v1/portfolio/{domain}/nameservers | Update domain nameservers


# **claim_free_domain_v1**
> DomainsV1PortfolioClaimResource claim_free_domain_v1(domains_v1_portfolio_claim_request)

Claim free domain

Claim a free domain available on your account and register it.

Unlike purchasing a domain, this consumes a free domain you already have,
so no payment method is required.

A successful response means the domain is registered. If registration fails, login to
[hPanel](https://hpanel.hostinger.com/) and check domain registration status.

If no WHOIS information is provided, default contact information for that TLD will be used.
Before making request, ensure WHOIS information for desired TLD exists in your account.

Some TLDs require `additional_details` to be provided and these will be validated before claiming.

Requests which cannot be fulfilled are rejected with an error code in the response body,
for example `2037` when no free domain is available.

Use this endpoint to register a domain using a free domain from your account.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domains_v1_portfolio_claim_request import DomainsV1PortfolioClaimRequest
from hostinger_api.models.domains_v1_portfolio_claim_resource import DomainsV1PortfolioClaimResource
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
    domains_v1_portfolio_claim_request = hostinger_api.DomainsV1PortfolioClaimRequest() # DomainsV1PortfolioClaimRequest | 

    try:
        # Claim free domain
        api_response = api_instance.claim_free_domain_v1(domains_v1_portfolio_claim_request)
        print("The response of DomainsPortfolioApi->claim_free_domain_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsPortfolioApi->claim_free_domain_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains_v1_portfolio_claim_request** | [**DomainsV1PortfolioClaimRequest**](DomainsV1PortfolioClaimRequest.md)|  | 

### Return type

[**DomainsV1PortfolioClaimResource**](DomainsV1PortfolioClaimResource.md)

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

# **complete_domain_setup_v1**
> CommonSuccessEmptyResource complete_domain_setup_v1(domain, domains_v1_portfolio_setup_request)

Complete domain setup

Register a domain you have already paid for but which has not been set up yet.

Use this endpoint when an order completed without registering the domain, for example when
`Purchase new domain` returned `202 Accepted` and the domain was added to your account without
being registered, or when an earlier setup attempt failed. No new order is placed and no payment
is taken: the subscription you already own is used, for the period you already paid for.

A domain is left awaiting setup when the details needed to register it were missing or invalid
as the order completed. Domains ordered elsewhere can be awaiting setup for the same reason.
Complete the missing information, then call this endpoint. If the order itself has not completed
yet, the domain is not on your account, wait until it appears in `Get domain list`.

If `domain_contacts` is omitted, the default WHOIS profile of that TLD is used for all four
roles. The profile must exist and be complete for the TLD, an incomplete profile is the most
common reason a domain is left awaiting setup. Create one with `Create WHOIS profile`.

Some TLDs require `additional_details`. These are validated before setup, so a missing or
invalid value is rejected without any registration being attempted.

The domain is set up with the default nameservers and without privacy protection. Use
`Update domain nameservers` and `Enable privacy protection` afterwards to change either.

A successful response means the setup request was accepted, not that the domain is already
registered. Poll `Get domain list` for the outcome, the domain appears in `Get domain details`
only once it is registered.

Use this endpoint to finish registering a domain that is awaiting setup on your account.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.domains_v1_portfolio_setup_request import DomainsV1PortfolioSetupRequest
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
    domains_v1_portfolio_setup_request = hostinger_api.DomainsV1PortfolioSetupRequest() # DomainsV1PortfolioSetupRequest | 

    try:
        # Complete domain setup
        api_response = api_instance.complete_domain_setup_v1(domain, domains_v1_portfolio_setup_request)
        print("The response of DomainsPortfolioApi->complete_domain_setup_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsPortfolioApi->complete_domain_setup_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 
 **domains_v1_portfolio_setup_request** | [**DomainsV1PortfolioSetupRequest**](DomainsV1PortfolioSetupRequest.md)|  | 

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
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_domain_lock_v1**
> CommonSuccessEmptyResource disable_domain_lock_v1(domain)

Disable domain lock

Disable domain lock for the domain.

Domain lock needs to be disabled before transferring the domain to another registrar.

Use this endpoint to prepare domains for transfer to other registrars.

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

Disable privacy protection for the domain.

When privacy protection is disabled, domain owner's personal information is visible in public WHOIS database.

Use this endpoint to make domain owner's information publicly visible.

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

Enable domain lock for the domain.

When domain lock is enabled,
the domain cannot be transferred to another registrar without first disabling the lock.

Use this endpoint to secure domains against unauthorized transfers.

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

Enable privacy protection for the domain.

When privacy protection is enabled, domain owner's personal information is hidden from public WHOIS database.

Use this endpoint to protect domain owner's personal information from public view.

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

# **get_domain_authorization_code_v1**
> DomainsV1PortfolioAuthCodeAuthCodeResource get_domain_authorization_code_v1(domain)

Get domain authorization code

Retrieve the authorization (EPP) code for a specified domain so it can be transferred
away from Hostinger to another registrar.

Requesting a new code invalidates any code retrieved previously.

Use this endpoint to obtain the code required to transfer a domain to another registrar.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domains_v1_portfolio_auth_code_auth_code_resource import DomainsV1PortfolioAuthCodeAuthCodeResource
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
        # Get domain authorization code
        api_response = api_instance.get_domain_authorization_code_v1(domain)
        print("The response of DomainsPortfolioApi->get_domain_authorization_code_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsPortfolioApi->get_domain_authorization_code_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 

### Return type

[**DomainsV1PortfolioAuthCodeAuthCodeResource**](DomainsV1PortfolioAuthCodeAuthCodeResource.md)

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

# **get_domain_details_v1**
> DomainsV1DomainDomainExtendedResource get_domain_details_v1(domain)

Get domain details

Retrieve detailed information for specified domain.

Use this endpoint to view comprehensive domain configuration and status.

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
        # Get domain details
        api_response = api_instance.get_domain_details_v1(domain)
        print("The response of DomainsPortfolioApi->get_domain_details_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsPortfolioApi->get_domain_details_v1: %s\n" % e)
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

# **get_domain_list_v1**
> List[DomainsV1DomainDomainResource] get_domain_list_v1()

Get domain list

Retrieve all domains associated with your account.

Use this endpoint to view user's domain portfolio.

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

# **get_domain_renewal_information_v1**
> DomainsV1PortfolioRenewalRenewalInformationResource get_domain_renewal_information_v1(domain)

Get domain renewal information

Retrieve renewal information for a specified domain, including its status and current
expiration date.

Use this endpoint to build renewal automation and expiry monitoring for a single domain.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domains_v1_portfolio_renewal_renewal_information_resource import DomainsV1PortfolioRenewalRenewalInformationResource
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
        # Get domain renewal information
        api_response = api_instance.get_domain_renewal_information_v1(domain)
        print("The response of DomainsPortfolioApi->get_domain_renewal_information_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsPortfolioApi->get_domain_renewal_information_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 

### Return type

[**DomainsV1PortfolioRenewalRenewalInformationResource**](DomainsV1PortfolioRenewalRenewalInformationResource.md)

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

Purchase and register a new domain name.

If registration fails, login to [hPanel](https://hpanel.hostinger.com/) and check domain registration status.

If no payment method is provided, your default payment method will be used automatically.

If the response is `202 Accepted`, the payment is still being processed and the domain was
**not** registered. Once the order completes, register the domain from
[hPanel](https://hpanel.hostinger.com/).

If no WHOIS information is provided, default contact information for that TLD will be used.
Before making request, ensure WHOIS information for desired TLD exists in your account.

Some TLDs require `additional_details` to be provided and these will be validated before completing purchase.

Use this endpoint to register new domains for users.

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
**202** | Payment is being processed, the order will complete asynchronously |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain_nameservers_v1**
> CommonSuccessEmptyResource update_domain_nameservers_v1(domain, domains_v1_portfolio_update_nameservers_request)

Update domain nameservers

Set nameservers for a specified domain.

Be aware, that improper nameserver configuration can lead to the domain being unresolvable or unavailable.

Use this endpoint to configure custom DNS hosting for domains.

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
        # Update domain nameservers
        api_response = api_instance.update_domain_nameservers_v1(domain, domains_v1_portfolio_update_nameservers_request)
        print("The response of DomainsPortfolioApi->update_domain_nameservers_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsPortfolioApi->update_domain_nameservers_v1: %s\n" % e)
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

