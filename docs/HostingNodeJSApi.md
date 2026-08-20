# hostinger_api.HostingNodeJSApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_node_js_build_logs_v1**](HostingNodeJSApi.md#get_node_js_build_logs_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds/{uuid}/logs | Get NodeJS build logs
[**get_node_js_build_settings_from_archive_v1**](HostingNodeJSApi.md#get_node_js_build_settings_from_archive_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds/settings/from-archive | Get Node.js build settings from archive
[**list_node_js_builds_v1**](HostingNodeJSApi.md#list_node_js_builds_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds | List NodeJS builds
[**list_node_js_vulnerabilities_v1**](HostingNodeJSApi.md#list_node_js_vulnerabilities_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/vulnerabilities | List Node.js vulnerabilities
[**patch_node_js_vulnerabilities_v1**](HostingNodeJSApi.md#patch_node_js_vulnerabilities_v1) | **POST** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/vulnerabilities/patch | Patch Node.js vulnerabilities
[**restart_node_js_application_v1**](HostingNodeJSApi.md#restart_node_js_application_v1) | **POST** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/server/restart | Restart Node.js application
[**start_node_js_build_v1**](HostingNodeJSApi.md#start_node_js_build_v1) | **POST** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds | Start Node.js build


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
To upload an archive and start a build in one step without inspecting settings first,
use the `Create Node.js Build from Archive` endpoint instead.

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
`Get Node.js Build Settings from Archive` endpoint. To upload an archive and start
a build in one step, use the `Create Node.js Build from Archive` endpoint instead.

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

