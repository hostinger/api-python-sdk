# hostinger_api.EcommercePaymentsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_payment_provider_connect_link_v1**](EcommercePaymentsApi.md#create_a_payment_provider_connect_link_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/payment-providers/{provider_id}/connect-link | Create a payment provider connect link
[**enable_manual_payment_method_v1**](EcommercePaymentsApi.md#enable_manual_payment_method_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/payment-methods/manual | Enable manual payment method
[**list_store_payment_providers_v1**](EcommercePaymentsApi.md#list_store_payment_providers_v1) | **GET** /api/ecommerce/v1/stores/{store_id}/payment-providers | List store payment providers


# **create_a_payment_provider_connect_link_v1**
> EcommerceV1PaymentProviderPaymentProviderConnectLinkResource create_a_payment_provider_connect_link_v1(store_id, provider_id)

Create a payment provider connect link

Create an onboarding link for connecting a payment gateway to the store. Returns the gateway
onboarding URL for the merchant to open and a deep-link into the store admin.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_payment_provider_payment_provider_connect_link_resource import EcommerceV1PaymentProviderPaymentProviderConnectLinkResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommercePaymentsApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store to connect the payment provider to.
    provider_id = 'stripe' # str | The ID of the payment gateway to connect, e.g. stripe.

    try:
        # Create a payment provider connect link
        api_response = api_instance.create_a_payment_provider_connect_link_v1(store_id, provider_id)
        print("The response of EcommercePaymentsApi->create_a_payment_provider_connect_link_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommercePaymentsApi->create_a_payment_provider_connect_link_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store to connect the payment provider to. | 
 **provider_id** | **str**| The ID of the payment gateway to connect, e.g. stripe. | 

### Return type

[**EcommerceV1PaymentProviderPaymentProviderConnectLinkResource**](EcommerceV1PaymentProviderPaymentProviderConnectLinkResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created response |  -  |
**401** | Unauthenticated response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_manual_payment_method_v1**
> EcommerceV1PaymentManualPaymentResource enable_manual_payment_method_v1(store_id, ecommerce_v1_payment_enable_manual_payment_request)

Enable manual payment method

Enable a manual payment method so the store can accept orders without an online payment provider.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_payment_enable_manual_payment_request import EcommerceV1PaymentEnableManualPaymentRequest
from hostinger_api.models.ecommerce_v1_payment_manual_payment_resource import EcommerceV1PaymentManualPaymentResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommercePaymentsApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store to enable manual payment for.
    ecommerce_v1_payment_enable_manual_payment_request = hostinger_api.EcommerceV1PaymentEnableManualPaymentRequest() # EcommerceV1PaymentEnableManualPaymentRequest | 

    try:
        # Enable manual payment method
        api_response = api_instance.enable_manual_payment_method_v1(store_id, ecommerce_v1_payment_enable_manual_payment_request)
        print("The response of EcommercePaymentsApi->enable_manual_payment_method_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommercePaymentsApi->enable_manual_payment_method_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store to enable manual payment for. | 
 **ecommerce_v1_payment_enable_manual_payment_request** | [**EcommerceV1PaymentEnableManualPaymentRequest**](EcommerceV1PaymentEnableManualPaymentRequest.md)|  | 

### Return type

[**EcommerceV1PaymentManualPaymentResource**](EcommerceV1PaymentManualPaymentResource.md)

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
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_store_payment_providers_v1**
> EcommerceV1PaymentProviderPaymentProviderListResource list_store_payment_providers_v1(store_id, include_currency_unsupported=include_currency_unsupported)

List store payment providers

List a store's payment providers, split into providers already connected to the store and
gateways available to install. Never exposes gateway credentials, secrets, or configuration.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.ecommerce_v1_payment_provider_payment_provider_list_resource import EcommerceV1PaymentProviderPaymentProviderListResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.EcommercePaymentsApi(api_client)
    store_id = 'store_01J8Z5F8W9K8M4A7B3C2D1E0FG' # str | The ID of the store to list payment providers for.
    include_currency_unsupported = true # bool | Include gateways that do not support the store currency in the available list. (optional)

    try:
        # List store payment providers
        api_response = api_instance.list_store_payment_providers_v1(store_id, include_currency_unsupported=include_currency_unsupported)
        print("The response of EcommercePaymentsApi->list_store_payment_providers_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EcommercePaymentsApi->list_store_payment_providers_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| The ID of the store to list payment providers for. | 
 **include_currency_unsupported** | **bool**| Include gateways that do not support the store currency in the available list. | [optional] 

### Return type

[**EcommerceV1PaymentProviderPaymentProviderListResource**](EcommerceV1PaymentProviderPaymentProviderListResource.md)

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

