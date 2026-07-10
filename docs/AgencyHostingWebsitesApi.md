# hostinger_api.AgencyHostingWebsitesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_agency_plan_website_node_js_assets_v1**](AgencyHostingWebsitesApi.md#build_agency_plan_website_node_js_assets_v1) | **POST** /api/agency-hosting/v1/websites/{website_uid}/build-assets | Build Agency Plan website NodeJS assets
[**delete_agency_plan_website_v1**](AgencyHostingWebsitesApi.md#delete_agency_plan_website_v1) | **DELETE** /api/agency-hosting/v1/websites/{website_uid} | Delete Agency Plan website
[**get_agency_plan_website_details_v1**](AgencyHostingWebsitesApi.md#get_agency_plan_website_details_v1) | **GET** /api/agency-hosting/v1/websites/{website_uid} | Get Agency Plan website details
[**list_running_agency_plan_website_processes_v1**](AgencyHostingWebsitesApi.md#list_running_agency_plan_website_processes_v1) | **GET** /api/agency-hosting/v1/websites/{website_uid}/processes | List running Agency Plan website processes


# **build_agency_plan_website_node_js_assets_v1**
> CommonSuccessEmptyResource build_agency_plan_website_node_js_assets_v1(website_uid, agency_hosting_v1_websites_build_assets_request)

Build Agency Plan website NodeJS assets

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
        # Build Agency Plan website NodeJS assets
        api_response = api_instance.build_agency_plan_website_node_js_assets_v1(website_uid, agency_hosting_v1_websites_build_assets_request)
        print("The response of AgencyHostingWebsitesApi->build_agency_plan_website_node_js_assets_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingWebsitesApi->build_agency_plan_website_node_js_assets_v1: %s\n" % e)
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

# **delete_agency_plan_website_v1**
> AgencyHostingV1WebsitesWebsiteDeletionResource delete_agency_plan_website_v1(website_uid)

Delete Agency Plan website

Deletes an Agency Plan website and schedules cleanup of its resources.

This action is irreversible. Website files, databases, and linked domains are removed.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_websites_website_deletion_resource import AgencyHostingV1WebsitesWebsiteDeletionResource
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
        # Delete Agency Plan website
        api_response = api_instance.delete_agency_plan_website_v1(website_uid)
        print("The response of AgencyHostingWebsitesApi->delete_agency_plan_website_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingWebsitesApi->delete_agency_plan_website_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 

### Return type

[**AgencyHostingV1WebsitesWebsiteDeletionResource**](AgencyHostingV1WebsitesWebsiteDeletionResource.md)

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

# **get_agency_plan_website_details_v1**
> AgencyHostingV1WebsitesWebsiteResource get_agency_plan_website_details_v1(website_uid)

Get Agency Plan website details

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
        # Get Agency Plan website details
        api_response = api_instance.get_agency_plan_website_details_v1(website_uid)
        print("The response of AgencyHostingWebsitesApi->get_agency_plan_website_details_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingWebsitesApi->get_agency_plan_website_details_v1: %s\n" % e)
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

# **list_running_agency_plan_website_processes_v1**
> List[AgencyHostingV1WebsitesWebsiteProcessResource] list_running_agency_plan_website_processes_v1(website_uid)

List running Agency Plan website processes

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
        # List running Agency Plan website processes
        api_response = api_instance.list_running_agency_plan_website_processes_v1(website_uid)
        print("The response of AgencyHostingWebsitesApi->list_running_agency_plan_website_processes_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingWebsitesApi->list_running_agency_plan_website_processes_v1: %s\n" % e)
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

