# hostinger_api.HostingDatabasesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_database_password_v1**](HostingDatabasesApi.md#change_database_password_v1) | **PATCH** /api/hosting/v1/accounts/{username}/databases/{name}/change-password | Change database password
[**create_account_database_v1**](HostingDatabasesApi.md#create_account_database_v1) | **POST** /api/hosting/v1/accounts/{username}/databases | Create account database
[**create_database_remote_connection_v1**](HostingDatabasesApi.md#create_database_remote_connection_v1) | **POST** /api/hosting/v1/accounts/{username}/databases/{name}/remote-connections | Create database remote connection
[**delete_account_database_v1**](HostingDatabasesApi.md#delete_account_database_v1) | **DELETE** /api/hosting/v1/accounts/{username}/databases/{name} | Delete account database
[**delete_database_remote_connection_v1**](HostingDatabasesApi.md#delete_database_remote_connection_v1) | **DELETE** /api/hosting/v1/accounts/{username}/databases/{name}/remote-connections | Delete database remote connection
[**get_php_my_admin_link_v1**](HostingDatabasesApi.md#get_php_my_admin_link_v1) | **GET** /api/hosting/v1/accounts/{username}/databases/{name}/phpmyadmin-link | Get phpMyAdmin link
[**list_account_databases_v1**](HostingDatabasesApi.md#list_account_databases_v1) | **GET** /api/hosting/v1/accounts/{username}/databases | List account databases
[**list_database_remote_connections_v1**](HostingDatabasesApi.md#list_database_remote_connections_v1) | **GET** /api/hosting/v1/accounts/{username}/databases/remote-connections | List database remote connections
[**repair_database_v1**](HostingDatabasesApi.md#repair_database_v1) | **PATCH** /api/hosting/v1/accounts/{username}/databases/{name}/repair | Repair database
[**setup_website_database_v1**](HostingDatabasesApi.md#setup_website_database_v1) | **POST** /api/hosting/v1/accounts/{username}/websites/{domain}/databases/setup | Setup website database


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

# **create_database_remote_connection_v1**
> CommonSuccessEmptyResource create_database_remote_connection_v1(username, name, hosting_v1_databases_remote_connections_create_remote_connection_request)

Create database remote connection

Allows a remote host to connect to the specified database.

Provide an IPv4/IPv6 address, or "%" to allow any host. The database name must be
the full name returned by the list databases endpoint.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.hosting_v1_databases_remote_connections_create_remote_connection_request import HostingV1DatabasesRemoteConnectionsCreateRemoteConnectionRequest
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
    hosting_v1_databases_remote_connections_create_remote_connection_request = hostinger_api.HostingV1DatabasesRemoteConnectionsCreateRemoteConnectionRequest() # HostingV1DatabasesRemoteConnectionsCreateRemoteConnectionRequest | 

    try:
        # Create database remote connection
        api_response = api_instance.create_database_remote_connection_v1(username, name, hosting_v1_databases_remote_connections_create_remote_connection_request)
        print("The response of HostingDatabasesApi->create_database_remote_connection_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDatabasesApi->create_database_remote_connection_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **name** | **str**| Full database name as returned by the list databases endpoint. | 
 **hosting_v1_databases_remote_connections_create_remote_connection_request** | [**HostingV1DatabasesRemoteConnectionsCreateRemoteConnectionRequest**](HostingV1DatabasesRemoteConnectionsCreateRemoteConnectionRequest.md)|  | 

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

# **delete_database_remote_connection_v1**
> CommonSuccessEmptyResource delete_database_remote_connection_v1(username, name, ip)

Delete database remote connection

Permanently removes a remote-access rule, revoking the given host's remote access to the database.

Identify the rule with the required ip query parameter (the IPv4/IPv6 address, or "%",
exactly as returned by the list remote connections endpoint). The database name must be
the full name returned by the list databases endpoint.

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
    ip = '192.0.2.10' # str | Remote host to revoke: the IPv4/IPv6 address, or \"%\", exactly as returned by the list remote connections endpoint.

    try:
        # Delete database remote connection
        api_response = api_instance.delete_database_remote_connection_v1(username, name, ip)
        print("The response of HostingDatabasesApi->delete_database_remote_connection_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDatabasesApi->delete_database_remote_connection_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **name** | **str**| Full database name as returned by the list databases endpoint. | 
 **ip** | **str**| Remote host to revoke: the IPv4/IPv6 address, or \&quot;%\&quot;, exactly as returned by the list remote connections endpoint. | 

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
    domain = 'example.com' # str | Filter by domain name (case-insensitive substring match) (optional)
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
 **domain** | **str**| Filter by domain name (case-insensitive substring match) | [optional] 
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

# **list_database_remote_connections_v1**
> List[HostingV1DatabasesRemoteConnectionsRemoteConnectionResource] list_database_remote_connections_v1(username, domain=domain)

List database remote connections

Returns the remote-access rules for the specified account: the remote hosts
(IPv4/IPv6 addresses, or "%" for any host) allowed to connect to the account databases.

Use the domain filter to only return rules for databases assigned to a specific domain.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_databases_remote_connections_remote_connection_resource import HostingV1DatabasesRemoteConnectionsRemoteConnectionResource
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
    domain = 'example.com' # str | Filter remote connections by the domain the database is assigned to. Rules for databases not assigned to any domain are always included. (optional)

    try:
        # List database remote connections
        api_response = api_instance.list_database_remote_connections_v1(username, domain=domain)
        print("The response of HostingDatabasesApi->list_database_remote_connections_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDatabasesApi->list_database_remote_connections_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Filter remote connections by the domain the database is assigned to. Rules for databases not assigned to any domain are always included. | [optional] 

### Return type

[**List[HostingV1DatabasesRemoteConnectionsRemoteConnectionResource]**](HostingV1DatabasesRemoteConnectionsRemoteConnectionResource.md)

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

# **setup_website_database_v1**
> HostingV1DatabasesWebsiteDatabaseResource setup_website_database_v1(username, domain, hosting_v1_databases_setup_database_request=hosting_v1_databases_setup_database_request)

Setup website database

Creates a new MySQL database for the website and writes its connection details into the
website's environment variables, then restarts the application. The platform generates the
password (and the database name and user, unless supplied). The password is never returned;
the application reads it from the environment.

Written variables: `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` and
`DATABASE_URL` (`mysql://user:password@host:port/name`, user and password percent-encoded).
Existing variables are kept. If the website already has any variable with one of these
names the call fails with 422 and nothing is created; the `Replace Node.js environment
variables` endpoint removes them.

After this call the variables are ordinary environment variables: the
`Replace Node.js environment variables` endpoint changes or removes them like any other.

A restart is enough for apps that read environment variables at process start, such as
Express or NestJS. Frameworks that bake variables into the build output (Next.js,
`NEXT_PUBLIC_*`) see the new values only after a fresh build (`Start Node.js build` endpoint).

A password in the request is ignored; the platform always generates it. The optional `name`
and `user` are identifiers, not secrets.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.hosting_v1_databases_setup_database_request import HostingV1DatabasesSetupDatabaseRequest
from hostinger_api.models.hosting_v1_databases_website_database_resource import HostingV1DatabasesWebsiteDatabaseResource
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
    domain = 'mydomain.tld' # str | Domain name
    hosting_v1_databases_setup_database_request = hostinger_api.HostingV1DatabasesSetupDatabaseRequest() # HostingV1DatabasesSetupDatabaseRequest |  (optional)

    try:
        # Setup website database
        api_response = api_instance.setup_website_database_v1(username, domain, hosting_v1_databases_setup_database_request=hosting_v1_databases_setup_database_request)
        print("The response of HostingDatabasesApi->setup_website_database_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingDatabasesApi->setup_website_database_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **domain** | **str**| Domain name | 
 **hosting_v1_databases_setup_database_request** | [**HostingV1DatabasesSetupDatabaseRequest**](HostingV1DatabasesSetupDatabaseRequest.md)|  | [optional] 

### Return type

[**HostingV1DatabasesWebsiteDatabaseResource**](HostingV1DatabasesWebsiteDatabaseResource.md)

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

