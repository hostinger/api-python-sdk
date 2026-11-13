# hostinger_api.HostingPocketBaseApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pocket_base_backend_v1**](HostingPocketBaseApi.md#create_pocket_base_backend_v1) | **POST** /api/hosting/v1/accounts/{username}/websites/{domain}/pocketbase | Create PocketBase backend
[**delete_pocket_base_backend_v1**](HostingPocketBaseApi.md#delete_pocket_base_backend_v1) | **DELETE** /api/hosting/v1/accounts/{username}/websites/{domain}/pocketbase | Delete PocketBase backend
[**get_pocket_base_backend_v1**](HostingPocketBaseApi.md#get_pocket_base_backend_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/pocketbase | Get PocketBase backend
[**list_account_pocket_base_backends_v1**](HostingPocketBaseApi.md#list_account_pocket_base_backends_v1) | **GET** /api/hosting/v1/accounts/{username}/pocketbase | List account PocketBase backends
[**set_pocket_base_superuser_v1**](HostingPocketBaseApi.md#set_pocket_base_superuser_v1) | **PUT** /api/hosting/v1/accounts/{username}/websites/{domain}/pocketbase/superuser | Set PocketBase superuser


# **create_pocket_base_backend_v1**
> HostingV1PocketBaseBackendCreatedResource create_pocket_base_backend_v1(username, domain, hosting_v1_pocket_base_create_backend_request=hosting_v1_pocket_base_create_backend_request)

Create PocketBase backend

Creates a PocketBase backend for a website: a database, authentication, file storage and a
realtime REST API, served from the website's own domain. A website has at most one
PocketBase backend. Creation usually takes a few seconds.

The backend takes over the `/api` and `/_` paths of the website: from then on requests to
these paths and everything below them go to PocketBase, while every other path keeps
serving the website. Do not create a backend for a website that serves its own `/api` or
`/_` paths, because they stop working; confirm with the user before calling it. Deleting
the backend gives both paths back to the website. Headless WordPress websites and parked
domains are not supported; for a parked domain, use the website it is parked on. A website
that already has a backend is rejected with 422, unless that backend is in state
`missing`: then it is replaced with a new, empty one. A website set up with
`type: headless_empty` becomes `headless_pocketbase`; any other website keeps its type.

`superuser_password` is optional: leave it out to get a strong generated password, or send
your own (10-128 characters). The response returns it in `superuser_password` once and
Hostinger never stores it, so save it in your app secrets right away; you need it to manage
the backend through the PocketBase REST API. If it is lost, set a new one with the
`Set PocketBase superuser` endpoint. `superuser_email` defaults to the email of the
website owner.

The instance sleeps when idle and wakes on the first request, so the first call after a
quiet period can take a few seconds. `next_steps` in the response lists what to do next.

PocketBase is rolling out gradually: an account without access yet gets 422.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_pocket_base_backend_created_resource import HostingV1PocketBaseBackendCreatedResource
from hostinger_api.models.hosting_v1_pocket_base_create_backend_request import HostingV1PocketBaseCreateBackendRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingPocketBaseApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    hosting_v1_pocket_base_create_backend_request = hostinger_api.HostingV1PocketBaseCreateBackendRequest() # HostingV1PocketBaseCreateBackendRequest |  (optional)

    try:
        # Create PocketBase backend
        api_response = api_instance.create_pocket_base_backend_v1(username, domain, hosting_v1_pocket_base_create_backend_request=hosting_v1_pocket_base_create_backend_request)
        print("The response of HostingPocketBaseApi->create_pocket_base_backend_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingPocketBaseApi->create_pocket_base_backend_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **hosting_v1_pocket_base_create_backend_request** | [**HostingV1PocketBaseCreateBackendRequest**](HostingV1PocketBaseCreateBackendRequest.md)|  | [optional] 

### Return type

[**HostingV1PocketBaseBackendCreatedResource**](HostingV1PocketBaseBackendCreatedResource.md)

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
**404** | Error response |  -  |
**429** | Error response |  -  |
**503** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pocket_base_backend_v1**
> CommonSuccessEmptyResource delete_pocket_base_backend_v1(username, domain)

Delete PocketBase backend

Permanently deletes the PocketBase backend of a website with all its data (collections,
records, users and uploaded files) and gives the `/api` and `/_` paths back to the website;
a `headless_pocketbase` website becomes `headless_empty`. This cannot be undone and every
app using this backend stops working, so confirm with the user before calling it and
export the data you need from the dashboard (`admin_url`) first.

Returns success also when the website has no PocketBase backend; then it only clears a
`headless_pocketbase` mark. To regain access after losing the superuser password, use the
`Set PocketBase superuser` endpoint instead of deleting the backend.

PocketBase is rolling out gradually: an account without access yet gets 422; an unknown
website gets 404.

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
    api_instance = hostinger_api.HostingPocketBaseApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Delete PocketBase backend
        api_response = api_instance.delete_pocket_base_backend_v1(username, domain)
        print("The response of HostingPocketBaseApi->delete_pocket_base_backend_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingPocketBaseApi->delete_pocket_base_backend_v1: %s\n" % e)
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
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**404** | Error response |  -  |
**503** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pocket_base_backend_v1**
> HostingV1PocketBaseBackendResource get_pocket_base_backend_v1(username, domain)

Get PocketBase backend

Returns the PocketBase backend of a website: its REST API and dashboard URLs, live state
and version. A PocketBase backend gives the website a database, authentication, file
storage and a realtime REST API, served from the website's own domain under `/api` and
`/_`. Returns 404 when the website has no PocketBase backend.

The superuser password is only shown once, when it is set, and is never returned here. If it
is lost, set a new one with the `Set PocketBase superuser` endpoint.

The instance sleeps when idle and wakes on the first request, so `asleep` is a normal state
and the first call to a sleeping instance can take a few seconds. `starting`, `running` and
`stopping` are healthy.

`failed` means the last start did not succeed. Hostinger starts it again on its own after
`retry_after_seconds`, and the data is intact: wait and call again, do not delete the
backend. `failure_reason` says why: `process_limit` means the hosting account has no free
process slots, usually because its Node.js apps are running.

`unregistered` means the instance is broken. `missing` means its files are gone from the
server, and creating the PocketBase backend again sets up a new, empty one. `state` is null
when the server could not be reached; retry later.

PocketBase is rolling out gradually: an account without access yet gets 422.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_pocket_base_backend_resource import HostingV1PocketBaseBackendResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingPocketBaseApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Get PocketBase backend
        api_response = api_instance.get_pocket_base_backend_v1(username, domain)
        print("The response of HostingPocketBaseApi->get_pocket_base_backend_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingPocketBaseApi->get_pocket_base_backend_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 

### Return type

[**HostingV1PocketBaseBackendResource**](HostingV1PocketBaseBackendResource.md)

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
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_pocket_base_backends_v1**
> List[HostingV1PocketBaseInstanceResource] list_account_pocket_base_backends_v1(username)

List account PocketBase backends

Lists the PocketBase backends of all websites of a hosting account with their URLs, live
state, version and disk usage. A PocketBase backend gives a website a database,
authentication, file storage and a realtime REST API, served from the website's own
domain. An empty list means no website of the account has a PocketBase backend.

States: `asleep` is normal (the instance sleeps when idle and wakes on the first request);
`starting`, `running` and `stopping` are healthy.

`failed` means the last start did not succeed. Hostinger starts it again on its own after
`retry_after_seconds`, and the data is intact: wait and call again, do not delete the
backend. `failure_reason` says why: `process_limit` means the hosting account has no free
process slots, usually because its Node.js apps are running.

`unregistered` means the instance is broken. `missing` means its files are gone from the
server, and creating the PocketBase backend again sets up a new, empty one. `state` is null
when the server could not be reached; retry later.

PocketBase is rolling out gradually: an account without access yet gets 422.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_pocket_base_instance_resource import HostingV1PocketBaseInstanceResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingPocketBaseApi(api_client)
    username = 'u123456789' # str | 

    try:
        # List account PocketBase backends
        api_response = api_instance.list_account_pocket_base_backends_v1(username)
        print("The response of HostingPocketBaseApi->list_account_pocket_base_backends_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingPocketBaseApi->list_account_pocket_base_backends_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**List[HostingV1PocketBaseInstanceResource]**](HostingV1PocketBaseInstanceResource.md)

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
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_pocket_base_superuser_v1**
> HostingV1PocketBaseSuperuserResource set_pocket_base_superuser_v1(username, domain, hosting_v1_pocket_base_update_superuser_request=hosting_v1_pocket_base_update_superuser_request)

Set PocketBase superuser

Sets the password of a superuser of the website's PocketBase backend, and creates that
superuser when there is none with the given email. The old password of that superuser stops
working at once, so apps and scripts still using it lose superuser access; confirm with the
user before calling it.

Use it when the superuser password is lost (Hostinger never stores it), when it leaked and
must be rotated, or to add another superuser with a different email. Returns 404 when the
website has no PocketBase backend; create one first. App user accounts are managed through
the PocketBase REST API, not here.

`superuser_password` is optional: leave it out to get a strong generated password, or send
your own (10-128 characters). The response returns it in `superuser_password` once and
Hostinger never stores it, so save it in your app secrets right away, then authenticate
again with `pb.collection('_superusers').authWithPassword`. `superuser_email` defaults to
the email of the website owner.

PocketBase is rolling out gradually: an account without access yet gets 422.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_pocket_base_superuser_resource import HostingV1PocketBaseSuperuserResource
from hostinger_api.models.hosting_v1_pocket_base_update_superuser_request import HostingV1PocketBaseUpdateSuperuserRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingPocketBaseApi(api_client)
    username = 'u123456789' # str | 
    domain = 'mydomain.tld' # str | Domain name
    hosting_v1_pocket_base_update_superuser_request = hostinger_api.HostingV1PocketBaseUpdateSuperuserRequest() # HostingV1PocketBaseUpdateSuperuserRequest |  (optional)

    try:
        # Set PocketBase superuser
        api_response = api_instance.set_pocket_base_superuser_v1(username, domain, hosting_v1_pocket_base_update_superuser_request=hosting_v1_pocket_base_update_superuser_request)
        print("The response of HostingPocketBaseApi->set_pocket_base_superuser_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingPocketBaseApi->set_pocket_base_superuser_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **hosting_v1_pocket_base_update_superuser_request** | [**HostingV1PocketBaseUpdateSuperuserRequest**](HostingV1PocketBaseUpdateSuperuserRequest.md)|  | [optional] 

### Return type

[**HostingV1PocketBaseSuperuserResource**](HostingV1PocketBaseSuperuserResource.md)

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
**404** | Error response |  -  |
**429** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

