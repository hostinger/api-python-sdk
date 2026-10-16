# EcommerceV1ProductCreatePhysicalProductRequestSeoSettings

Search-engine settings. Omitted fields are generated from the name and description; a slug already in use gets a numeric suffix. Send at least one field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Search-engine title for the product page. | [optional] 
**description** | **str** | Search-engine description for the product page. | [optional] 
**slug** | **str** | URL slug of the product page. Lowercase letters, digits and dashes. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_product_create_physical_product_request_seo_settings import EcommerceV1ProductCreatePhysicalProductRequestSeoSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ProductCreatePhysicalProductRequestSeoSettings from a JSON string
ecommerce_v1_product_create_physical_product_request_seo_settings_instance = EcommerceV1ProductCreatePhysicalProductRequestSeoSettings.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ProductCreatePhysicalProductRequestSeoSettings.to_json())

# convert the object into a dict
ecommerce_v1_product_create_physical_product_request_seo_settings_dict = ecommerce_v1_product_create_physical_product_request_seo_settings_instance.to_dict()
# create an instance of EcommerceV1ProductCreatePhysicalProductRequestSeoSettings from a dict
ecommerce_v1_product_create_physical_product_request_seo_settings_from_dict = EcommerceV1ProductCreatePhysicalProductRequestSeoSettings.from_dict(ecommerce_v1_product_create_physical_product_request_seo_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


