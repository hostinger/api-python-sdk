# BillingV1CatalogCatalogItemPriceResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Price item ID | [optional] 
**name** | **str** | Price item name | [optional] 
**currency** | **str** | Currency code | [optional] 
**price** | **int** | Price in cents | [optional] 
**first_period_price** | **int** | First period price in cents | [optional] 
**period** | **int** | Period | [optional] 
**period_unit** | **str** | Period unit | [optional] 

## Example

```python
from hostinger-api.models.billing_v1_catalog_catalog_item_price_resource import BillingV1CatalogCatalogItemPriceResource

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1CatalogCatalogItemPriceResource from a JSON string
billing_v1_catalog_catalog_item_price_resource_instance = BillingV1CatalogCatalogItemPriceResource.from_json(json)
# print the JSON string representation of the object
print(BillingV1CatalogCatalogItemPriceResource.to_json())

# convert the object into a dict
billing_v1_catalog_catalog_item_price_resource_dict = billing_v1_catalog_catalog_item_price_resource_instance.to_dict()
# create an instance of BillingV1CatalogCatalogItemPriceResource from a dict
billing_v1_catalog_catalog_item_price_resource_from_dict = BillingV1CatalogCatalogItemPriceResource.from_dict(billing_v1_catalog_catalog_item_price_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


