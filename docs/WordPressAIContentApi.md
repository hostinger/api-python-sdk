# hostinger_api.WordPressAIContentApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_images_v1**](WordPressAIContentApi.md#generate_images_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/content/images/generate | Generate images
[**get_generation_result_v1**](WordPressAIContentApi.md#get_generation_result_v1) | **GET** /api/hosting/v1/accounts/{username}/wordpress/{software}/content/generations/{generation_id} | Get generation result


# **generate_images_v1**
> WordPressV1ContentGenerationResource generate_images_v1(username, software, word_press_v1_content_generate_images_request)

Generate images

Start generating one or more images from a prompt and an image type for the specified
WordPress installation. The generation runs asynchronously: the response is returned
right away with `status: in-progress` and a `generation_id`. Poll
GET /api/hosting/v1/accounts/{username}/wordpress/{software}/content/generations/{generation_id}
every few seconds until `status` is `completed` or `failed`.

A completed generation returns temporary image URLs together with the time they expire;
download the images before then. Images match the requested aspect ratio and are never
smaller than the requested size; logos are transparent images cropped to the mark.

Only one image generation can run per installation at a time: while one is still in
progress the endpoint returns 409 without the ID of the running generation, so a caller
that did not receive the `202` has to wait for it to finish (up to a few minutes) before
starting a new one. The endpoint is limited to 10 requests per minute.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_content_generate_images_request import WordPressV1ContentGenerateImagesRequest
from hostinger_api.models.word_press_v1_content_generation_resource import WordPressV1ContentGenerationResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressAIContentApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    word_press_v1_content_generate_images_request = hostinger_api.WordPressV1ContentGenerateImagesRequest() # WordPressV1ContentGenerateImagesRequest | 

    try:
        # Generate images
        api_response = api_instance.generate_images_v1(username, software, word_press_v1_content_generate_images_request)
        print("The response of WordPressAIContentApi->generate_images_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressAIContentApi->generate_images_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **word_press_v1_content_generate_images_request** | [**WordPressV1ContentGenerateImagesRequest**](WordPressV1ContentGenerateImagesRequest.md)|  | 

### Return type

[**WordPressV1ContentGenerationResource**](WordPressV1ContentGenerationResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**404** | Error response |  -  |
**409** | Conflict response. &#x60;Retry-After&#x60;, when present, is the number of seconds to wait before retrying. |  * Retry-After - Seconds to wait before retrying the request <br>  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_generation_result_v1**
> WordPressV1ContentGenerationResource get_generation_result_v1(username, software, generation_id, type=type)

Get generation result

Get the result of an AI content generation started for the specified WordPress
installation, such as an image generation started with
POST /api/hosting/v1/accounts/{username}/wordpress/{software}/content/images/generate.

While the generation is still running only `status: in-progress` is returned; poll every
few seconds. Once `completed`, `result` holds the generated content shaped according to
`type`: temporary image URLs together with the time they expire for `image-generation`, or
the generated website document for `website-generation` (started from the Hostinger
WordPress plugin). A `failed` generation has no `result`. Unknown or expired generation
IDs return 404.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_content_generation_resource import WordPressV1ContentGenerationResource
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.WordPressAIContentApi(api_client)
    username = 'u123456789' # str | 
    software = '1232456789' # str | WordPress installation (software) identifier
    generation_id = '9d4f8a1e-2b3c-4d5e-8f6a-7b8c9d0e1f2a' # str | Generation ID returned when the generation was started
    type = 'image-generation' # str | Generation type to look up. When omitted, every generation type is checked. (optional)

    try:
        # Get generation result
        api_response = api_instance.get_generation_result_v1(username, software, generation_id, type=type)
        print("The response of WordPressAIContentApi->get_generation_result_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordPressAIContentApi->get_generation_result_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **software** | **str**| WordPress installation (software) identifier | 
 **generation_id** | **str**| Generation ID returned when the generation was started | 
 **type** | **str**| Generation type to look up. When omitted, every generation type is checked. | [optional] 

### Return type

[**WordPressV1ContentGenerationResource**](WordPressV1ContentGenerationResource.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**422** | Validation error response |  -  |
**401** | Unauthenticated response |  -  |
**404** | Error response |  -  |
**500** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

