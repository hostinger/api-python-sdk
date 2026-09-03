# hostinger_api.ReachCampaignsApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_draft_campaign_v1**](ReachCampaignsApi.md#create_a_draft_campaign_v1) | **POST** /api/reach/v1/profiles/{profileUuid}/campaigns | Create a draft campaign
[**get_campaign_details_v1**](ReachCampaignsApi.md#get_campaign_details_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/campaigns/{campaignUuid} | Get campaign details
[**get_campaign_performance_v1**](ReachCampaignsApi.md#get_campaign_performance_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/campaigns/{campaignUuid}/statistics | Get campaign performance
[**list_campaigns_v1**](ReachCampaignsApi.md#list_campaigns_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/campaigns | List campaigns


# **create_a_draft_campaign_v1**
> ReachV1CampaignsCreatedCampaignResource create_a_draft_campaign_v1(profile_uuid, reach_v1_campaigns_store_request)

Create a draft campaign

Create a campaign in a profile.

The campaign is created as a draft, so nothing is sent and no contact is touched. It has no
audience yet either - targeting and scheduling are not part of this request, the draft is
finished and sent from the Reach interface.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_campaigns_created_campaign_resource import ReachV1CampaignsCreatedCampaignResource
from hostinger_api.models.reach_v1_campaigns_store_request import ReachV1CampaignsStoreRequest
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachCampaignsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    reach_v1_campaigns_store_request = hostinger_api.ReachV1CampaignsStoreRequest() # ReachV1CampaignsStoreRequest | 

    try:
        # Create a draft campaign
        api_response = api_instance.create_a_draft_campaign_v1(profile_uuid, reach_v1_campaigns_store_request)
        print("The response of ReachCampaignsApi->create_a_draft_campaign_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachCampaignsApi->create_a_draft_campaign_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **reach_v1_campaigns_store_request** | [**ReachV1CampaignsStoreRequest**](ReachV1CampaignsStoreRequest.md)|  | 

### Return type

[**ReachV1CampaignsCreatedCampaignResource**](ReachV1CampaignsCreatedCampaignResource.md)

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

# **get_campaign_details_v1**
> ReachV1CampaignsCampaignDetailsResource get_campaign_details_v1(profile_uuid, campaign_uuid)

Get campaign details

Get a single campaign with its sender, subject, template reference, targeting and delivery
progress.

This describes how the campaign was set up and how far it has got. For opens, clicks and
unsubscribes use the campaign statistics endpoint.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_campaigns_campaign_details_resource import ReachV1CampaignsCampaignDetailsResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachCampaignsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    campaign_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Campaign uuid parameter

    try:
        # Get campaign details
        api_response = api_instance.get_campaign_details_v1(profile_uuid, campaign_uuid)
        print("The response of ReachCampaignsApi->get_campaign_details_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachCampaignsApi->get_campaign_details_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **campaign_uuid** | **str**| Campaign uuid parameter | 

### Return type

[**ReachV1CampaignsCampaignDetailsResource**](ReachV1CampaignsCampaignDetailsResource.md)

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

# **get_campaign_performance_v1**
> ReachV1CampaignsCampaignStatisticsResource get_campaign_performance_v1(profile_uuid, campaign_uuid)

Get campaign performance

Get the performance of a campaign: delivery, opens, clicks and unsubscribes, with the
matching rates.

Every count is unique contacts rather than raw events, so a contact who opens the same email
five times is counted once.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_v1_campaigns_campaign_statistics_resource import ReachV1CampaignsCampaignStatisticsResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachCampaignsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    campaign_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Campaign uuid parameter

    try:
        # Get campaign performance
        api_response = api_instance.get_campaign_performance_v1(profile_uuid, campaign_uuid)
        print("The response of ReachCampaignsApi->get_campaign_performance_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachCampaignsApi->get_campaign_performance_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **campaign_uuid** | **str**| Campaign uuid parameter | 

### Return type

[**ReachV1CampaignsCampaignStatisticsResource**](ReachV1CampaignsCampaignStatisticsResource.md)

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

# **list_campaigns_v1**
> ReachListCampaignsV1200Response list_campaigns_v1(profile_uuid, status=status, type=type, sort_direction=sort_direction, page=page, per_page=per_page)

List campaigns

Get a paginated list of the campaigns in a profile.

Each campaign carries its headline engagement rates. Filter by status to find drafts,
scheduled, sending or sent campaigns, keeping in mind that a fully sent campaign has the
status `publish`. By default only regular campaigns are returned - pass `type` to get the
emails sent by automations or the double opt-in confirmations instead.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.reach_list_campaigns_v1200_response import ReachListCampaignsV1200Response
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.ReachCampaignsApi(api_client)
    profile_uuid = '550e8400-e09b-41d4-a716-400055000000' # str | Profile uuid parameter
    status = 'publish' # str | Filter campaigns by status.  A fully sent campaign has the status `publish`. There is no `sent` status, and campaigns can be neither paused nor archived. (optional)
    type = campaign # str | Filter campaigns by type.  Defaults to `campaign`, which leaves out the emails sent by automations and the double opt-in confirmations. (optional) (default to campaign)
    sort_direction = 'desc' # str | Order campaigns by creation date. Newest first unless set to `asc`. (optional)
    page = 1 # int | Page number (optional)
    per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List campaigns
        api_response = api_instance.list_campaigns_v1(profile_uuid, status=status, type=type, sort_direction=sort_direction, page=page, per_page=per_page)
        print("The response of ReachCampaignsApi->list_campaigns_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReachCampaignsApi->list_campaigns_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_uuid** | **str**| Profile uuid parameter | 
 **status** | **str**| Filter campaigns by status.  A fully sent campaign has the status &#x60;publish&#x60;. There is no &#x60;sent&#x60; status, and campaigns can be neither paused nor archived. | [optional] 
 **type** | **str**| Filter campaigns by type.  Defaults to &#x60;campaign&#x60;, which leaves out the emails sent by automations and the double opt-in confirmations. | [optional] [default to campaign]
 **sort_direction** | **str**| Order campaigns by creation date. Newest first unless set to &#x60;asc&#x60;. | [optional] 
 **page** | **int**| Page number | [optional] 
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**ReachListCampaignsV1200Response**](ReachListCampaignsV1200Response.md)

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

