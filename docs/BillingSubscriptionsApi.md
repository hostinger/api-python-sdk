# hostinger_api.BillingSubscriptionsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_subscription_v1**](BillingSubscriptionsApi.md#cancel_subscription_v1) | **DELETE** /api/billing/v1/subscriptions/{subscriptionId} | Cancel subscription
[**get_subscription_list_v1**](BillingSubscriptionsApi.md#get_subscription_list_v1) | **GET** /api/billing/v1/subscriptions | Get subscription list


# **cancel_subscription_v1**
> CommonSuccessEmptyResource cancel_subscription_v1(subscription_id, billing_v1_subscription_cancel_request)

Cancel subscription

This endpoint cancels a subscription and stops any further billing.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.billing_v1_subscription_cancel_request import BillingV1SubscriptionCancelRequest
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
    api_instance = hostinger_api.BillingSubscriptionsApi(api_client)
    subscription_id = 'Cxy353Uhl1xC54pG6' # str | Subscription ID
    billing_v1_subscription_cancel_request = hostinger_api.BillingV1SubscriptionCancelRequest() # BillingV1SubscriptionCancelRequest | 

    try:
        # Cancel subscription
        api_response = api_instance.cancel_subscription_v1(subscription_id, billing_v1_subscription_cancel_request)
        print("The response of BillingSubscriptionsApi->cancel_subscription_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingSubscriptionsApi->cancel_subscription_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription ID | 
 **billing_v1_subscription_cancel_request** | [**BillingV1SubscriptionCancelRequest**](BillingV1SubscriptionCancelRequest.md)|  | 

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
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_list_v1**
> List[BillingV1SubscriptionSubscriptionResource] get_subscription_list_v1()

Get subscription list

This endpoint retrieves a list of all subscriptions associated with your account.

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
**401** | Unauthenticated |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

