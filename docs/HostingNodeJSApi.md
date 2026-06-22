# hostinger_api.HostingNodeJSApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_node_js_build_from_archive_v1**](HostingNodeJSApi.md#create_node_js_build_from_archive_v1) | **POST** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds/from-archive | Create NodeJS build from archive
[**get_node_js_build_logs_v1**](HostingNodeJSApi.md#get_node_js_build_logs_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds/{uuid}/logs | Get NodeJS build logs
[**list_node_js_builds_v1**](HostingNodeJSApi.md#list_node_js_builds_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds | List NodeJS builds


# **create_node_js_build_from_archive_v1**
> HostingV1NodeJsBuildResource create_node_js_build_from_archive_v1(username, domain, hosting_v1_node_js_create_from_archive_request)

Create NodeJS build from archive

Upload a project archive, auto-detect build settings, and immediately start a Node.js build.

This is the recommended single-step approach for deploying a Node.js application.
The archive is uploaded to the website's file storage, build settings are auto-detected
from the package.json inside the archive, and the build process starts automatically.
Optional override fields take precedence over auto-detected values.
Maximum archive size is 50MB.

Before archiving, exclude `node_modules/` and any build output directories
(e.g. `dist/`, `.next/`, `build/`) — they are not needed because the build
process runs the install step automatically, and including them unnecessarily
increases the archive size. This also helps keep the archive well under the 50MB limit.

Example (zip):
```
zip -r archive.zip . --exclude "node_modules/*" --exclude "dist/*"
```

The returned build `uuid` can be used to poll progress and retrieve logs via
the `Get Node.js Build Logs` endpoint.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_node_js_build_resource import HostingV1NodeJsBuildResource
from hostinger_api.models.hosting_v1_node_js_create_from_archive_request import HostingV1NodeJsCreateFromArchiveRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingNodeJSApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    hosting_v1_node_js_create_from_archive_request = hostinger_api.HostingV1NodeJsCreateFromArchiveRequest() # HostingV1NodeJsCreateFromArchiveRequest | 

    try:
        # Create NodeJS build from archive
        api_response = api_instance.create_node_js_build_from_archive_v1(username, domain, hosting_v1_node_js_create_from_archive_request)
        print("The response of HostingNodeJSApi->create_node_js_build_from_archive_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingNodeJSApi->create_node_js_build_from_archive_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **hosting_v1_node_js_create_from_archive_request** | [**HostingV1NodeJsCreateFromArchiveRequest**](HostingV1NodeJsCreateFromArchiveRequest.md)|  | 

### Return type

[**HostingV1NodeJsBuildResource**](HostingV1NodeJsBuildResource.md)

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

# **get_node_js_build_logs_v1**
> HostingV1NodeJsBuildLogsResource get_node_js_build_logs_v1(username, domain, uuid, from_line=from_line)

Get NodeJS build logs

Retrieve logs from a specific Node.js build process.

To stream live output while a build is running, poll this endpoint repeatedly
while the build state is `running`, passing the previously returned `lines` count
as `from_line` to fetch only new output since the last call.
Log content may contain ANSI escape sequences (color codes).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_node_js_build_logs_resource import HostingV1NodeJsBuildLogsResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingNodeJSApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    uuid = '123e4567-e89b-12d3-a456-426614174000' # str | Build UUID
    from_line = 0 # int | Line from which to start retrieving logs (optional) (default to 0)

    try:
        # Get NodeJS build logs
        api_response = api_instance.get_node_js_build_logs_v1(username, domain, uuid, from_line=from_line)
        print("The response of HostingNodeJSApi->get_node_js_build_logs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingNodeJSApi->get_node_js_build_logs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **uuid** | **str**| Build UUID | 
 **from_line** | **int**| Line from which to start retrieving logs | [optional] [default to 0]

### Return type

[**HostingV1NodeJsBuildLogsResource**](HostingV1NodeJsBuildLogsResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_node_js_builds_v1**
> HostingListNodeJSBuildsV1200Response list_node_js_builds_v1(username, domain, page=page, per_page=per_page, states=states)

List NodeJS builds

Retrieve a paginated list of Node.js build processes for a specific website.

Each build represents a single run of the Node.js build pipeline. Use the `states`
query parameter to filter results by build state (pending, running, completed, failed).
Use the `uuid` from a build to poll its output via the `Get Node.js Build Logs` endpoint.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_list_node_js_builds_v1200_response import HostingListNodeJSBuildsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingNodeJSApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)
    states = ['states_example'] # List[str] | Build states to filter by (optional)

    try:
        # List NodeJS builds
        api_response = api_instance.list_node_js_builds_v1(username, domain, page=page, per_page=per_page, states=states)
        print("The response of HostingNodeJSApi->list_node_js_builds_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingNodeJSApi->list_node_js_builds_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]
 **states** | [**List[str]**](str.md)| Build states to filter by | [optional] 

### Return type

[**HostingListNodeJSBuildsV1200Response**](HostingListNodeJSBuildsV1200Response.md)

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

