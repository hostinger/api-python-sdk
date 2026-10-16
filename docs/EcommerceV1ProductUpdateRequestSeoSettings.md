# EcommerceV1ProductUpdateRequestSeoSettings

Search-engine settings to change. Send at least one field; omitted fields keep their current values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Search-engine title for the product page. | [optional] 
**description** | **str** | Search-engine description for the product page. | [optional] 
**slug** | **str** | URL slug of the product page. Lowercase letters, digits and dashes. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_product_update_request_seo_settings import EcommerceV1ProductUpdateRequestSeoSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ProductUpdateRequestSeoSettings from a JSON string
ecommerce_v1_product_update_request_seo_settings_instance = EcommerceV1ProductUpdateRequestSeoSettings.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ProductUpdateRequestSeoSettings.to_json())

# convert the object into a dict
ecommerce_v1_product_update_request_seo_settings_dict = ecommerce_v1_product_update_request_seo_settings_instance.to_dict()
# create an instance of EcommerceV1ProductUpdateRequestSeoSettings from a dict
ecommerce_v1_product_update_request_seo_settings_from_dict = EcommerceV1ProductUpdateRequestSeoSettings.from_dict(ecommerce_v1_product_update_request_seo_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


