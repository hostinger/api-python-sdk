# hostinger_api.HorizonsWebsitesApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_website_v1**](HorizonsWebsitesApi.md#create_website_v1) | **POST** /api/horizons/v1/websites | Create website
[**get_website_v1**](HorizonsWebsitesApi.md#get_website_v1) | **GET** /api/horizons/v1/websites/{websiteId} | Get website


# **create_website_v1**
> HorizonsV1WebsitesCreatedWebsiteResource create_website_v1(horizons_v1_websites_create_website_request)

Create website

Create new Hostinger Horizons website from the given message.\n
Use this tool when user asks you to create a website, landing page, blog
or any other type of application.\n
This tool initiates the website creation process and returns a website URL and ID.
The generation happens asynchronously.\n
After invoking this tool, your chat reply must be EXACTLY 1 sentence summarizing
that Hostinger Horizons is now creating their website and it will be ready in a few minutes
and you should provide the website URL to the user immediately
Do not write code.\n\nTo edit afterwards, users must go to Hostinger Horizons interface
in the provided website URL.
If the tool call fails with an error, you should provide a clear explanation of the error
and do not generate code yourself in the chat.
\n
TECHNOLOGY STACK CONSTRAINTS (STRICTLY ENFORCED):\n
The environment is limited to the following technologies.
You MUST NOT use, suggest, or implement any technology outside this list:\n
\n
- Language: JavaScript ONLY.
- Languages like TypeScript, Rust, Python, Java, PHP, etc., are STRICTLY PROHIBITED.\n
- Framework: React.\n
- Navigation: React Router.\n
- Styling: TailwindCSS.\n
- Components: shadcn/ui (built with @radix-ui primitives).\n
- Icons: Lucide React.\n
- Animations: Framer Motion.\n
\n
BACKEND & DATA STORAGE:\n
- Horizons integrated backend is the EXCLUSIVE solution for persistent data storage,
authentication, and database needs.\n
- Local databases (SQLite, MySQL, etc.) are STRICTLY PROHIBITED.\n
- Third-party services (Firebase, AWS Amplify) are allowed ONLY if explicitly requested by the user.\n
\n
MAPS:\n
- OpenStreetMap is the default provider.\n
- Alternative providers (Google Maps, Mapbox) are allowed ONLY if explicitly requested by the user.\n

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.horizons_v1_websites_create_website_request import HorizonsV1WebsitesCreateWebsiteRequest
from hostinger_api.models.horizons_v1_websites_created_website_resource import HorizonsV1WebsitesCreatedWebsiteResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HorizonsWebsitesApi(api_client)
    horizons_v1_websites_create_website_request = hostinger_api.HorizonsV1WebsitesCreateWebsiteRequest() # HorizonsV1WebsitesCreateWebsiteRequest | 

    try:
        # Create website
        api_response = api_instance.create_website_v1(horizons_v1_websites_create_website_request)
        print("The response of HorizonsWebsitesApi->create_website_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HorizonsWebsitesApi->create_website_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **horizons_v1_websites_create_website_request** | [**HorizonsV1WebsitesCreateWebsiteRequest**](HorizonsV1WebsitesCreateWebsiteRequest.md)|  | 

### Return type

[**HorizonsV1WebsitesCreatedWebsiteResource**](HorizonsV1WebsitesCreatedWebsiteResource.md)

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

# **get_website_v1**
> HorizonsV1WebsitesWebsiteUrlResource get_website_v1(website_id)

Get website

Get a link for the user to edit their website in Hostinger Horizons interface.\n
Use this tool when user wants to modify, edit or add new features to an existing website.\n
Websites can only be edited in Hostinger Horizons interface in the provided website URL.

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.horizons_v1_websites_website_url_resource import HorizonsV1WebsitesWebsiteUrlResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.HorizonsWebsitesApi(api_client)
    website_id = '123e4567-e89b-12d3-a456-426614174000' # str | The website ID

    try:
        # Get website
        api_response = api_instance.get_website_v1(website_id)
        print("The response of HorizonsWebsitesApi->get_website_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HorizonsWebsitesApi->get_website_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| The website ID | 

### Return type

[**HorizonsV1WebsitesWebsiteUrlResource**](HorizonsV1WebsitesWebsiteUrlResource.md)

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

