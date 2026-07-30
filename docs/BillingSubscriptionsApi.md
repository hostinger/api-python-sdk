# hostinger_api.BillingSubscriptionsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_auto_renewal_v1**](BillingSubscriptionsApi.md#disable_auto_renewal_v1) | **DELETE** /api/billing/v1/subscriptions/{subscriptionId}/auto-renewal/disable | Disable auto-renewal
[**enable_auto_renewal_v1**](BillingSubscriptionsApi.md#enable_auto_renewal_v1) | **PATCH** /api/billing/v1/subscriptions/{subscriptionId}/auto-renewal/enable | Enable auto-renewal
[**get_subscription_list_v1**](BillingSubscriptionsApi.md#get_subscription_list_v1) | **GET** /api/billing/v1/subscriptions | Get subscription list
[**renew_subscription_v1**](BillingSubscriptionsApi.md#renew_subscription_v1) | **POST** /api/billing/v1/subscriptions/{subscriptionId}/renew | Renew subscription


# **disable_auto_renewal_v1**
> BillingV1SubscriptionSubscriptionResource disable_auto_renewal_v1(subscription_id)

Disable auto-renewal

Disable auto-renewal for a subscription.

Use this endpoint when disable auto-renewal for a subscription.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.billing_v1_subscription_subscription_resource import BillingV1SubscriptionSubscriptionResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.BillingSubscriptionsApi(api_client)
    subscription_id = 'Cxy353Uhl1xC54pG6' # str | Subscription ID

    try:
        # Disable auto-renewal
        api_response = api_instance.disable_auto_renewal_v1(subscription_id)
        print("The response of BillingSubscriptionsApi->disable_auto_renewal_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingSubscriptionsApi->disable_auto_renewal_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription ID | 

### Return type

[**BillingV1SubscriptionSubscriptionResource**](BillingV1SubscriptionSubscriptionResource.md)

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

# **enable_auto_renewal_v1**
> BillingV1SubscriptionSubscriptionResource enable_auto_renewal_v1(subscription_id)

Enable auto-renewal

Enable auto-renewal for a subscription.

Use this endpoint when enable auto-renewal for a subscription.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.billing_v1_subscription_subscription_resource import BillingV1SubscriptionSubscriptionResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.BillingSubscriptionsApi(api_client)
    subscription_id = 'Cxy353Uhl1xC54pG6' # str | Subscription ID

    try:
        # Enable auto-renewal
        api_response = api_instance.enable_auto_renewal_v1(subscription_id)
        print("The response of BillingSubscriptionsApi->enable_auto_renewal_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingSubscriptionsApi->enable_auto_renewal_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription ID | 

### Return type

[**BillingV1SubscriptionSubscriptionResource**](BillingV1SubscriptionSubscriptionResource.md)

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

# **get_subscription_list_v1**
> List[BillingV1SubscriptionSubscriptionResource] get_subscription_list_v1()

Get subscription list

Retrieve a list of all subscriptions associated with your account.

Use this endpoint to monitor active services and billing status.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.billing_v1_subscription_subscription_resource import BillingV1SubscriptionSubscriptionResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.BillingSubscriptionsApi(api_client)

    try:
        # Get subscription list
        api_response = api_instance.get_subscription_list_v1()
        print("The response of BillingSubscriptionsApi->get_subscription_list_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingSubscriptionsApi->get_subscription_list_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BillingV1SubscriptionSubscriptionResource]**](BillingV1SubscriptionSubscriptionResource.md)

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

# **renew_subscription_v1**
> BillingV1OrderOrderResource renew_subscription_v1(subscription_id, billing_v1_subscription_renewal_renew_request=billing_v1_subscription_renewal_renew_request)

Renew subscription

Create a renewal order for an existing Hostinger subscription.

This endpoint places a renewal order for a single subscription, leveraging
the existing billing infrastructure. Use the
[subscriptions endpoint](#tag/billing-subscriptions) to look up the
`subscriptionId` values available for renewal.

If no payment method is provided, your default payment method will be used automatically.

Use this endpoint to renew any subscription available in your account.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.billing_v1_order_order_resource import BillingV1OrderOrderResource
from hostinger_api.models.billing_v1_subscription_renewal_renew_request import BillingV1SubscriptionRenewalRenewRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.BillingSubscriptionsApi(api_client)
    subscription_id = 'Cxy353Uhl1xC54pG6' # str | Subscription ID
    billing_v1_subscription_renewal_renew_request = hostinger_api.BillingV1SubscriptionRenewalRenewRequest() # BillingV1SubscriptionRenewalRenewRequest |  (optional)

    try:
        # Renew subscription
        api_response = api_instance.renew_subscription_v1(subscription_id, billing_v1_subscription_renewal_renew_request=billing_v1_subscription_renewal_renew_request)
        print("The response of BillingSubscriptionsApi->renew_subscription_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingSubscriptionsApi->renew_subscription_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription ID | 
 **billing_v1_subscription_renewal_renew_request** | [**BillingV1SubscriptionRenewalRenewRequest**](BillingV1SubscriptionRenewalRenewRequest.md)|  | [optional] 

### Return type

[**BillingV1OrderOrderResource**](BillingV1OrderOrderResource.md)

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

