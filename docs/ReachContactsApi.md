# hostinger_api.ReachContactsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_new_contact_v1**](ReachContactsApi.md#create_a_new_contact_v1) | **POST** /api/reach/v1/contacts | Create a new contact
[**create_contacts_in_bulk_v1**](ReachContactsApi.md#create_contacts_in_bulk_v1) | **POST** /api/reach/v1/profiles/{profileUuid}/contacts/bulk | Create contacts in bulk
[**create_new_contacts_v1**](ReachContactsApi.md#create_new_contacts_v1) | **POST** /api/reach/v1/profiles/{profileUuid}/contacts | Create new contacts
[**delete_a_contact_v1**](ReachContactsApi.md#delete_a_contact_v1) | **DELETE** /api/reach/v1/contacts/{uuid} | Delete a contact
[**delete_a_profile_contact_v1**](ReachContactsApi.md#delete_a_profile_contact_v1) | **DELETE** /api/reach/v1/profiles/{profileUuid}/contacts/{contactUuid} | Delete a profile contact
[**get_contact_details_v1**](ReachContactsApi.md#get_contact_details_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/contacts/{contactUuid} | Get contact details
[**list_contact_groups_v1**](ReachContactsApi.md#list_contact_groups_v1) | **GET** /api/reach/v1/contacts/groups | List contact groups
[**list_contacts_v1**](ReachContactsApi.md#list_contacts_v1) | **GET** /api/reach/v1/contacts | List contacts
[**list_profile_contacts_v1**](ReachContactsApi.md#list_profile_contacts_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/contacts | List profile contacts
[**update_a_contact_v1**](ReachContactsApi.md#update_a_contact_v1) | **PATCH** /api/reach/v1/profiles/{profileUuid}/contacts/{contactUuid} | Update a contact


# **create_a_new_contact_v1**
> CommonSuccessEmptyResource create_a_new_contact_v1(reach_v1_contacts_store_request)

Create a new contact

Create a new contact in the email marketing system.

This endpoint allows you to create a new contact with basic information like name, email, and surname.

If double opt-in is enabled,
the contact will be created with a pending status and a confirmation email will be sent.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.reach_v1_contacts_store_request import ReachV1ContactsStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachContactsApi(api_client)
    reach_v1_contacts_store_request = hostinger_api.ReachV1ContactsStoreRequest() # ReachV1ContactsStoreRequest | 

    try:
        # Create a new contact
        api_response = api_instance.create_a_new_contact_v1(reach_v1_contacts_store_request)
        print("The response of ReachContactsApi->create_a_new_contact_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachContactsApi->create_a_new_contact_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reach_v1_contacts_store_request** | [**ReachV1ContactsStoreRequest**](ReachV1ContactsStoreRequest.md)|  | 

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

# **create_contacts_in_bulk_v1**
> CommonSuccessEmptyResource create_contacts_in_bulk_v1(profile_uuid, reach_v1_contacts_bulk_store_request)

Create contacts in bulk

Create many contacts in a profile in a single call.

The contacts are imported in the background, so a success response means the import was
accepted rather than finished. Contacts whose email already exists in the profile are
left as they are. If double opt-in is enabled, new contacts start off pending and are
sent a confirmation email.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.reach_v1_contacts_bulk_store_request import ReachV1ContactsBulkStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachContactsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    reach_v1_contacts_bulk_store_request = hostinger_api.ReachV1ContactsBulkStoreRequest() # ReachV1ContactsBulkStoreRequest | 

    try:
        # Create contacts in bulk
        api_response = api_instance.create_contacts_in_bulk_v1(profile_uuid, reach_v1_contacts_bulk_store_request)
        print("The response of ReachContactsApi->create_contacts_in_bulk_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachContactsApi->create_contacts_in_bulk_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **reach_v1_contacts_bulk_store_request** | [**ReachV1ContactsBulkStoreRequest**](ReachV1ContactsBulkStoreRequest.md)|  | 

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

# **create_new_contacts_v1**
> CommonSuccessEmptyResource create_new_contacts_v1(profile_uuid, reach_v1_contacts_store_request)

Create new contacts

Create a new contact in the email marketing system.

This endpoint allows you to create a new contact with basic information like name, email, and surname.

If double opt-in is enabled, the contact will be created with a pending status
and a confirmation email will be sent.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.reach_v1_contacts_store_request import ReachV1ContactsStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachContactsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    reach_v1_contacts_store_request = hostinger_api.ReachV1ContactsStoreRequest() # ReachV1ContactsStoreRequest | 

    try:
        # Create new contacts
        api_response = api_instance.create_new_contacts_v1(profile_uuid, reach_v1_contacts_store_request)
        print("The response of ReachContactsApi->create_new_contacts_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachContactsApi->create_new_contacts_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **reach_v1_contacts_store_request** | [**ReachV1ContactsStoreRequest**](ReachV1ContactsStoreRequest.md)|  | 

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

# **delete_a_contact_v1**
> CommonSuccessEmptyResource delete_a_contact_v1(uuid)

Delete a contact

Delete a contact with the specified UUID.

This endpoint permanently removes a contact from the email marketing system.

**Deprecated.** This endpoint cannot target a profile, so it always falls back to the
client's default profile and cannot delete contacts of any other profile. Use
`DELETE /api/reach/v1/profiles/{profileUuid}/contacts/{contactUuid}` instead.

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
    api_instance = hostinger_api.ReachContactsApi(api_client)
    uuid = 'uuid_example' # str | UUID of the contact to delete

    try:
        # Delete a contact
        api_response = api_instance.delete_a_contact_v1(uuid)
        print("The response of ReachContactsApi->delete_a_contact_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachContactsApi->delete_a_contact_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the contact to delete | 

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
**200** | Success response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_a_profile_contact_v1**
> CommonSuccessEmptyResource delete_a_profile_contact_v1(profile_uuid, contact_uuid)

Delete a profile contact

Permanently delete a contact from a profile.

The contact is removed together with its custom field values and tag assignments.

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
    api_instance = hostinger_api.ReachContactsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    contact_uuid = '550e8400-e29b-41d4-a716-446655440000' # str | Contact uuid parameter

    try:
        # Delete a profile contact
        api_response = api_instance.delete_a_profile_contact_v1(profile_uuid, contact_uuid)
        print("The response of ReachContactsApi->delete_a_profile_contact_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachContactsApi->delete_a_profile_contact_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **contact_uuid** | **str**| Contact uuid parameter | 

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

# **get_contact_details_v1**
> ReachV1ContactsContactDetailsResource get_contact_details_v1(profile_uuid, contact_uuid)

Get contact details

Get the full details of a single contact.

Alongside the contact's own attributes this returns the tags assigned to it and the
values it holds for the profile's custom contact fields.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_contact_details_resource import ReachV1ContactsContactDetailsResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachContactsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    contact_uuid = '550e8400-e29b-41d4-a716-446655440000' # str | Contact uuid parameter

    try:
        # Get contact details
        api_response = api_instance.get_contact_details_v1(profile_uuid, contact_uuid)
        print("The response of ReachContactsApi->get_contact_details_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachContactsApi->get_contact_details_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **contact_uuid** | **str**| Contact uuid parameter | 

### Return type

[**ReachV1ContactsContactDetailsResource**](ReachV1ContactsContactDetailsResource.md)

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

# **list_contact_groups_v1**
> List[ReachV1ContactsGroupsContactGroupResource] list_contact_groups_v1()

List contact groups

Get a list of all contact groups.

This endpoint returns a list of contact groups that can be used to organize contacts.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_groups_contact_group_resource import ReachV1ContactsGroupsContactGroupResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachContactsApi(api_client)

    try:
        # List contact groups
        api_response = api_instance.list_contact_groups_v1()
        print("The response of ReachContactsApi->list_contact_groups_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachContactsApi->list_contact_groups_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ReachV1ContactsGroupsContactGroupResource]**](ReachV1ContactsGroupsContactGroupResource.md)

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

# **list_contacts_v1**
> ReachListContactsV1200Response list_contacts_v1(group_uuid=group_uuid, subscription_status=subscription_status, page=page)

List contacts

Get a list of contacts, optionally filtered by group and subscription status.

This endpoint returns a paginated list of contacts with their basic information.
You can filter contacts by group UUID and subscription status.

**Deprecated.** This endpoint cannot target a profile, so it always falls back to the
client's default profile and cannot list contacts of any other profile. Use
`GET /api/reach/v1/profiles/{profileUuid}/contacts` instead, which also replaces the
group filter with a tag filter.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_list_contacts_v1200_response import ReachListContactsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachContactsApi(api_client)
    group_uuid = '550e8400-e29b-41d4-a716-446655440000' # str | Filter contacts by group UUID (optional)
    subscription_status = 'subscribed' # str | Filter contacts by subscription status (optional)
    page = 1 # int | Page number (optional)

    try:
        # List contacts
        api_response = api_instance.list_contacts_v1(group_uuid=group_uuid, subscription_status=subscription_status, page=page)
        print("The response of ReachContactsApi->list_contacts_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachContactsApi->list_contacts_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uuid** | **str**| Filter contacts by group UUID | [optional] 
 **subscription_status** | **str**| Filter contacts by subscription status | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**ReachListContactsV1200Response**](ReachListContactsV1200Response.md)

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

# **list_profile_contacts_v1**
> ReachListProfileContactsV1200Response list_profile_contacts_v1(profile_uuid, subscription_status=subscription_status, tag_uuid=tag_uuid, search=search, page=page, per_page=per_page)

List profile contacts

Get a paginated list of contacts belonging to a profile.

Contacts can be filtered by subscription status, by tag, and by an email search term.
The `meta.total` field of the response is the number of contacts matching the filters,
so calling this endpoint without filters gives the profile's total contact count.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_list_profile_contacts_v1200_response import ReachListProfileContactsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachContactsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    subscription_status = 'subscribed' # str | Filter contacts by subscription status (optional)
    tag_uuid = '550e8400-e29b-41d4-a716-446655440000' # str | Filter contacts by tag UUID (optional)
    search = 'john.doe@example.com' # str | Search contacts by email (optional)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List profile contacts
        api_response = api_instance.list_profile_contacts_v1(profile_uuid, subscription_status=subscription_status, tag_uuid=tag_uuid, search=search, page=page, per_page=per_page)
        print("The response of ReachContactsApi->list_profile_contacts_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachContactsApi->list_profile_contacts_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **subscription_status** | **str**| Filter contacts by subscription status | [optional] 
 **tag_uuid** | **str**| Filter contacts by tag UUID | [optional] 
 **search** | **str**| Search contacts by email | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**ReachListProfileContactsV1200Response**](ReachListProfileContactsV1200Response.md)

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

# **update_a_contact_v1**
> ReachV1ContactsProfileContactUpdateResource update_a_contact_v1(profile_uuid, contact_uuid, reach_v1_contacts_update_request)

Update a contact

Update a contact's attributes and custom field values.

Only the properties present in the request body are changed, so a partial body is enough
to change a single attribute. Sending a property as `null` clears it.

The response carries the contact's core attributes. Read back its tags, custom field
values, source and note with `GET /api/reach/v1/profiles/{profileUuid}/contacts/{contactUuid}`.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_contacts_profile_contact_update_resource import ReachV1ContactsProfileContactUpdateResource
from hostinger_api.models.reach_v1_contacts_update_request import ReachV1ContactsUpdateRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachContactsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    contact_uuid = '550e8400-e29b-41d4-a716-446655440000' # str | Contact uuid parameter
    reach_v1_contacts_update_request = hostinger_api.ReachV1ContactsUpdateRequest() # ReachV1ContactsUpdateRequest | 

    try:
        # Update a contact
        api_response = api_instance.update_a_contact_v1(profile_uuid, contact_uuid, reach_v1_contacts_update_request)
        print("The response of ReachContactsApi->update_a_contact_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachContactsApi->update_a_contact_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **contact_uuid** | **str**| Contact uuid parameter | 
 **reach_v1_contacts_update_request** | [**ReachV1ContactsUpdateRequest**](ReachV1ContactsUpdateRequest.md)|  | 

### Return type

[**ReachV1ContactsProfileContactUpdateResource**](ReachV1ContactsProfileContactUpdateResource.md)

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

