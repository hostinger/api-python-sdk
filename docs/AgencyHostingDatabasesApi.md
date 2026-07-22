# hostinger_api.AgencyHostingDatabasesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agency_plan_website_database_user_v1**](AgencyHostingDatabasesApi.md#create_agency_plan_website_database_user_v1) | **POST** /api/agency-hosting/v1/websites/{website_uid}/databases/{database_name}/users | Create Agency Plan website database user
[**create_agency_plan_website_database_v1**](AgencyHostingDatabasesApi.md#create_agency_plan_website_database_v1) | **POST** /api/agency-hosting/v1/websites/{website_uid}/databases | Create Agency Plan website database
[**delete_agency_plan_website_database_user_v1**](AgencyHostingDatabasesApi.md#delete_agency_plan_website_database_user_v1) | **DELETE** /api/agency-hosting/v1/websites/{website_uid}/databases/{database_name}/users/{database_user_name} | Delete Agency Plan website database user
[**delete_agency_plan_website_database_v1**](AgencyHostingDatabasesApi.md#delete_agency_plan_website_database_v1) | **DELETE** /api/agency-hosting/v1/websites/{website_uid}/databases/{database_name} | Delete Agency Plan website database
[**list_agency_plan_website_databases_v1**](AgencyHostingDatabasesApi.md#list_agency_plan_website_databases_v1) | **GET** /api/agency-hosting/v1/websites/{website_uid}/databases | List Agency Plan website databases


# **create_agency_plan_website_database_user_v1**
> AgencyHostingV1WebsitesDatabasesDatabaseUserResource create_agency_plan_website_database_user_v1(website_uid, database_name, agency_hosting_v1_websites_databases_users_create_database_user_request)

Create Agency Plan website database user

Creates a user for an existing database on an Agency Plan website.

Each database supports a single non-system user; creating a user for a database that already has one fails.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_websites_databases_database_user_resource import AgencyHostingV1WebsitesDatabasesDatabaseUserResource
from hostinger_api.models.agency_hosting_v1_websites_databases_users_create_database_user_request import AgencyHostingV1WebsitesDatabasesUsersCreateDatabaseUserRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingDatabasesApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    database_name = 'my_database' # str | Full database name as returned by the list databases endpoint.
    agency_hosting_v1_websites_databases_users_create_database_user_request = hostinger_api.AgencyHostingV1WebsitesDatabasesUsersCreateDatabaseUserRequest() # AgencyHostingV1WebsitesDatabasesUsersCreateDatabaseUserRequest | 

    try:
        # Create Agency Plan website database user
        api_response = api_instance.create_agency_plan_website_database_user_v1(website_uid, database_name, agency_hosting_v1_websites_databases_users_create_database_user_request)
        print("The response of AgencyHostingDatabasesApi->create_agency_plan_website_database_user_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingDatabasesApi->create_agency_plan_website_database_user_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
 **database_name** | **str**| Full database name as returned by the list databases endpoint. | 
 **agency_hosting_v1_websites_databases_users_create_database_user_request** | [**AgencyHostingV1WebsitesDatabasesUsersCreateDatabaseUserRequest**](AgencyHostingV1WebsitesDatabasesUsersCreateDatabaseUserRequest.md)|  | 

### Return type

[**AgencyHostingV1WebsitesDatabasesDatabaseUserResource**](AgencyHostingV1WebsitesDatabasesDatabaseUserResource.md)

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

# **create_agency_plan_website_database_v1**
> AgencyHostingV1WebsitesDatabasesDatabaseResource create_agency_plan_website_database_v1(website_uid, agency_hosting_v1_websites_databases_create_database_request)

Create Agency Plan website database

Creates a MySQL database with a dedicated user for an Agency Plan website.

The database name, username, and password must all be provided by the caller.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_websites_databases_create_database_request import AgencyHostingV1WebsitesDatabasesCreateDatabaseRequest
from hostinger_api.models.agency_hosting_v1_websites_databases_database_resource import AgencyHostingV1WebsitesDatabasesDatabaseResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingDatabasesApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    agency_hosting_v1_websites_databases_create_database_request = hostinger_api.AgencyHostingV1WebsitesDatabasesCreateDatabaseRequest() # AgencyHostingV1WebsitesDatabasesCreateDatabaseRequest | 

    try:
        # Create Agency Plan website database
        api_response = api_instance.create_agency_plan_website_database_v1(website_uid, agency_hosting_v1_websites_databases_create_database_request)
        print("The response of AgencyHostingDatabasesApi->create_agency_plan_website_database_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingDatabasesApi->create_agency_plan_website_database_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
 **agency_hosting_v1_websites_databases_create_database_request** | [**AgencyHostingV1WebsitesDatabasesCreateDatabaseRequest**](AgencyHostingV1WebsitesDatabasesCreateDatabaseRequest.md)|  | 

### Return type

[**AgencyHostingV1WebsitesDatabasesDatabaseResource**](AgencyHostingV1WebsitesDatabasesDatabaseResource.md)

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

# **delete_agency_plan_website_database_user_v1**
> CommonSuccessEmptyResource delete_agency_plan_website_database_user_v1(website_uid, database_name, database_user_name)

Delete Agency Plan website database user

Permanently deletes a database user from an Agency Plan website database, revoking all access it had.

The operation is idempotent: deleting a user that does not exist succeeds without error.

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
    api_instance = hostinger_api.AgencyHostingDatabasesApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    database_name = 'my_database' # str | Full database name as returned by the list databases endpoint.
    database_user_name = 'my_user' # str | Database username as returned by the list databases endpoint.

    try:
        # Delete Agency Plan website database user
        api_response = api_instance.delete_agency_plan_website_database_user_v1(website_uid, database_name, database_user_name)
        print("The response of AgencyHostingDatabasesApi->delete_agency_plan_website_database_user_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingDatabasesApi->delete_agency_plan_website_database_user_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
 **database_name** | **str**| Full database name as returned by the list databases endpoint. | 
 **database_user_name** | **str**| Database username as returned by the list databases endpoint. | 

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

# **delete_agency_plan_website_database_v1**
> CommonSuccessEmptyResource delete_agency_plan_website_database_v1(website_uid, database_name)

Delete Agency Plan website database

Permanently deletes a MySQL database and all its data from an Agency Plan website, including its users.

The operation is idempotent: deleting a database that does not exist succeeds without error.

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
    api_instance = hostinger_api.AgencyHostingDatabasesApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    database_name = 'my_database' # str | Full database name as returned by the list databases endpoint.

    try:
        # Delete Agency Plan website database
        api_response = api_instance.delete_agency_plan_website_database_v1(website_uid, database_name)
        print("The response of AgencyHostingDatabasesApi->delete_agency_plan_website_database_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingDatabasesApi->delete_agency_plan_website_database_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
 **database_name** | **str**| Full database name as returned by the list databases endpoint. | 

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

# **list_agency_plan_website_databases_v1**
> AgencyHostingListAgencyPlanWebsiteDatabasesV1200Response list_agency_plan_website_databases_v1(website_uid, page=page, per_page=per_page)

List Agency Plan website databases

Returns a paginated list of MySQL databases created for an Agency Plan website.

Each entry includes the database's non-system users.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_list_agency_plan_website_databases_v1200_response import AgencyHostingListAgencyPlanWebsiteDatabasesV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingDatabasesApi(api_client)
    website_uid = 'zpwlGlp19' # str | Agency Plan website UID
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List Agency Plan website databases
        api_response = api_instance.list_agency_plan_website_databases_v1(website_uid, page=page, per_page=per_page)
        print("The response of AgencyHostingDatabasesApi->list_agency_plan_website_databases_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingDatabasesApi->list_agency_plan_website_databases_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_uid** | **str**| Agency Plan website UID | 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**AgencyHostingListAgencyPlanWebsiteDatabasesV1200Response**](AgencyHostingListAgencyPlanWebsiteDatabasesV1200Response.md)

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

