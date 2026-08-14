# EcommerceV1ProductProductImageUploadUrlResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_url** | **str** | Signed URL to upload the image to with a multipart/form-data POST. | [optional] 
**fields** | **Dict[str, str]** | Form fields to send alongside the file in the multipart POST. | [optional] 
**object_name** | **str** | Key of the uploaded object — send it to the attach-image endpoint. | [optional] 
**max_bytes** | **int** | Maximum accepted upload size in bytes. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_product_product_image_upload_url_resource import EcommerceV1ProductProductImageUploadUrlResource

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ProductProductImageUploadUrlResource from a JSON string
ecommerce_v1_product_product_image_upload_url_resource_instance = EcommerceV1ProductProductImageUploadUrlResource.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ProductProductImageUploadUrlResource.to_json())

# convert the object into a dict
ecommerce_v1_product_product_image_upload_url_resource_dict = ecommerce_v1_product_product_image_upload_url_resource_instance.to_dict()
# create an instance of EcommerceV1ProductProductImageUploadUrlResource from a dict
ecommerce_v1_product_product_image_upload_url_resource_from_dict = EcommerceV1ProductProductImageUploadUrlResource.from_dict(ecommerce_v1_product_product_image_upload_url_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


