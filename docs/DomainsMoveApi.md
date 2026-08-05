# hostinger_api.DomainsMoveApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_incoming_domain_move_v1**](DomainsMoveApi.md#accept_incoming_domain_move_v1) | **PUT** /api/domains/v1/move/incoming/{domain} | Accept incoming domain move
[**cancel_outgoing_domain_move_v1**](DomainsMoveApi.md#cancel_outgoing_domain_move_v1) | **DELETE** /api/domains/v1/move/outgoing/{domain} | Cancel outgoing domain move
[**get_incoming_domain_move_list_v1**](DomainsMoveApi.md#get_incoming_domain_move_list_v1) | **GET** /api/domains/v1/move/incoming | Get incoming domain move list
[**get_incoming_domain_move_v1**](DomainsMoveApi.md#get_incoming_domain_move_v1) | **GET** /api/domains/v1/move/incoming/{domain} | Get incoming domain move
[**get_outgoing_domain_move_list_v1**](DomainsMoveApi.md#get_outgoing_domain_move_list_v1) | **GET** /api/domains/v1/move/outgoing | Get outgoing domain move list
[**get_outgoing_domain_move_v1**](DomainsMoveApi.md#get_outgoing_domain_move_v1) | **GET** /api/domains/v1/move/outgoing/{domain} | Get outgoing domain move
[**reject_incoming_domain_move_v1**](DomainsMoveApi.md#reject_incoming_domain_move_v1) | **DELETE** /api/domains/v1/move/incoming/{domain} | Reject incoming domain move
[**start_outgoing_domain_move_v1**](DomainsMoveApi.md#start_outgoing_domain_move_v1) | **POST** /api/domains/v1/move/outgoing/{domain} | Start outgoing domain move


# **accept_incoming_domain_move_v1**
> CommonSuccessEmptyResource accept_incoming_domain_move_v1(domain, domains_v1_move_incoming_update_request)

Accept incoming domain move

Accept an incoming move for a specified domain.

The provided WHOIS profiles become the contacts of the domain, so they must belong
to your account and satisfy the requirements of the TLD. Only the contact types the
domain actually uses are applied, but all four profile IDs have to be provided.

The move has to still be waiting for your decision, already accepted moves
cannot be accepted again.

Accepting does not complete the move. A confirmation email is sent to the email address of
the new owner contact, and the domain changes hands only after the change is confirmed from it.
Until then the move stays in the `activating` status, which can be followed with the
[incoming move endpoint](#tag/domains-move).

Use this endpoint to take ownership of a domain offered to you.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.domains_v1_move_incoming_update_request import DomainsV1MoveIncomingUpdateRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsMoveApi(api_client)
    domain = 'mydomain.tld' # str | Domain name
    domains_v1_move_incoming_update_request = hostinger_api.DomainsV1MoveIncomingUpdateRequest() # DomainsV1MoveIncomingUpdateRequest | 

    try:
        # Accept incoming domain move
        api_response = api_instance.accept_incoming_domain_move_v1(domain, domains_v1_move_incoming_update_request)
        print("The response of DomainsMoveApi->accept_incoming_domain_move_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsMoveApi->accept_incoming_domain_move_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 
 **domains_v1_move_incoming_update_request** | [**DomainsV1MoveIncomingUpdateRequest**](DomainsV1MoveIncomingUpdateRequest.md)|  | 

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

# **cancel_outgoing_domain_move_v1**
> CommonSuccessEmptyResource cancel_outgoing_domain_move_v1(domain)

Cancel outgoing domain move

Cancel an outgoing move for a specified domain.

The move can only be cancelled while the receiving account has not accepted it yet.
The domain stays in your account.

Use this endpoint to withdraw a move you no longer want to complete.

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
    api_instance = hostinger_api.DomainsMoveApi(api_client)
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Cancel outgoing domain move
        api_response = api_instance.cancel_outgoing_domain_move_v1(domain)
        print("The response of DomainsMoveApi->cancel_outgoing_domain_move_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsMoveApi->cancel_outgoing_domain_move_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_incoming_domain_move_list_v1**
> List[DomainsV1MoveMoveResource] get_incoming_domain_move_list_v1()

Get incoming domain move list

Retrieve all domains other Hostinger accounts are moving to your account.

Moves of every status are returned, including the ones which already completed.

Use this endpoint to find domains waiting for you to accept them.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domains_v1_move_move_resource import DomainsV1MoveMoveResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsMoveApi(api_client)

    try:
        # Get incoming domain move list
        api_response = api_instance.get_incoming_domain_move_list_v1()
        print("The response of DomainsMoveApi->get_incoming_domain_move_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsMoveApi->get_incoming_domain_move_list_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DomainsV1MoveMoveResource]**](DomainsV1MoveMoveResource.md)

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

# **get_incoming_domain_move_v1**
> DomainsV1MoveMoveResource get_incoming_domain_move_v1(domain, force_sync=force_sync)

Get incoming domain move

Retrieve the incoming move for a specified domain.

Returns 404 when no account is moving this domain to you.

Use this endpoint to check whether a domain addressed to you is still waiting to be accepted.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domains_v1_move_move_resource import DomainsV1MoveMoveResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsMoveApi(api_client)
    domain = 'mydomain.tld' # str | Domain name
    force_sync = False # bool | Re-check the move against the registry before responding. Only has an effect while the move is in the `activating` status. (optional) (default to False)

    try:
        # Get incoming domain move
        api_response = api_instance.get_incoming_domain_move_v1(domain, force_sync=force_sync)
        print("The response of DomainsMoveApi->get_incoming_domain_move_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsMoveApi->get_incoming_domain_move_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 
 **force_sync** | **bool**| Re-check the move against the registry before responding. Only has an effect while the move is in the &#x60;activating&#x60; status. | [optional] [default to False]

### Return type

[**DomainsV1MoveMoveResource**](DomainsV1MoveMoveResource.md)

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

# **get_outgoing_domain_move_list_v1**
> List[DomainsV1MoveMoveResource] get_outgoing_domain_move_list_v1()

Get outgoing domain move list

Retrieve all domains you are moving to other Hostinger accounts.

Only moves which have not completed yet are returned.

Use this endpoint to track moves you have initiated and the accounts they are addressed to.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domains_v1_move_move_resource import DomainsV1MoveMoveResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsMoveApi(api_client)

    try:
        # Get outgoing domain move list
        api_response = api_instance.get_outgoing_domain_move_list_v1()
        print("The response of DomainsMoveApi->get_outgoing_domain_move_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsMoveApi->get_outgoing_domain_move_list_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DomainsV1MoveMoveResource]**](DomainsV1MoveMoveResource.md)

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

# **get_outgoing_domain_move_v1**
> DomainsV1MoveMoveResource get_outgoing_domain_move_v1(domain)

Get outgoing domain move

Retrieve the outgoing move for a specified domain.

Returns 404 when the domain has no move in progress.

Use this endpoint to track the status of a move you have initiated for a single domain.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.domains_v1_move_move_resource import DomainsV1MoveMoveResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsMoveApi(api_client)
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Get outgoing domain move
        api_response = api_instance.get_outgoing_domain_move_v1(domain)
        print("The response of DomainsMoveApi->get_outgoing_domain_move_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsMoveApi->get_outgoing_domain_move_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 

### Return type

[**DomainsV1MoveMoveResource**](DomainsV1MoveMoveResource.md)

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

# **reject_incoming_domain_move_v1**
> CommonSuccessEmptyResource reject_incoming_domain_move_v1(domain)

Reject incoming domain move

Reject an incoming move for a specified domain.

The domain stays in the account which initiated the move.
Moves you have already accepted cannot be rejected anymore.

Use this endpoint to decline a domain you do not want to take over.

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
    api_instance = hostinger_api.DomainsMoveApi(api_client)
    domain = 'mydomain.tld' # str | Domain name

    try:
        # Reject incoming domain move
        api_response = api_instance.reject_incoming_domain_move_v1(domain)
        print("The response of DomainsMoveApi->reject_incoming_domain_move_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsMoveApi->reject_incoming_domain_move_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **start_outgoing_domain_move_v1**
> CommonSuccessEmptyResource start_outgoing_domain_move_v1(domain, domains_v1_move_outgoing_store_request)

Start outgoing domain move

Initiate a move of a specified domain to another Hostinger account.

The receiving account has to already exist and accept the move before the domain changes hands.

The domain must be active. The subscription it belongs to is resolved automatically,
and the request is rejected with a 404 status code when the domain has no domain
subscription of its own.

Domains protected by premium protection require an additional verification step,
such requests are rejected with a 428 status code.

Use this endpoint to hand a domain over to another Hostinger user.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.domains_v1_move_outgoing_store_request import DomainsV1MoveOutgoingStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.DomainsMoveApi(api_client)
    domain = 'mydomain.tld' # str | Domain name
    domains_v1_move_outgoing_store_request = hostinger_api.DomainsV1MoveOutgoingStoreRequest() # DomainsV1MoveOutgoingStoreRequest | 

    try:
        # Start outgoing domain move
        api_response = api_instance.start_outgoing_domain_move_v1(domain, domains_v1_move_outgoing_store_request)
        print("The response of DomainsMoveApi->start_outgoing_domain_move_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsMoveApi->start_outgoing_domain_move_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name | 
 **domains_v1_move_outgoing_store_request** | [**DomainsV1MoveOutgoingStoreRequest**](DomainsV1MoveOutgoingStoreRequest.md)|  | 

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

