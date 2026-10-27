# hostinger_api.ReachIntegrationsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connect_ai_website_builder_site_v1**](ReachIntegrationsApi.md#connect_ai_website_builder_site_v1) | **POST** /api/reach/v1/profiles/{profileUuid}/websites/website-builder | Connect AI Website Builder site
[**disconnect_ai_website_builder_site_v1**](ReachIntegrationsApi.md#disconnect_ai_website_builder_site_v1) | **DELETE** /api/reach/v1/profiles/{profileUuid}/websites/website-builder | Disconnect AI Website Builder site
[**disconnect_ecommerce_store_v1**](ReachIntegrationsApi.md#disconnect_ecommerce_store_v1) | **DELETE** /api/reach/v1/profiles/{profileUuid}/ecommerce/stores/{storeId} | Disconnect Ecommerce store
[**disconnect_word_press_site_v1**](ReachIntegrationsApi.md#disconnect_word_press_site_v1) | **DELETE** /api/reach/v1/profiles/{profileUuid}/websites/wordpress | Disconnect WordPress site
[**list_connected_websites_v1**](ReachIntegrationsApi.md#list_connected_websites_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/websites | List connected websites
[**list_ecommerce_stores_v1**](ReachIntegrationsApi.md#list_ecommerce_stores_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/ecommerce/stores | List Ecommerce stores


# **connect_ai_website_builder_site_v1**
> CommonSuccessEmptyResource connect_ai_website_builder_site_v1(profile_uuid, reach_v1_websites_website_builder_connect_request)

Connect AI Website Builder site

Connect an AI Website Builder site the customer built manually to the profile, so its
subscribers flow into Reach.

Fails with not found when the customer owns no AI Website Builder site with that domain.
Fails with `DOMAIN_ALREADY_EXISTS` when the domain is connected to any profile - to move a
site to another plan, disconnect it from the old profile first - and with
`WEBSITE_CONNECTION_ALREADY_EXISTS` when this profile already has an AI Website Builder site.
The eCommerce store selling on the site, if it is not connected anywhere, is connected too.
WordPress sites and sites made with the agentic AI Website Builder cannot be connected here.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.reach_v1_websites_website_builder_connect_request import ReachV1WebsitesWebsiteBuilderConnectRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachIntegrationsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    reach_v1_websites_website_builder_connect_request = hostinger_api.ReachV1WebsitesWebsiteBuilderConnectRequest() # ReachV1WebsitesWebsiteBuilderConnectRequest | 

    try:
        # Connect AI Website Builder site
        api_response = api_instance.connect_ai_website_builder_site_v1(profile_uuid, reach_v1_websites_website_builder_connect_request)
        print("The response of ReachIntegrationsApi->connect_ai_website_builder_site_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachIntegrationsApi->connect_ai_website_builder_site_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **reach_v1_websites_website_builder_connect_request** | [**ReachV1WebsitesWebsiteBuilderConnectRequest**](ReachV1WebsitesWebsiteBuilderConnectRequest.md)|  | 

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
**401** | Unauthenticated response |  -  |
**422** | Validation error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disconnect_ai_website_builder_site_v1**
> CommonSuccessEmptyResource disconnect_ai_website_builder_site_v1(profile_uuid, reach_v1_websites_website_builder_disconnect_request)

Disconnect AI Website Builder site

Disconnect an AI Website Builder site from the profile; the site stops sending subscribers
to Reach.

Take `domain` from the list connected websites endpoint. Works for a site that was already
deleted in the builder. Fails with not found when the domain is not connected to this
profile. Contacts and any connected eCommerce store stay. The site stays disconnected until
it is connected again, so confirm the site and the plan with the customer before calling.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.reach_v1_websites_website_builder_disconnect_request import ReachV1WebsitesWebsiteBuilderDisconnectRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachIntegrationsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    reach_v1_websites_website_builder_disconnect_request = hostinger_api.ReachV1WebsitesWebsiteBuilderDisconnectRequest() # ReachV1WebsitesWebsiteBuilderDisconnectRequest | 

    try:
        # Disconnect AI Website Builder site
        api_response = api_instance.disconnect_ai_website_builder_site_v1(profile_uuid, reach_v1_websites_website_builder_disconnect_request)
        print("The response of ReachIntegrationsApi->disconnect_ai_website_builder_site_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachIntegrationsApi->disconnect_ai_website_builder_site_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **reach_v1_websites_website_builder_disconnect_request** | [**ReachV1WebsitesWebsiteBuilderDisconnectRequest**](ReachV1WebsitesWebsiteBuilderDisconnectRequest.md)|  | 

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

# **disconnect_ecommerce_store_v1**
> CommonSuccessEmptyResource disconnect_ecommerce_store_v1(profile_uuid, store_id)

Disconnect Ecommerce store

Disconnect an eCommerce store from the profile.

Reach stops receiving the store's customers and orders, and its products and coupons are
removed from Reach; contacts and past orders stay. Take `store_id` from the list eCommerce
stores endpoint; for a store that is `connected_to_other_profile`, call this with that
profile. Also succeeds when the store is not connected to this profile, so success is not
proof that anything was disconnected. Confirm the store and the plan with the customer
before calling.

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
    api_instance = hostinger_api.ReachIntegrationsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    store_id = 'ec_123' # str | Hostinger eCommerce store ID, as returned by the eCommerce stores list

    try:
        # Disconnect Ecommerce store
        api_response = api_instance.disconnect_ecommerce_store_v1(profile_uuid, store_id)
        print("The response of ReachIntegrationsApi->disconnect_ecommerce_store_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachIntegrationsApi->disconnect_ecommerce_store_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **store_id** | **str**| Hostinger eCommerce store ID, as returned by the eCommerce stores list | 

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

# **disconnect_word_press_site_v1**
> CommonSuccessEmptyResource disconnect_word_press_site_v1(profile_uuid, reach_v1_websites_word_press_disconnect_request)

Disconnect WordPress site

Disconnect a WordPress site from the profile.

The Reach plugin on the site stops sending subscribers and store data, and the site's
products and coupons are removed from Reach; contacts and past orders stay. Take `domain`
from the list connected websites endpoint. Fails with not found when the domain is not
connected to this profile. This cannot be undone through the API - the customer reconnects
from the WordPress plugin - so confirm the site and the plan with the customer before calling.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.common_success_empty_resource import CommonSuccessEmptyResource
from hostinger_api.models.reach_v1_websites_word_press_disconnect_request import ReachV1WebsitesWordPressDisconnectRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachIntegrationsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    reach_v1_websites_word_press_disconnect_request = hostinger_api.ReachV1WebsitesWordPressDisconnectRequest() # ReachV1WebsitesWordPressDisconnectRequest | 

    try:
        # Disconnect WordPress site
        api_response = api_instance.disconnect_word_press_site_v1(profile_uuid, reach_v1_websites_word_press_disconnect_request)
        print("The response of ReachIntegrationsApi->disconnect_word_press_site_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachIntegrationsApi->disconnect_word_press_site_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **reach_v1_websites_word_press_disconnect_request** | [**ReachV1WebsitesWordPressDisconnectRequest**](ReachV1WebsitesWordPressDisconnectRequest.md)|  | 

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

# **list_connected_websites_v1**
> List[ReachV1WebsitesWebsiteResource] list_connected_websites_v1(profile_uuid)

List connected websites

Get the websites connected to the profile, each with its `domain` and `platform_type`.

A domain is connected to at most one profile, so to find which plan a site is on, call this
for each profile. Only connected sites are listed, not every website the customer owns, and
eCommerce stores are not included - use the list eCommerce stores endpoint for those. Pass
`domain` to the disconnect WordPress site or disconnect AI Website Builder site endpoint.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_websites_website_resource import ReachV1WebsitesWebsiteResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachIntegrationsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter

    try:
        # List connected websites
        api_response = api_instance.list_connected_websites_v1(profile_uuid)
        print("The response of ReachIntegrationsApi->list_connected_websites_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachIntegrationsApi->list_connected_websites_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 

### Return type

[**List[ReachV1WebsitesWebsiteResource]**](ReachV1WebsitesWebsiteResource.md)

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

# **list_ecommerce_stores_v1**
> List[ReachV1StoresStoreResource] list_ecommerce_stores_v1(profile_uuid)

List Ecommerce stores

Get all of the customer's Hostinger eCommerce stores, each with its `store_id` and
`connection_status` for the profile in the path.

A store is connected to at most one profile. `connected_to_other_profile` does not name that
profile - call this for each profile to find it. The list is empty, not an error, when the
eCommerce service cannot be reached. Pass `store_id` to the disconnect eCommerce store
endpoint. Connecting an AI Website Builder site connects the store selling on it.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_stores_store_resource import ReachV1StoresStoreResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachIntegrationsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter

    try:
        # List Ecommerce stores
        api_response = api_instance.list_ecommerce_stores_v1(profile_uuid)
        print("The response of ReachIntegrationsApi->list_ecommerce_stores_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachIntegrationsApi->list_ecommerce_stores_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 

### Return type

[**List[ReachV1StoresStoreResource]**](ReachV1StoresStoreResource.md)

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

