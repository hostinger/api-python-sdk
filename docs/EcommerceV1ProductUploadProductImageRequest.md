# EcommerceV1ProductUploadProductImageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** | Publicly reachable URL of the raster image (JPEG, PNG, GIF or WebP), maximum 15MB. The image is fetched, virus-scanned and validated by content, then stored on the CDN. SVG is not accepted. Provide either this or object_name. | [optional] 
**object_name** | **str** | Key returned by the upload-url endpoint. Provide this instead of image_url to attach an uploaded image. | [optional] 
**is_thumbnail** | **bool** | When true, the image becomes the product&#39;s thumbnail (primary image). When omitted, it becomes the thumbnail only if the product does not have one yet. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_product_upload_product_image_request import EcommerceV1ProductUploadProductImageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ProductUploadProductImageRequest from a JSON string
ecommerce_v1_product_upload_product_image_request_instance = EcommerceV1ProductUploadProductImageRequest.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ProductUploadProductImageRequest.to_json())

# convert the object into a dict
ecommerce_v1_product_upload_product_image_request_dict = ecommerce_v1_product_upload_product_image_request_instance.to_dict()
# create an instance of EcommerceV1ProductUploadProductImageRequest from a dict
ecommerce_v1_product_upload_product_image_request_from_dict = EcommerceV1ProductUploadProductImageRequest.from_dict(ecommerce_v1_product_upload_product_image_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


