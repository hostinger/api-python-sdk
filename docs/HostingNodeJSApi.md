# hostinger_api.HostingNodeJSApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyse_failed_node_js_build_v1**](HostingNodeJSApi.md#analyse_failed_node_js_build_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds/{uuid}/analysis | Analyse failed Node.js build
[**clear_node_js_runtime_logs_v1**](HostingNodeJSApi.md#clear_node_js_runtime_logs_v1) | **DELETE** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/runtime-logs | Clear Node.js runtime logs
[**get_node_js_build_details_v1**](HostingNodeJSApi.md#get_node_js_build_details_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds/{uuid} | Get Node.js build details
[**get_node_js_build_logs_v1**](HostingNodeJSApi.md#get_node_js_build_logs_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds/{uuid}/logs | Get NodeJS build logs
[**get_node_js_build_settings_from_archive_v1**](HostingNodeJSApi.md#get_node_js_build_settings_from_archive_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds/settings/from-archive | Get Node.js build settings from archive
[**get_node_js_build_settings_v1**](HostingNodeJSApi.md#get_node_js_build_settings_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds/settings | Get Node.js build settings
[**get_node_js_runtime_logs_v1**](HostingNodeJSApi.md#get_node_js_runtime_logs_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/runtime-logs | Get Node.js runtime logs
[**list_node_js_builds_v1**](HostingNodeJSApi.md#list_node_js_builds_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds | List NodeJS builds
[**list_node_js_environment_variables_v1**](HostingNodeJSApi.md#list_node_js_environment_variables_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds/settings/env | List Node.js environment variables
[**list_node_js_vulnerabilities_v1**](HostingNodeJSApi.md#list_node_js_vulnerabilities_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/vulnerabilities | List Node.js vulnerabilities
[**patch_node_js_vulnerabilities_v1**](HostingNodeJSApi.md#patch_node_js_vulnerabilities_v1) | **POST** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/vulnerabilities/patch | Patch Node.js vulnerabilities
[**replace_node_js_environment_variables_v1**](HostingNodeJSApi.md#replace_node_js_environment_variables_v1) | **PUT** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds/settings/env | Replace Node.js environment variables
[**restart_node_js_application_v1**](HostingNodeJSApi.md#restart_node_js_application_v1) | **POST** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/server/restart | Restart Node.js application
[**start_node_js_build_v1**](HostingNodeJSApi.md#start_node_js_build_v1) | **POST** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds | Start Node.js build
[**update_node_js_build_settings_v1**](HostingNodeJSApi.md#update_node_js_build_settings_v1) | **PUT** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds/settings | Update Node.js build settings


# **analyse_failed_node_js_build_v1**
> HostingV1NodeJsBuildAnalysisResource analyse_failed_node_js_build_v1(username, domain, uuid)

Analyse failed Node.js build

Returns an AI analysis of why a build failed and how to fix it, based on the build logs,
the project file list and package.json. Only builds in the `failed` state can be analysed;
any other state returns 422. When no analysis could be produced both `analysis` and
`solution` are null, in which case read `Get NodeJS build logs` instead.

Each call runs the analysis again, so call it once per failed build and keep the result.
Limited to 5 calls per minute per API client (429 above that).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_node_js_build_analysis_resource import HostingV1NodeJsBuildAnalysisResource
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

    try:
        # Analyse failed Node.js build
        api_response = api_instance.analyse_failed_node_js_build_v1(username, domain, uuid)
        print("The response of HostingNodeJSApi->analyse_failed_node_js_build_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingNodeJSApi->analyse_failed_node_js_build_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **uuid** | **str**| Build UUID | 

### Return type

[**HostingV1NodeJsBuildAnalysisResource**](HostingV1NodeJsBuildAnalysisResource.md)

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

# **clear_node_js_runtime_logs_v1**
> CommonSuccessEmptyResource clear_node_js_runtime_logs_v1(username, domain)

Clear Node.js runtime logs

Empties the Node.js application's runtime log file. This cannot be undone, so confirm with
the user before calling it. Returns success even when no log file exists yet.

Use it before reproducing a problem so the next `Get Node.js runtime logs` call returns
only fresh entries; start that call with `period` again instead of reusing a `from_line`
from before the clear.

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
    api_instance = hostinger_api.HostingNodeJSApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Clear Node.js runtime logs
        api_response = api_instance.clear_node_js_runtime_logs_v1(username, domain)
        print("The response of HostingNodeJSApi->clear_node_js_runtime_logs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingNodeJSApi->clear_node_js_runtime_logs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
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

# **get_node_js_build_details_v1**
> HostingV1NodeJsBuildResource get_node_js_build_details_v1(username, domain, uuid)

Get Node.js build details

Returns one build by UUID: its state (`pending`, `running`, `completed`, `failed`), the
options it ran with and timestamps. Poll this while a build is pending or running. When it
is failed, read `Get NodeJS build logs` and `Analyse failed Node.js build` for the cause.
Returns 404 when the UUID does not belong to a build of this website.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_node_js_build_resource import HostingV1NodeJsBuildResource
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

    try:
        # Get Node.js build details
        api_response = api_instance.get_node_js_build_details_v1(username, domain, uuid)
        print("The response of HostingNodeJSApi->get_node_js_build_details_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingNodeJSApi->get_node_js_build_details_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **uuid** | **str**| Build UUID | 

### Return type

[**HostingV1NodeJsBuildResource**](HostingV1NodeJsBuildResource.md)

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

# **get_node_js_build_settings_from_archive_v1**
> HostingV1NodeJsBuildSettingsResource get_node_js_build_settings_from_archive_v1(username, domain, archive_path)

Get Node.js build settings from archive

Auto-detect Node.js build settings from a package.json inside an archive already on the server.

Use this before calling `Start Node.js Build` to preview what settings will be used,
or to let the user review and override values (framework, node version, root directory,
output directory, build script) before committing to a build.

The archive must already be present on the website's file storage. Use the
`Generate Upload URL` endpoint to obtain credentials and upload the archive first.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_node_js_build_settings_resource import HostingV1NodeJsBuildSettingsResource
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
    archive_path = 'example.zip' # str | The path to the archive file relative to the document root of the vhost

    try:
        # Get Node.js build settings from archive
        api_response = api_instance.get_node_js_build_settings_from_archive_v1(username, domain, archive_path)
        print("The response of HostingNodeJSApi->get_node_js_build_settings_from_archive_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingNodeJSApi->get_node_js_build_settings_from_archive_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **archive_path** | **str**| The path to the archive file relative to the document root of the vhost | 

### Return type

[**HostingV1NodeJsBuildSettingsResource**](HostingV1NodeJsBuildSettingsResource.md)

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

# **get_node_js_build_settings_v1**
> HostingV1NodeJsStoredBuildSettingsResource get_node_js_build_settings_v1(username, domain)

Get Node.js build settings

Returns the build settings stored for the website: framework (`app_type`), Node.js version,
root and output directory, build script, entry file and package manager. Stored settings
drive Git auto-deployment builds. A build started through the API uses the values sent in
that request and saves them here only when no settings exist yet.

Returns 404 until the first build or the first settings update stores them. Use this after
a failed build to check whether the framework or the entry file were detected wrong, then
fix them with the `Update Node.js build settings` endpoint.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_node_js_stored_build_settings_resource import HostingV1NodeJsStoredBuildSettingsResource
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

    try:
        # Get Node.js build settings
        api_response = api_instance.get_node_js_build_settings_v1(username, domain)
        print("The response of HostingNodeJSApi->get_node_js_build_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingNodeJSApi->get_node_js_build_settings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 

### Return type

[**HostingV1NodeJsStoredBuildSettingsResource**](HostingV1NodeJsStoredBuildSettingsResource.md)

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

# **get_node_js_runtime_logs_v1**
> HostingV1NodeJsRuntimeLogsResource get_node_js_runtime_logs_v1(username, domain, period=period, from_line=from_line, limit=limit, levels=levels)

Get Node.js runtime logs

Returns the Node.js application's runtime console log entries, oldest first, each with
timestamp, level and message. On the first call send `period` (`1h`, `1d`, `1w` or `1m`)
and optionally `levels` and `limit` (1-5000, default 1000); when more entries match than
`limit`, the newest are kept.

To poll for new entries send `total_lines + 1` from the previous response as `from_line`
and omit `period`; `period` and `from_line` cannot be combined. Lines that are not JSON
with a timestamp, level and message are skipped, so `logs` may hold fewer than `limit`
entries while `total_lines` counts every raw line. Entries with a timestamp before
`last_deployed_at` belong to the previous deployment. Returns an empty `logs` list when
the application has not written a log file yet.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_node_js_runtime_logs_resource import HostingV1NodeJsRuntimeLogsResource
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
    period = '1h' # str | Time window for the first fetch. Required when `from_line` is not sent. (optional)
    from_line = 5042 # int | 1-based line of the log file to start from. For polling send `total_lines + 1` from the previous response. Cannot be combined with `period`. (optional)
    limit = 1000 # int | Maximum number of log entries to return. When more entries match, the newest are kept. (optional) (default to 1000)
    levels = ['[\"ERROR\",\"WARN\"]'] # List[str] | Return only entries with these log levels, sent as a comma-separated list, e.g. ERROR,WARN. Matching runs on the raw log line, so entries written with numeric levels (for example by pino) are excluded while this filter is set. (optional)

    try:
        # Get Node.js runtime logs
        api_response = api_instance.get_node_js_runtime_logs_v1(username, domain, period=period, from_line=from_line, limit=limit, levels=levels)
        print("The response of HostingNodeJSApi->get_node_js_runtime_logs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingNodeJSApi->get_node_js_runtime_logs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **period** | **str**| Time window for the first fetch. Required when &#x60;from_line&#x60; is not sent. | [optional] 
 **from_line** | **int**| 1-based line of the log file to start from. For polling send &#x60;total_lines + 1&#x60; from the previous response. Cannot be combined with &#x60;period&#x60;. | [optional] 
 **limit** | **int**| Maximum number of log entries to return. When more entries match, the newest are kept. | [optional] [default to 1000]
 **levels** | [**List[str]**](str.md)| Return only entries with these log levels, sent as a comma-separated list, e.g. ERROR,WARN. Matching runs on the raw log line, so entries written with numeric levels (for example by pino) are excluded while this filter is set. | [optional] 

### Return type

[**HostingV1NodeJsRuntimeLogsResource**](HostingV1NodeJsRuntimeLogsResource.md)

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

# **list_node_js_environment_variables_v1**
> List[HostingV1NodeJsEnvVarResource] list_node_js_environment_variables_v1(username, domain)

List Node.js environment variables

Lists the Node.js environment variables currently set for the website. Values are always
masked as `********` and cannot be read back through this API. Use this endpoint to see
which keys are configured or to verify a change, not to read values.

To change variables, use the `Replace Node.js environment variables` endpoint. It replaces
the whole set, so never copy the masked values from this response into that request; send
the full desired set with real values taken from the project `.env` file or the user
prompt instead.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_node_js_env_var_resource import HostingV1NodeJsEnvVarResource
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

    try:
        # List Node.js environment variables
        api_response = api_instance.list_node_js_environment_variables_v1(username, domain)
        print("The response of HostingNodeJSApi->list_node_js_environment_variables_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingNodeJSApi->list_node_js_environment_variables_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 

### Return type

[**List[HostingV1NodeJsEnvVarResource]**](HostingV1NodeJsEnvVarResource.md)

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

# **list_node_js_vulnerabilities_v1**
> List[HostingV1NodeJsVulnerabilityResource] list_node_js_vulnerabilities_v1(username, domain, severities=severities)

List Node.js vulnerabilities

Lists known npm package vulnerabilities detected on a Node.js website, enriched with
advisory metadata (severity, CVSS score, CVE, advisory URL). Results are sorted from
the most severe to the least severe, then by publish date (newest first). Use the
`severities` query parameter to filter.

Vulnerabilities with `is_patchable` set to `true` can be auto-fixed via the
`Patch Node.js Vulnerabilities` endpoint, which opens a GitHub pull request with
updated package versions. Auto-fix is only available for websites deployed from a
connected GitHub repository. Vulnerabilities with `is_patching_in_progress` set to
`true` are already included in an open patch pull request; while any patch pull
request is open, new patch requests for this website are rejected until it is merged
or closed.

Data comes from periodic dependency scans, so it may lag behind the latest deployment.
An empty list means the most recent scan found no vulnerabilities; it does not
guarantee the current deployment is vulnerability-free. Available on Business and
Cloud Hosting plans.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_node_js_vulnerability_resource import HostingV1NodeJsVulnerabilityResource
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
    severities = ['severities_example'] # List[str] | Severities to filter by (optional)

    try:
        # List Node.js vulnerabilities
        api_response = api_instance.list_node_js_vulnerabilities_v1(username, domain, severities=severities)
        print("The response of HostingNodeJSApi->list_node_js_vulnerabilities_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingNodeJSApi->list_node_js_vulnerabilities_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **severities** | [**List[str]**](str.md)| Severities to filter by | [optional] 

### Return type

[**List[HostingV1NodeJsVulnerabilityResource]**](HostingV1NodeJsVulnerabilityResource.md)

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

# **patch_node_js_vulnerabilities_v1**
> HostingV1NodeJsPatchResultResource patch_node_js_vulnerabilities_v1(username, domain, hosting_v1_node_js_patch_vulnerabilities_request)

Patch Node.js vulnerabilities

Patches the selected Node.js vulnerabilities by updating the affected package versions
in `package.json` and opening a GitHub pull request in the connected repository. The
customer reviews and merges the pull request; merging triggers the automatic deployment.

Auto-fix is only available for websites deployed from a connected GitHub repository.
Websites deployed from an archive have no auto-fix path and return a 404. The Hostinger
GitHub App needs write access to the repository; without it the request fails with a
403 explaining the missing permission.

Only vulnerabilities with `is_patchable` set to `true` can be patched. Non-patchable
IDs in the selection are skipped; the pull request covers the patchable subset, listed
in `patched_vulnerability_ids`. Selections without any patchable vulnerability are
rejected with a 422. Only one patch pull request can be open at a time per website;
close or merge it before patching again. Available on Business and Cloud Hosting plans.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_node_js_patch_result_resource import HostingV1NodeJsPatchResultResource
from hostinger_api.models.hosting_v1_node_js_patch_vulnerabilities_request import HostingV1NodeJsPatchVulnerabilitiesRequest
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
    hosting_v1_node_js_patch_vulnerabilities_request = hostinger_api.HostingV1NodeJsPatchVulnerabilitiesRequest() # HostingV1NodeJsPatchVulnerabilitiesRequest | 

    try:
        # Patch Node.js vulnerabilities
        api_response = api_instance.patch_node_js_vulnerabilities_v1(username, domain, hosting_v1_node_js_patch_vulnerabilities_request)
        print("The response of HostingNodeJSApi->patch_node_js_vulnerabilities_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingNodeJSApi->patch_node_js_vulnerabilities_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **hosting_v1_node_js_patch_vulnerabilities_request** | [**HostingV1NodeJsPatchVulnerabilitiesRequest**](HostingV1NodeJsPatchVulnerabilitiesRequest.md)|  | 

### Return type

[**HostingV1NodeJsPatchResultResource**](HostingV1NodeJsPatchResultResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_node_js_environment_variables_v1**
> CommonSuccessEmptyResource replace_node_js_environment_variables_v1(username, domain, hosting_v1_node_js_set_build_env_vars_request)

Replace Node.js environment variables

Replaces the website's Node.js environment variables with the ones provided. This is a
full replace: any variable not in the request is deleted, and sending an empty `env_vars`
array deletes every variable. Saving writes the values and restarts the running Node.js
process.

A restart is enough for apps that read environment variables at process start, such as
Express or NestJS. It is not enough for frameworks that bake variables into the build.
Next.js standalone is one of those: build-time values (including `NEXT_PUBLIC_*`) need a
fresh build. After this call, use the `Start Node.js build` endpoint so those apps
pick up the new values.

The `List Node.js environment variables` endpoint returns masked values (`********`), so
never copy values from it into this request. Always send the full desired set with real
values taken from the project `.env` file or the user prompt.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.hosting_v1_node_js_set_build_env_vars_request import HostingV1NodeJsSetBuildEnvVarsRequest
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
    hosting_v1_node_js_set_build_env_vars_request = hostinger_api.HostingV1NodeJsSetBuildEnvVarsRequest() # HostingV1NodeJsSetBuildEnvVarsRequest | 

    try:
        # Replace Node.js environment variables
        api_response = api_instance.replace_node_js_environment_variables_v1(username, domain, hosting_v1_node_js_set_build_env_vars_request)
        print("The response of HostingNodeJSApi->replace_node_js_environment_variables_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingNodeJSApi->replace_node_js_environment_variables_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **hosting_v1_node_js_set_build_env_vars_request** | [**HostingV1NodeJsSetBuildEnvVarsRequest**](HostingV1NodeJsSetBuildEnvVarsRequest.md)|  | 

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

# **restart_node_js_application_v1**
> CommonSuccessEmptyResource restart_node_js_application_v1(username, domain)

Restart Node.js application

Restarts the Node.js server process for the website. Does not rebuild or redeploy the
application. Use it to apply environment or configuration changes, or to recover a hung
application.

Only applicable to server-side applications (Express, Next.js, NestJS, etc.). Static
front-end apps (React, Vue, Vite) have no persistent server process, so restarting them
has no effect. Returns success even when the website has no server process to restart.

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
    api_instance = hostinger_api.HostingNodeJSApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Restart Node.js application
        api_response = api_instance.restart_node_js_application_v1(username, domain)
        print("The response of HostingNodeJSApi->restart_node_js_application_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingNodeJSApi->restart_node_js_application_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
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

# **start_node_js_build_v1**
> HostingV1NodeJsBuildResource start_node_js_build_v1(username, domain, hosting_v1_node_js_start_build_request)

Start Node.js build

Start a Node.js build process using files already present on the website's file storage.

WARNING: on success this overwrites the website's existing contents and cannot be
undone — verify this is intended before calling this endpoint.

The `source_type` must be `archive` and `source_options.archive_path` must point to an
existing archive file on the server (relative to the website document root).
Use the `Generate Upload URL` endpoint to obtain credentials and upload the archive first.

To auto-detect build settings from an archive before starting, first call the
`Get Node.js Build Settings from Archive` endpoint.

The returned build `uuid` can be used to poll progress and retrieve logs via
the `Get Node.js Build Logs` endpoint.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_node_js_build_resource import HostingV1NodeJsBuildResource
from hostinger_api.models.hosting_v1_node_js_start_build_request import HostingV1NodeJsStartBuildRequest
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
    hosting_v1_node_js_start_build_request = hostinger_api.HostingV1NodeJsStartBuildRequest() # HostingV1NodeJsStartBuildRequest | 

    try:
        # Start Node.js build
        api_response = api_instance.start_node_js_build_v1(username, domain, hosting_v1_node_js_start_build_request)
        print("The response of HostingNodeJSApi->start_node_js_build_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingNodeJSApi->start_node_js_build_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **hosting_v1_node_js_start_build_request** | [**HostingV1NodeJsStartBuildRequest**](HostingV1NodeJsStartBuildRequest.md)|  | 

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

# **update_node_js_build_settings_v1**
> HostingV1NodeJsStoredBuildSettingsResource update_node_js_build_settings_v1(username, domain, hosting_v1_node_js_update_build_settings_request)

Update Node.js build settings

Replaces the build settings stored for the website. Send the full set: `node_version` is
required and every nullable field you omit is stored as null. Creates the settings when
none exist yet.

This does not start a build. Stored settings drive Git auto-deployment builds; a build
started through the API uses the values sent in that request, so to rebuild with corrected
settings call `Start Node.js build` with the same values. Typical fixes: a wrong `app_type`
after auto-detection, or a missing `entry_file` for express, fastify, nest, nuxt and hono
apps.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_node_js_stored_build_settings_resource import HostingV1NodeJsStoredBuildSettingsResource
from hostinger_api.models.hosting_v1_node_js_update_build_settings_request import HostingV1NodeJsUpdateBuildSettingsRequest
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
    hosting_v1_node_js_update_build_settings_request = hostinger_api.HostingV1NodeJsUpdateBuildSettingsRequest() # HostingV1NodeJsUpdateBuildSettingsRequest | 

    try:
        # Update Node.js build settings
        api_response = api_instance.update_node_js_build_settings_v1(username, domain, hosting_v1_node_js_update_build_settings_request)
        print("The response of HostingNodeJSApi->update_node_js_build_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingNodeJSApi->update_node_js_build_settings_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **hosting_v1_node_js_update_build_settings_request** | [**HostingV1NodeJsUpdateBuildSettingsRequest**](HostingV1NodeJsUpdateBuildSettingsRequest.md)|  | 

### Return type

[**HostingV1NodeJsStoredBuildSettingsResource**](HostingV1NodeJsStoredBuildSettingsResource.md)

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

