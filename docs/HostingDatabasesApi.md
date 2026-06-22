# hostinger_api.HostingDatabasesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_database_password_v1**](HostingDatabasesApi.md#change_database_password_v1) | **PATCH** /api/hosting/v1/accounts/{username}/databases/{name}/change-password | Change database password
[**create_account_database_v1**](HostingDatabasesApi.md#create_account_database_v1) | **POST** /api/hosting/v1/accounts/{username}/databases | Create account database
[**delete_account_database_v1**](HostingDatabasesApi.md#delete_account_database_v1) | **DELETE** /api/hosting/v1/accounts/{username}/databases/{name} | Delete account database
[**get_php_my_admin_link_v1**](HostingDatabasesApi.md#get_php_my_admin_link_v1) | **GET** /api/hosting/v1/accounts/{username}/databases/{name}/phpmyadmin-link | Get phpMyAdmin link
[**list_account_databases_v1**](HostingDatabasesApi.md#list_account_databases_v1) | **GET** /api/hosting/v1/accounts/{username}/databases | List account databases
[**repair_database_v1**](HostingDatabasesApi.md#repair_database_v1) | **PATCH** /api/hosting/v1/accounts/{username}/databases/{name}/repair | Repair database


# **change_database_password_v1**
> CommonSuccessEmptyResource change_database_password_v1(username, name, hosting_v1_databases_change_database_password_request)

Change database password

Changes the password for the specified database user.

The database name must be the full name returned by the list databases endpoint.
The password must also be updated in any website configuration that uses this database.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.hosting_v1_databases_change_database_password_request import HostingV1DatabasesChangeDatabasePasswordRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingDatabasesApi(api_client)
    username = 'u123456789' # str | 
    name = 'u123456789_test_db' # str | Full database name as returned by the list databases endpoint.
    hosting_v1_databases_change_database_password_request = hostinger_api.HostingV1DatabasesChangeDatabasePasswordRequest() # HostingV1DatabasesChangeDatabasePasswordRequest | 

    try:
        # Change database password
        api_response = api_instance.change_database_password_v1(username, name, hosting_v1_databases_change_database_password_request)
        print("The response of HostingDatabasesApi->change_database_password_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDatabasesApi->change_database_password_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **name** | **str**| Full database name as returned by the list databases endpoint. | 
 **hosting_v1_databases_change_database_password_request** | [**HostingV1DatabasesChangeDatabasePasswordRequest**](HostingV1DatabasesChangeDatabasePasswordRequest.md)|  | 

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

# **create_account_database_v1**
> CommonSuccessEmptyResource create_account_database_v1(username, hosting_v1_databases_create_database_request)

Create account database

Creates a database with a database user and password for the specified account.

The database name and user are automatically prefixed with the account username when needed.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.hosting_v1_databases_create_database_request import HostingV1DatabasesCreateDatabaseRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingDatabasesApi(api_client)
    username = 'u123456789' # str | 
    hosting_v1_databases_create_database_request = hostinger_api.HostingV1DatabasesCreateDatabaseRequest() # HostingV1DatabasesCreateDatabaseRequest | 

    try:
        # Create account database
        api_response = api_instance.create_account_database_v1(username, hosting_v1_databases_create_database_request)
        print("The response of HostingDatabasesApi->create_account_database_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDatabasesApi->create_account_database_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **hosting_v1_databases_create_database_request** | [**HostingV1DatabasesCreateDatabaseRequest**](HostingV1DatabasesCreateDatabaseRequest.md)|  | 

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

# **delete_account_database_v1**
> CommonSuccessEmptyResource delete_account_database_v1(username, name)

Delete account database

Permanently deletes a database and its remote connections.

The database name must be the full name returned by the list databases endpoint.

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
    api_instance = hostinger_api.HostingDatabasesApi(api_client)
    username = 'u123456789' # str | 
    name = 'u123456789_test_db' # str | Full database name as returned by the list databases endpoint.

    try:
        # Delete account database
        api_response = api_instance.delete_account_database_v1(username, name)
        print("The response of HostingDatabasesApi->delete_account_database_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDatabasesApi->delete_account_database_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **name** | **str**| Full database name as returned by the list databases endpoint. | 

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

# **get_php_my_admin_link_v1**
> HostingV1DatabasesPhpMyAdminLinkResource get_php_my_admin_link_v1(username, name)

Get phpMyAdmin link

Returns a direct sign-on link to phpMyAdmin for the specified database.

Use this when a visual database interface is needed for SQL queries, imports, exports, or table management.
The database name must be the full name returned by the list databases endpoint.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_databases_php_my_admin_link_resource import HostingV1DatabasesPhpMyAdminLinkResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingDatabasesApi(api_client)
    username = 'u123456789' # str | 
    name = 'u123456789_test_db' # str | Full database name as returned by the list databases endpoint.

    try:
        # Get phpMyAdmin link
        api_response = api_instance.get_php_my_admin_link_v1(username, name)
        print("The response of HostingDatabasesApi->get_php_my_admin_link_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDatabasesApi->get_php_my_admin_link_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **name** | **str**| Full database name as returned by the list databases endpoint. | 

### Return type

[**HostingV1DatabasesPhpMyAdminLinkResource**](HostingV1DatabasesPhpMyAdminLinkResource.md)

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

# **list_account_databases_v1**
> HostingListAccountDatabasesV1200Response list_account_databases_v1(username, page=page, per_page=per_page, domain=domain, is_assigned=is_assigned, search=search)

List account databases

Returns a paginated list of databases for the specified account.

Use the domain and is_assigned filters to find databases assigned to a specific domain.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_list_account_databases_v1200_response import HostingListAccountDatabasesV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HostingDatabasesApi(api_client)
    username = 'u123456789' # str | 
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)
    domain = 'example.com' # str | Filter by domain name (exact match) (optional)
    is_assigned = true # bool | When used with domain, return only databases assigned to that domain. (optional)
    search = 'test_db' # str | Search databases by name, user, or creation date. (optional)

    try:
        # List account databases
        api_response = api_instance.list_account_databases_v1(username, page=page, per_page=per_page, domain=domain, is_assigned=is_assigned, search=search)
        print("The response of HostingDatabasesApi->list_account_databases_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDatabasesApi->list_account_databases_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]
 **domain** | **str**| Filter by domain name (exact match) | [optional] 
 **is_assigned** | **bool**| When used with domain, return only databases assigned to that domain. | [optional] 
 **search** | **str**| Search databases by name, user, or creation date. | [optional] 

### Return type

[**HostingListAccountDatabasesV1200Response**](HostingListAccountDatabasesV1200Response.md)

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

# **repair_database_v1**
> CommonSuccessEmptyResource repair_database_v1(username, name)

Repair database

Repairs corrupted database tables asynchronously.

Use when database errors, crashes, or corruption are reported.
The database name must be the full name returned by the list databases endpoint.

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
    api_instance = hostinger_api.HostingDatabasesApi(api_client)
    username = 'u123456789' # str | 
    name = 'u123456789_test_db' # str | Full database name as returned by the list databases endpoint.

    try:
        # Repair database
        api_response = api_instance.repair_database_v1(username, name)
        print("The response of HostingDatabasesApi->repair_database_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDatabasesApi->repair_database_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **name** | **str**| Full database name as returned by the list databases endpoint. | 

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

