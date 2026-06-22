# EcommerceV1ProductProductCreationResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**EcommerceV1ProductProductCreationResourceProduct**](EcommerceV1ProductProductCreationResourceProduct.md) |  | [optional] 
**admin_url** | **str** | Admin UI deep-link to manage the product. | [optional] 

## Example

```python
from hostinger_api.models.ecommerce_v1_product_product_creation_resource import EcommerceV1ProductProductCreationResource

# TODO update the JSON string below
json = "{}"
# create an instance of EcommerceV1ProductProductCreationResource from a JSON string
ecommerce_v1_product_product_creation_resource_instance = EcommerceV1ProductProductCreationResource.from_json(json)
# print the JSON string representation of the object
print(EcommerceV1ProductProductCreationResource.to_json())

# convert the object into a dict
ecommerce_v1_product_product_creation_resource_dict = ecommerce_v1_product_product_creation_resource_instance.to_dict()
# create an instance of EcommerceV1ProductProductCreationResource from a dict
ecommerce_v1_product_product_creation_resource_from_dict = EcommerceV1ProductProductCreationResource.from_dict(ecommerce_v1_product_product_creation_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


