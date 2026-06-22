# hostinger_api.HostingDomainsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_website_parked_domain_v1**](HostingDomainsApi.md#create_website_parked_domain_v1) | **POST** /api/hosting/v1/accounts/{username}/websites/{domain}/parked-domains | Create website parked domain
[**create_website_subdomain_v1**](HostingDomainsApi.md#create_website_subdomain_v1) | **POST** /api/hosting/v1/accounts/{username}/websites/{domain}/subdomains | Create website subdomain
[**delete_website_parked_domain_v1**](HostingDomainsApi.md#delete_website_parked_domain_v1) | **DELETE** /api/hosting/v1/accounts/{username}/websites/{domain}/parked-domains/{parkedDomain} | Delete website parked domain
[**delete_website_subdomain_v1**](HostingDomainsApi.md#delete_website_subdomain_v1) | **DELETE** /api/hosting/v1/accounts/{username}/websites/{domain}/subdomains/{subdomain} | Delete website subdomain
[**generate_a_free_subdomain_v1**](HostingDomainsApi.md#generate_a_free_subdomain_v1) | **POST** /api/hosting/v1/domains/free-subdomains | Generate a free subdomain
[**list_website_parked_domains_v1**](HostingDomainsApi.md#list_website_parked_domains_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/parked-domains | List website parked domains
[**list_website_subdomains_v1**](HostingDomainsApi.md#list_website_subdomains_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/subdomains | List website subdomains
[**verify_domain_ownership_v1**](HostingDomainsApi.md#verify_domain_ownership_v1) | **POST** /api/hosting/v1/domains/verify-ownership | Verify domain ownership


# **create_website_parked_domain_v1**
> CommonSuccessEmptyResource create_website_parked_domain_v1(username, domain, hosting_v1_domains_create_parked_domain_request)

Create website parked domain

Create a parked or alias domain for the selected website.

Provide a domain name or IP address to park on the website so it serves the same content
as the parent domain.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.hosting_v1_domains_create_parked_domain_request import HostingV1DomainsCreateParkedDomainRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingDomainsApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    hosting_v1_domains_create_parked_domain_request = hostinger_api.HostingV1DomainsCreateParkedDomainRequest() # HostingV1DomainsCreateParkedDomainRequest | 

    try:
        # Create website parked domain
        api_response = api_instance.create_website_parked_domain_v1(username, domain, hosting_v1_domains_create_parked_domain_request)
        print("The response of HostingDomainsApi->create_website_parked_domain_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDomainsApi->create_website_parked_domain_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **hosting_v1_domains_create_parked_domain_request** | [**HostingV1DomainsCreateParkedDomainRequest**](HostingV1DomainsCreateParkedDomainRequest.md)|  | 

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

# **create_website_subdomain_v1**
> CommonSuccessEmptyResource create_website_subdomain_v1(username, domain, hosting_v1_domains_create_subdomain_request)

Create website subdomain

Create a new subdomain for the selected website.

Provide a subdomain prefix and, optionally, a custom directory or the
website public directory to use as the subdomain root.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.hosting_v1_domains_create_subdomain_request import HostingV1DomainsCreateSubdomainRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingDomainsApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    hosting_v1_domains_create_subdomain_request = hostinger_api.HostingV1DomainsCreateSubdomainRequest() # HostingV1DomainsCreateSubdomainRequest | 

    try:
        # Create website subdomain
        api_response = api_instance.create_website_subdomain_v1(username, domain, hosting_v1_domains_create_subdomain_request)
        print("The response of HostingDomainsApi->create_website_subdomain_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDomainsApi->create_website_subdomain_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **hosting_v1_domains_create_subdomain_request** | [**HostingV1DomainsCreateSubdomainRequest**](HostingV1DomainsCreateSubdomainRequest.md)|  | 

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

# **delete_website_parked_domain_v1**
> CommonSuccessEmptyResource delete_website_parked_domain_v1(username, domain, parked_domain)

Delete website parked domain

Delete an existing parked or alias domain from the selected website.

Use this endpoint to remove parked domains that are no longer needed.

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
    api_instance = hostinger_api.HostingDomainsApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    parked_domain = 'parked-domain.com' # str | 

    try:
        # Delete website parked domain
        api_response = api_instance.delete_website_parked_domain_v1(username, domain, parked_domain)
        print("The response of HostingDomainsApi->delete_website_parked_domain_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDomainsApi->delete_website_parked_domain_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **parked_domain** | **str**|  | 

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

# **delete_website_subdomain_v1**
> CommonSuccessEmptyResource delete_website_subdomain_v1(username, domain, subdomain)

Delete website subdomain

Delete an existing subdomain from the selected website.

Use this endpoint to remove subdomains that are no longer needed.

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
    api_instance = hostinger_api.HostingDomainsApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    subdomain = 'blog' # str | 

    try:
        # Delete website subdomain
        api_response = api_instance.delete_website_subdomain_v1(username, domain, subdomain)
        print("The response of HostingDomainsApi->delete_website_subdomain_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDomainsApi->delete_website_subdomain_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **subdomain** | **str**|  | 

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

# **generate_a_free_subdomain_v1**
> HostingV1DomainsFreeSubdomainResource generate_a_free_subdomain_v1()

Generate a free subdomain

Generate a unique free subdomain that can be used for hosting services without purchasing custom domains.
Free subdomains allow you to start using hosting services immediately
and you can always connect a custom domain to your site later.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_domains_free_subdomain_resource import HostingV1DomainsFreeSubdomainResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingDomainsApi(api_client)

    try:
        # Generate a free subdomain
        api_response = api_instance.generate_a_free_subdomain_v1()
        print("The response of HostingDomainsApi->generate_a_free_subdomain_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDomainsApi->generate_a_free_subdomain_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HostingV1DomainsFreeSubdomainResource**](HostingV1DomainsFreeSubdomainResource.md)

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

# **list_website_parked_domains_v1**
> List[HostingV1DomainsParkedDomainResource] list_website_parked_domains_v1(username, domain)

List website parked domains

Retrieve all parked or alias domains created under the selected website.

Use this endpoint to inspect parked domain configuration for a specific website,
including the parent domain and root directory assigned to each parked domain.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_domains_parked_domain_resource import HostingV1DomainsParkedDomainResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingDomainsApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name

    try:
        # List website parked domains
        api_response = api_instance.list_website_parked_domains_v1(username, domain)
        print("The response of HostingDomainsApi->list_website_parked_domains_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDomainsApi->list_website_parked_domains_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 

### Return type

[**List[HostingV1DomainsParkedDomainResource]**](HostingV1DomainsParkedDomainResource.md)

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

# **list_website_subdomains_v1**
> List[HostingV1DomainsSubdomainResource] list_website_subdomains_v1(username, domain)

List website subdomains

Retrieve all subdomains created under the selected website.

Use this endpoint to inspect subdomain configuration for a specific website,
including the parent domain and root directory assigned to each subdomain.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_domains_subdomain_resource import HostingV1DomainsSubdomainResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingDomainsApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name

    try:
        # List website subdomains
        api_response = api_instance.list_website_subdomains_v1(username, domain)
        print("The response of HostingDomainsApi->list_website_subdomains_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDomainsApi->list_website_subdomains_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 

### Return type

[**List[HostingV1DomainsSubdomainResource]**](HostingV1DomainsSubdomainResource.md)

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

# **verify_domain_ownership_v1**
> HostingV1DomainsDomainAccessResource verify_domain_ownership_v1(hosting_v1_domains_verify_ownership_request)

Verify domain ownership

Verify ownership of a single domain and return the verification status.

Use this endpoint to check if a domain is accessible for you before using it for new websites.
If the domain is accessible, the response will have `is_accessible: true`.
If not, add the given TXT record to your domain's DNS records and try verifying again.
Keep in mind that it may take up to 10 minutes for new TXT DNS records to propagate.

Skip this verification when using Hostinger's free subdomains (*.hostingersite.com).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_domains_domain_access_resource import HostingV1DomainsDomainAccessResource
from hostinger_api.models.hosting_v1_domains_verify_ownership_request import HostingV1DomainsVerifyOwnershipRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingDomainsApi(api_client)
    hosting_v1_domains_verify_ownership_request = hostinger_api.HostingV1DomainsVerifyOwnershipRequest() # HostingV1DomainsVerifyOwnershipRequest | 

    try:
        # Verify domain ownership
        api_response = api_instance.verify_domain_ownership_v1(hosting_v1_domains_verify_ownership_request)
        print("The response of HostingDomainsApi->verify_domain_ownership_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDomainsApi->verify_domain_ownership_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hosting_v1_domains_verify_ownership_request** | [**HostingV1DomainsVerifyOwnershipRequest**](HostingV1DomainsVerifyOwnershipRequest.md)|  | 

### Return type

[**HostingV1DomainsDomainAccessResource**](HostingV1DomainsDomainAccessResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Unauthenticated response |  -  |
**422** | Validation error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

