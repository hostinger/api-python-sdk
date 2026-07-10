# hostinger_api.AgencyHostingDomainsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_agency_plan_website_domain_v1**](AgencyHostingDomainsApi.md#change_agency_plan_website_domain_v1) | **PUT** /api/agency-hosting/v1/websites/{website_uid}/domains/{from_domain} | Change Agency Plan website domain
[**link_domain_to_agency_plan_website_v1**](AgencyHostingDomainsApi.md#link_domain_to_agency_plan_website_v1) | **POST** /api/agency-hosting/v1/websites/{website_uid}/domains | Link domain to Agency Plan website
[**list_agency_plan_domains_v1**](AgencyHostingDomainsApi.md#list_agency_plan_domains_v1) | **GET** /api/agency-hosting/v1/domains | List Agency Plan domains
[**unlink_domain_from_agency_plan_website_v1**](AgencyHostingDomainsApi.md#unlink_domain_from_agency_plan_website_v1) | **DELETE** /api/agency-hosting/v1/websites/{website_uid}/domains/{domain} | Unlink domain from Agency Plan website


# **change_agency_plan_website_domain_v1**
> CommonSuccessEmptyResource change_agency_plan_website_domain_v1(website_uid, from_domain, agency_hosting_v1_domains_change_domain_request)

Change Agency Plan website domain

Changes the primary domain for an Agency Plan website.

Provide the current domain in the path and the new domain in the request body.
Set domain to null to revert to the temporary domain.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_domains_change_domain_request import AgencyHostingV1DomainsChangeDomainRequest
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
    api_instance = hostinger_api.AgencyHostingDomainsApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    from_domain = 'old.example.com' # str | Current domain name to change from
    agency_hosting_v1_domains_change_domain_request = hostinger_api.AgencyHostingV1DomainsChangeDomainRequest() # AgencyHostingV1DomainsChangeDomainRequest | 

    try:
        # Change Agency Plan website domain
        api_response = api_instance.change_agency_plan_website_domain_v1(website_uid, from_domain, agency_hosting_v1_domains_change_domain_request)
        print("The response of AgencyHostingDomainsApi->change_agency_plan_website_domain_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingDomainsApi->change_agency_plan_website_domain_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
 **from_domain** | **str**| Current domain name to change from | 
 **agency_hosting_v1_domains_change_domain_request** | [**AgencyHostingV1DomainsChangeDomainRequest**](AgencyHostingV1DomainsChangeDomainRequest.md)|  | 

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

# **link_domain_to_agency_plan_website_v1**
> CommonSuccessEmptyResource link_domain_to_agency_plan_website_v1(website_uid, agency_hosting_v1_domains_link_domain_request)

Link domain to Agency Plan website

Links a domain to the specified Agency Plan website so it can serve traffic for that domain.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_domains_link_domain_request import AgencyHostingV1DomainsLinkDomainRequest
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
    api_instance = hostinger_api.AgencyHostingDomainsApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    agency_hosting_v1_domains_link_domain_request = hostinger_api.AgencyHostingV1DomainsLinkDomainRequest() # AgencyHostingV1DomainsLinkDomainRequest | 

    try:
        # Link domain to Agency Plan website
        api_response = api_instance.link_domain_to_agency_plan_website_v1(website_uid, agency_hosting_v1_domains_link_domain_request)
        print("The response of AgencyHostingDomainsApi->link_domain_to_agency_plan_website_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingDomainsApi->link_domain_to_agency_plan_website_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
 **agency_hosting_v1_domains_link_domain_request** | [**AgencyHostingV1DomainsLinkDomainRequest**](AgencyHostingV1DomainsLinkDomainRequest.md)|  | 

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

# **list_agency_plan_domains_v1**
> AgencyHostingListAgencyPlanDomainsV1200Response list_agency_plan_domains_v1(page=page, per_page=per_page, website_uuids=website_uuids)

List Agency Plan domains

Returns a paginated list of domains associated with Agency Plan websites accessible to the authenticated client.

Use the website_uuids filter to narrow results to specific websites.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_list_agency_plan_domains_v1200_response import AgencyHostingListAgencyPlanDomainsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingDomainsApi(api_client)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)
    website_uuids = ['[\"zpwlGlp19\"]'] # List[str] | Filter by website UIDs (optional)

    try:
        # List Agency Plan domains
        api_response = api_instance.list_agency_plan_domains_v1(page=page, per_page=per_page, website_uuids=website_uuids)
        print("The response of AgencyHostingDomainsApi->list_agency_plan_domains_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingDomainsApi->list_agency_plan_domains_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]
 **website_uuids** | [**List[str]**](str.md)| Filter by website UIDs | [optional] 

### Return type

[**AgencyHostingListAgencyPlanDomainsV1200Response**](AgencyHostingListAgencyPlanDomainsV1200Response.md)

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

# **unlink_domain_from_agency_plan_website_v1**
> CommonSuccessEmptyResource unlink_domain_from_agency_plan_website_v1(website_uid, domain)

Unlink domain from Agency Plan website

Unlinks a domain from the specified Agency Plan website.

The website stops serving traffic on this domain immediately.

Website files and database are preserved, and any other linked domains remain accessible.

If this is the only domain on the website, unlinking leaves the website without an accessible domain.

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
    api_instance = hostinger_api.AgencyHostingDomainsApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Unlink domain from Agency Plan website
        api_response = api_instance.unlink_domain_from_agency_plan_website_v1(website_uid, domain)
        print("The response of AgencyHostingDomainsApi->unlink_domain_from_agency_plan_website_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingDomainsApi->unlink_domain_from_agency_plan_website_v1: %s\n" % e)
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
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

