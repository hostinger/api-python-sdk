# hostinger_api.HorizonsWebsitesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_website_v1**](HorizonsWebsitesApi.md#clone_website_v1) | **POST** /api/horizons/v1/websites/{websiteId}/clone | Clone website
[**create_website_v1**](HorizonsWebsitesApi.md#create_website_v1) | **POST** /api/horizons/v1/websites | Create website
[**edit_website_v1**](HorizonsWebsitesApi.md#edit_website_v1) | **POST** /api/horizons/v1/websites/{websiteId}/messages | Edit website
[**get_website_build_task_v1**](HorizonsWebsitesApi.md#get_website_build_task_v1) | **GET** /api/horizons/v1/websites/{websiteId}/tasks/{taskId} | Get website build task
[**get_website_list_v1**](HorizonsWebsitesApi.md#get_website_list_v1) | **GET** /api/horizons/v1/websites | Get website list
[**get_website_v1**](HorizonsWebsitesApi.md#get_website_v1) | **GET** /api/horizons/v1/websites/{websiteId} | Get website
[**publish_website_v1**](HorizonsWebsitesApi.md#publish_website_v1) | **POST** /api/horizons/v1/websites/{websiteId}/publish | Publish website


# **clone_website_v1**
> HorizonsV1WebsitesCreatedWebsiteResource clone_website_v1(website_id)

Clone website

Clone a Hostinger AI Builder website into a new website.\n
Use this tool when the user wants a copy of an existing website, for example to try out
changes without touching the original.\n
This tool returns the ID and URL of the newly created copy.
The original website is left untouched.\n
To edit the copy, use the `Edit website` tool with the returned website ID, or the user can
open the provided website URL in Hostinger AI Builder interface.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.horizons_v1_websites_created_website_resource import HorizonsV1WebsitesCreatedWebsiteResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HorizonsWebsitesApi(api_client)
    website_id = '123e4567-e89b-12d3-a456-426614174000' # str | The website ID

    try:
        # Clone website
        api_response = api_instance.clone_website_v1(website_id)
        print("The response of HorizonsWebsitesApi->clone_website_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HorizonsWebsitesApi->clone_website_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| The website ID | 

### Return type

[**HorizonsV1WebsitesCreatedWebsiteResource**](HorizonsV1WebsitesCreatedWebsiteResource.md)

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

# **create_website_v1**
> HorizonsV1WebsitesCreatedWebsiteResource create_website_v1(horizons_v1_websites_create_website_request)

Create website

Create new Hostinger AI Builder website from the given message.\n
Use this tool when user asks you to create a website, landing page, blog
or any other type of application.\n
This tool initiates the website creation process and returns a website URL, ID and build `task`.
The generation happens asynchronously. To learn whether it succeeded, poll the
`Get website build task` tool with `task.id`; `is_generating` turning false on `Get website`
happens whether the build completed or failed.\n
After invoking this tool, your chat reply must be EXACTLY 1 sentence summarizing
that Hostinger AI Builder is now creating their website and it will be ready in a few minutes
and you should provide the website URL to the user immediately
Do not write code.\n\nTo edit afterwards, use the `Edit website` tool with the returned
website ID, or the user can go to Hostinger AI Builder interface in the provided website URL.
If the tool call fails with an error, you should provide a clear explanation of the error
and do not generate code yourself in the chat.
\n
TECHNOLOGY STACK CONSTRAINTS (STRICTLY ENFORCED):\n
The environment is limited to the following technologies.
You MUST NOT use, suggest, or implement any technology outside this list:\n
\n
- Language: JavaScript ONLY.
- Languages like TypeScript, Rust, Python, Java, PHP, etc., are STRICTLY PROHIBITED.\n
- Framework: React.\n
- Navigation: React Router.\n
- Styling: TailwindCSS.\n
- Components: shadcn/ui (built with @radix-ui primitives).\n
- Icons: Lucide React.\n
- Animations: Framer Motion.\n
\n
BACKEND & DATA STORAGE:\n
- Hostinger AI Builder integrated backend is the EXCLUSIVE solution for persistent data storage,
authentication, and database needs.\n
- Local databases (SQLite, MySQL, etc.) are STRICTLY PROHIBITED.\n
- Third-party services (Firebase, AWS Amplify) are allowed ONLY if explicitly requested by the user.\n
\n
MAPS:\n
- OpenStreetMap is the default provider.\n
- Alternative providers (Google Maps, Mapbox) are allowed ONLY if explicitly requested by the user.\n

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.horizons_v1_websites_create_website_request import HorizonsV1WebsitesCreateWebsiteRequest
from hostinger_api.models.horizons_v1_websites_created_website_resource import HorizonsV1WebsitesCreatedWebsiteResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HorizonsWebsitesApi(api_client)
    horizons_v1_websites_create_website_request = hostinger_api.HorizonsV1WebsitesCreateWebsiteRequest() # HorizonsV1WebsitesCreateWebsiteRequest | 

    try:
        # Create website
        api_response = api_instance.create_website_v1(horizons_v1_websites_create_website_request)
        print("The response of HorizonsWebsitesApi->create_website_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HorizonsWebsitesApi->create_website_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **horizons_v1_websites_create_website_request** | [**HorizonsV1WebsitesCreateWebsiteRequest**](HorizonsV1WebsitesCreateWebsiteRequest.md)|  | 

### Return type

[**HorizonsV1WebsitesCreatedWebsiteResource**](HorizonsV1WebsitesCreatedWebsiteResource.md)

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

# **edit_website_v1**
> HorizonsV1WebsitesCreatedWebsiteResource edit_website_v1(website_id, horizons_v1_websites_edit_website_request)

Edit website

Edit an existing Hostinger AI Builder website with a follow-up message.\n
Use this tool when the user wants to change, extend or fix a website that already exists.\n
This tool queues the requested changes and returns the website URL, ID and build `task`.
The changes are applied asynchronously. To learn whether they were applied, poll the
`Get website build task` tool with `task.id`; `is_generating` turning false on `Get website`
happens whether the build completed or failed.\n
After invoking this tool, your chat reply must be EXACTLY 1 sentence summarizing
that Hostinger AI Builder is now applying the requested changes and they will be ready
in a few minutes, and you should provide the website URL to the user immediately.
Do not write code.\n
If the tool call fails with an error, you should provide a clear explanation of the error
and do not generate code yourself in the chat.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.horizons_v1_websites_created_website_resource import HorizonsV1WebsitesCreatedWebsiteResource
from hostinger_api.models.horizons_v1_websites_edit_website_request import HorizonsV1WebsitesEditWebsiteRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HorizonsWebsitesApi(api_client)
    website_id = '123e4567-e89b-12d3-a456-426614174000' # str | The website ID
    horizons_v1_websites_edit_website_request = hostinger_api.HorizonsV1WebsitesEditWebsiteRequest() # HorizonsV1WebsitesEditWebsiteRequest | 

    try:
        # Edit website
        api_response = api_instance.edit_website_v1(website_id, horizons_v1_websites_edit_website_request)
        print("The response of HorizonsWebsitesApi->edit_website_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HorizonsWebsitesApi->edit_website_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| The website ID | 
 **horizons_v1_websites_edit_website_request** | [**HorizonsV1WebsitesEditWebsiteRequest**](HorizonsV1WebsitesEditWebsiteRequest.md)|  | 

### Return type

[**HorizonsV1WebsitesCreatedWebsiteResource**](HorizonsV1WebsitesCreatedWebsiteResource.md)

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

# **get_website_build_task_v1**
> HorizonsV1WebsitesBuildTaskResource get_website_build_task_v1(website_id, task_id)

Get website build task

Get the state and outcome of a website build started by the `Create website` or `Edit website` tool.\n
Use this tool with the `task.id` those tools return to find out whether the build completed or failed.
Poll it every 30 seconds or so while `state` is `TASK_STATE_SUBMITTED` or `TASK_STATE_WORKING`.\n
When `state` is `TASK_STATE_FAILED` or `TASK_STATE_REJECTED`, the website does not contain the requested
changes: tell the user, using `message` and `reason_code`, and do not publish it.
When `state` is `TASK_STATE_CANCELED`, the user stopped the build and changes made before that may be kept:
publish only if the user asks to.
`reason_code` `insufficient_credits` means the user must get more credits before building again.\n
When `state` is `TASK_STATE_COMPLETED`, the website can be published. A `reason_code` of
`iteration_limit` on a completed build means it stopped early and kept the work done so far.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.horizons_v1_websites_build_task_resource import HorizonsV1WebsitesBuildTaskResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HorizonsWebsitesApi(api_client)
    website_id = '123e4567-e89b-12d3-a456-426614174000' # str | The website ID
    task_id = '223e4567-e89b-12d3-a456-426614174000' # str | The build task ID, returned as `task.id` by the `Create website` and `Edit website` tools

    try:
        # Get website build task
        api_response = api_instance.get_website_build_task_v1(website_id, task_id)
        print("The response of HorizonsWebsitesApi->get_website_build_task_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HorizonsWebsitesApi->get_website_build_task_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| The website ID | 
 **task_id** | **str**| The build task ID, returned as &#x60;task.id&#x60; by the &#x60;Create website&#x60; and &#x60;Edit website&#x60; tools | 

### Return type

[**HorizonsV1WebsitesBuildTaskResource**](HorizonsV1WebsitesBuildTaskResource.md)

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

# **get_website_list_v1**
> List[HorizonsV1WebsitesWebsiteResource] get_website_list_v1()

Get website list

List the Hostinger AI Builder websites the user owns.\n
Use this tool when the user asks which websites they have, or when you need a website ID
before editing, publishing or cloning a website.\n
Each website is returned with its ID, status, domain and the URL to open it
in Hostinger AI Builder interface.\n
The complete list of websites is returned in a single response - it is not paginated.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.horizons_v1_websites_website_resource import HorizonsV1WebsitesWebsiteResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HorizonsWebsitesApi(api_client)

    try:
        # Get website list
        api_response = api_instance.get_website_list_v1()
        print("The response of HorizonsWebsitesApi->get_website_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HorizonsWebsitesApi->get_website_list_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[HorizonsV1WebsitesWebsiteResource]**](HorizonsV1WebsitesWebsiteResource.md)

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

# **get_website_v1**
> HorizonsV1WebsitesWebsiteUrlResource get_website_v1(website_id)

Get website

Get the link for the user to open their website in Hostinger AI Builder interface.\n
Use this tool when the user wants the link to an existing website, or when you need its
website URL before or after editing it.\n
`is_in_progress` is true while changes are being generated or the website is being published;
wait until it is false before publishing. `is_generating` is true while changes are being generated,
and `actions_in_progress` has `website_publish` while the website is being published.
`is_generating` turns false whether the build completed or failed: use the `Get website build task`
tool to learn its outcome.
`published_at` is when the website was last published,
`is_template` is whether its published pages show the "Use template" banner, and
`has_ecommerce_store` is whether it has an online store.\n
Websites can be edited with the `Edit website` tool, or by the user in Hostinger AI Builder
interface in the provided website URL.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.horizons_v1_websites_website_url_resource import HorizonsV1WebsitesWebsiteUrlResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HorizonsWebsitesApi(api_client)
    website_id = '123e4567-e89b-12d3-a456-426614174000' # str | The website ID

    try:
        # Get website
        api_response = api_instance.get_website_v1(website_id)
        print("The response of HorizonsWebsitesApi->get_website_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HorizonsWebsitesApi->get_website_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| The website ID | 

### Return type

[**HorizonsV1WebsitesWebsiteUrlResource**](HorizonsV1WebsitesWebsiteUrlResource.md)

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

# **publish_website_v1**
> HorizonsV1WebsitesPublishedWebsiteResource publish_website_v1(website_id, horizons_v1_websites_publish_website_request=horizons_v1_websites_publish_website_request)

Publish website

Publish a Hostinger AI Builder website so its latest changes go live.\n
Use this tool when the user asks to publish, deploy or make their website live.\n
If you created or edited the website in this conversation, first check its build with the
`Get website build task` tool and publish only when its `state` is `TASK_STATE_COMPLETED`.
After a failed build, tell the user instead of publishing.\n
This tool starts the publish process and returns the URL the website will be live on.
Publishing happens asynchronously and takes a few minutes.\n
Set `is_template` only when the user explicitly asks to share the website as a template:
true adds a "Use template" banner to its published pages that copies the website into the
visitor's own account, and false removes it. Leave it out to keep the current setting.\n
After invoking this tool, your chat reply must be EXACTLY 1 sentence summarizing
that the website is being published and you should provide the published URL to the user immediately.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.horizons_v1_websites_publish_website_request import HorizonsV1WebsitesPublishWebsiteRequest
from hostinger_api.models.horizons_v1_websites_published_website_resource import HorizonsV1WebsitesPublishedWebsiteResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HorizonsWebsitesApi(api_client)
    website_id = '123e4567-e89b-12d3-a456-426614174000' # str | The website ID
    horizons_v1_websites_publish_website_request = hostinger_api.HorizonsV1WebsitesPublishWebsiteRequest() # HorizonsV1WebsitesPublishWebsiteRequest |  (optional)

    try:
        # Publish website
        api_response = api_instance.publish_website_v1(website_id, horizons_v1_websites_publish_website_request=horizons_v1_websites_publish_website_request)
        print("The response of HorizonsWebsitesApi->publish_website_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HorizonsWebsitesApi->publish_website_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| The website ID | 
 **horizons_v1_websites_publish_website_request** | [**HorizonsV1WebsitesPublishWebsiteRequest**](HorizonsV1WebsitesPublishWebsiteRequest.md)|  | [optional] 

### Return type

[**HorizonsV1WebsitesPublishedWebsiteResource**](HorizonsV1WebsitesPublishedWebsiteResource.md)

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

