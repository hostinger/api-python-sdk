# hostinger_api.AgencyHostingWebsitesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_website_node_js_assets_v1**](AgencyHostingWebsitesApi.md#build_website_node_js_assets_v1) | **POST** /api/agency-hosting/v1/websites/{website_uid}/build-assets | Build website NodeJS assets
[**delete_website_v1**](AgencyHostingWebsitesApi.md#delete_website_v1) | **DELETE** /api/agency-hosting/v1/websites/{website_uid} | Delete website
[**get_website_details_v1**](AgencyHostingWebsitesApi.md#get_website_details_v1) | **GET** /api/agency-hosting/v1/websites/{website_uid} | Get website details
[**list_agency_plan_websites_v1**](AgencyHostingWebsitesApi.md#list_agency_plan_websites_v1) | **GET** /api/agency-hosting/v1/websites | List Agency Plan websites
[**list_website_processes_v1**](AgencyHostingWebsitesApi.md#list_website_processes_v1) | **GET** /api/agency-hosting/v1/websites/{website_uid}/processes | List website processes


# **build_website_node_js_assets_v1**
> CommonSuccessEmptyResource build_website_node_js_assets_v1(website_uid, agency_hosting_v1_websites_build_assets_request)

Build website NodeJS assets

Builds and deploys a Node.js application for an Agency Plan website from an already-uploaded archive.

Upload the archive to file browser first, then provide its relative path from document root in this request.
Website contents are overwritten by the build result, which is deployed to public_html.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_websites_build_assets_request import AgencyHostingV1WebsitesBuildAssetsRequest
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
    api_instance = hostinger_api.AgencyHostingWebsitesApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    agency_hosting_v1_websites_build_assets_request = hostinger_api.AgencyHostingV1WebsitesBuildAssetsRequest() # AgencyHostingV1WebsitesBuildAssetsRequest | 

    try:
        # Build website NodeJS assets
        api_response = api_instance.build_website_node_js_assets_v1(website_uid, agency_hosting_v1_websites_build_assets_request)
        print("The response of AgencyHostingWebsitesApi->build_website_node_js_assets_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingWebsitesApi->build_website_node_js_assets_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
 **agency_hosting_v1_websites_build_assets_request** | [**AgencyHostingV1WebsitesBuildAssetsRequest**](AgencyHostingV1WebsitesBuildAssetsRequest.md)|  | 

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

# **delete_website_v1**
> CommonSuccessEmptyResource delete_website_v1(website_uid)

Delete website

Permanently deletes an Agency Plan website. Deletion is processed asynchronously: the
website is immediately transitioned to a deleting state and the underlying server
resources are removed in the background.

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
    api_instance = hostinger_api.AgencyHostingWebsitesApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID

    try:
        # Delete website
        api_response = api_instance.delete_website_v1(website_uid)
        print("The response of AgencyHostingWebsitesApi->delete_website_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingWebsitesApi->delete_website_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 

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

# **get_website_details_v1**
> AgencyHostingV1WebsitesWebsiteResource get_website_details_v1(website_uid)

Get website details

Retrieves detailed information about a specific Agency Plan website, including configuration,
status, metadata, hosting plan details, and resource quotas.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_websites_website_resource import AgencyHostingV1WebsitesWebsiteResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingWebsitesApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID

    try:
        # Get website details
        api_response = api_instance.get_website_details_v1(website_uid)
        print("The response of AgencyHostingWebsitesApi->get_website_details_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingWebsitesApi->get_website_details_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 

### Return type

[**AgencyHostingV1WebsitesWebsiteResource**](AgencyHostingV1WebsitesWebsiteResource.md)

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

# **list_agency_plan_websites_v1**
> AgencyHostingListAgencyPlanWebsitesV1200Response list_agency_plan_websites_v1(page=page, per_page=per_page, order_ids=order_ids, states=states, website_types=website_types, domain=domain)

List Agency Plan websites

Retrieve a paginated list of Agency Plan websites (H5G, Builder, and Horizons) accessible to
the authenticated client.

This endpoint returns websites from your hosting accounts as well as
websites from other client hosting accounts that have shared access
with you.

The response shape differs per platform — see the `platform` field on each item.

Use `website_types` to list only websites of a given detected type, e.g. only
WordPress websites (`website_types=wordpress`) or only Node.js websites
(`website_types=nodejs`). Combine with `order_ids`, `states`, or `domain` for more
targeted results.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_list_agency_plan_websites_v1200_response import AgencyHostingListAgencyPlanWebsitesV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingWebsitesApi(api_client)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)
    order_ids = [[12345,67890]] # List[int] | Filter by order IDs. Accepts a comma-separated list. (optional)
    states = ['[\"active\"]'] # List[str] | Filter by website state. Accepts a comma-separated list. (optional)
    website_types = ['[\"wordpress\",\"nodejs\"]'] # List[str] | Filter by detected website type, e.g. wordpress,nodejs. Accepts a comma-separated list. (optional)
    domain = 'example.com' # str | Filter by domain name (case-insensitive substring match) (optional)

    try:
        # List Agency Plan websites
        api_response = api_instance.list_agency_plan_websites_v1(page=page, per_page=per_page, order_ids=order_ids, states=states, website_types=website_types, domain=domain)
        print("The response of AgencyHostingWebsitesApi->list_agency_plan_websites_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingWebsitesApi->list_agency_plan_websites_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]
 **order_ids** | [**List[int]**](int.md)| Filter by order IDs. Accepts a comma-separated list. | [optional] 
 **states** | [**List[str]**](str.md)| Filter by website state. Accepts a comma-separated list. | [optional] 
 **website_types** | [**List[str]**](str.md)| Filter by detected website type, e.g. wordpress,nodejs. Accepts a comma-separated list. | [optional] 
 **domain** | **str**| Filter by domain name (case-insensitive substring match) | [optional] 

### Return type

[**AgencyHostingListAgencyPlanWebsitesV1200Response**](AgencyHostingListAgencyPlanWebsitesV1200Response.md)

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

# **list_website_processes_v1**
> List[AgencyHostingV1WebsitesWebsiteProcessResource] list_website_processes_v1(website_uid)

List website processes

Lists active and recently completed asynchronous processes for an Agency Plan website.

Each process has a unique ID (for tracking), a type, and a status (running, completed, failed).
Poll this endpoint after initiating async operations (SSL setup, backups, cloning) to track progress.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_websites_website_process_resource import AgencyHostingV1WebsitesWebsiteProcessResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingWebsitesApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID

    try:
        # List website processes
        api_response = api_instance.list_website_processes_v1(website_uid)
        print("The response of AgencyHostingWebsitesApi->list_website_processes_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingWebsitesApi->list_website_processes_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 

### Return type

[**List[AgencyHostingV1WebsitesWebsiteProcessResource]**](AgencyHostingV1WebsitesWebsiteProcessResource.md)

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

