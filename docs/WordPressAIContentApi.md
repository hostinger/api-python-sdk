# hostinger_api.WordPressAIContentApi

All URIs are relative to *https://developers.hostinger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_images_v1**](WordPressAIContentApi.md#generate_images_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/content/images/generate | Generate images


# **generate_images_v1**
> WordPressV1ContentGeneratedImagesResource generate_images_v1(username, software, word_press_v1_content_generate_images_request)

Generate images

Generate one or more images from a prompt and an image type for the specified
WordPress installation. Images are returned inline as base64-encoded PNGs. They match
the requested aspect ratio and are never smaller than the requested size; logos are
transparent PNGs cropped to the mark.

Generation is synchronous and can take up to a minute. The endpoint is limited to
10 requests per minute.

Provide the WordPress installation (software) identifier in the path. It can
be obtained from GET /api/hosting/v1/wordpress/installations (the `id` field).

### Example

* Bearer Authentication (apiToken):

```python
import hostinger_api
from hostinger_api.models.word_press_v1_content_generate_images_request import WordPressV1ContentGenerateImagesRequest
from hostinger_api.models.word_press_v1_content_generated_images_resource import WordPressV1ContentGeneratedImagesResource
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

[**WordPressV1ContentGeneratedImagesResource**](WordPressV1ContentGeneratedImagesResource.md)

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

