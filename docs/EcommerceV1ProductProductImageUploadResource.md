# EcommerceV1ProductProductImageUploadResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | CDN URL of the uploaded image. | [optional] 
**is_thumbnail** | **bool** | Whether the image was set as the product&#39;s thumbnail (primary image). | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_product_product_image_upload_resource import EcommerceV1ProductProductImageUploadResource

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ProductProductImageUploadResource from a JSON string
ecommerce_v1_product_product_image_upload_resource_instance = EcommerceV1ProductProductImageUploadResource.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ProductProductImageUploadResource.to_json())

# convert the object into a dict
ecommerce_v1_product_product_image_upload_resource_dict = ecommerce_v1_product_product_image_upload_resource_instance.to_dict()
# create an instance of EcommerceV1ProductProductImageUploadResource from a dict
ecommerce_v1_product_product_image_upload_resource_from_dict = EcommerceV1ProductProductImageUploadResource.from_dict(ecommerce_v1_product_product_image_upload_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


