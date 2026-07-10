# hostinger_api.AgencyHostingWebsiteSetupsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agency_plan_website_setup_status_v1**](AgencyHostingWebsiteSetupsApi.md#get_agency_plan_website_setup_status_v1) | **GET** /api/agency-hosting/v1/orders/{order_id}/websites/setups/{setup_uuid} | Get Agency Plan website setup status
[**provision_a_new_agency_plan_website_v1**](AgencyHostingWebsiteSetupsApi.md#provision_a_new_agency_plan_website_v1) | **POST** /api/agency-hosting/v1/orders/{order_id}/websites/setups | Provision a new Agency Plan website


# **get_agency_plan_website_setup_status_v1**
> AgencyHostingV1SetupsWebsiteSetupStatusResource get_agency_plan_website_setup_status_v1(order_id, setup_uuid)

Get Agency Plan website setup status

Returns the current status of an Agency Plan website setup started via the setups
endpoint.

Poll this endpoint using the `setup_uuid` returned from the provisioning request until
`status` becomes `completed`, at which point `website_uid` identifies the new website.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_setups_website_setup_status_resource import AgencyHostingV1SetupsWebsiteSetupStatusResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingWebsiteSetupsApi(api_client)
    order_id = 123456 # int | Agency Plan order ID
    setup_uuid = '0193b6d4-fabb-70e0-8ea4-cfe060a45898' # str | Website setup UUID

    try:
        # Get Agency Plan website setup status
        api_response = api_instance.get_agency_plan_website_setup_status_v1(order_id, setup_uuid)
        print("The response of AgencyHostingWebsiteSetupsApi->get_agency_plan_website_setup_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingWebsiteSetupsApi->get_agency_plan_website_setup_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Agency Plan order ID | 
 **setup_uuid** | **str**| Website setup UUID | 

### Return type

[**AgencyHostingV1SetupsWebsiteSetupStatusResource**](AgencyHostingV1SetupsWebsiteSetupStatusResource.md)

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

# **provision_a_new_agency_plan_website_v1**
> AgencyHostingV1SetupsWebsiteSetupResource provision_a_new_agency_plan_website_v1(order_id, agency_hosting_v1_setups_create_setup_request)

Provision a new Agency Plan website

Provisions a new website on one of your Agency Plan hosting orders.

Choose the datacenter, stack (`flavor`), and PHP version for the site. Optionally attach
your own `domain` — omit it, set it to `null`, or leave it unavailable and a free
`*.hostingersite.com` subdomain is generated instead — and/or install WordPress by
supplying the `wordpress` details (admin account, site title, and language).

Common setups:
- **Plain PHP site**: `flavor` set to `php-fpm`, with `settings.php.version`; omit
  `wordpress` and `type`.
- **WordPress site**: `flavor` set to the desired WordPress version (e.g. `wp-7.0`), plus
  the `wordpress` block (admin account, title, language).
- **Static/Node.js frontend app**: `flavor` set to `php-fpm` and `type` set to
  `node-static`.

Provisioning runs in the background, so the response returns immediately with a setup UUID
that identifies the job. The new website becomes reachable once provisioning finishes.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.agency_hosting_v1_setups_create_setup_request import AgencyHostingV1SetupsCreateSetupRequest
from hostinger_api.models.agency_hosting_v1_setups_website_setup_resource import AgencyHostingV1SetupsWebsiteSetupResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.AgencyHostingWebsiteSetupsApi(api_client)
    order_id = 123456 # int | Agency Plan order ID
    agency_hosting_v1_setups_create_setup_request = hostinger_api.AgencyHostingV1SetupsCreateSetupRequest() # AgencyHostingV1SetupsCreateSetupRequest | 

    try:
        # Provision a new Agency Plan website
        api_response = api_instance.provision_a_new_agency_plan_website_v1(order_id, agency_hosting_v1_setups_create_setup_request)
        print("The response of AgencyHostingWebsiteSetupsApi->provision_a_new_agency_plan_website_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgencyHostingWebsiteSetupsApi->provision_a_new_agency_plan_website_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Agency Plan order ID | 
 **agency_hosting_v1_setups_create_setup_request** | [**AgencyHostingV1SetupsCreateSetupRequest**](AgencyHostingV1SetupsCreateSetupRequest.md)|  | 

### Return type

[**AgencyHostingV1SetupsWebsiteSetupResource**](AgencyHostingV1SetupsWebsiteSetupResource.md)

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

