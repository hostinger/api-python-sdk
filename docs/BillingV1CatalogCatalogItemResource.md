# BillingV1CatalogCatalogItemResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Catalog item ID | [optional] 
**name** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**prices** | [**List[BillingV1CatalogCatalogItemPriceResource]**](BillingV1CatalogCatalogItemPriceResource.md) | Array of [&#x60;Billing.V1.Catalog.CatalogItemPriceResource&#x60;](#model/billingv1catalogcatalogitempriceresource) | [optional] 

## Example

```python
from hostinger-api.models.billing_v1_catalog_catalog_item_resource import BillingV1CatalogCatalogItemResource

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1CatalogCatalogItemResource from a JSON string
billing_v1_catalog_catalog_item_resource_instance = BillingV1CatalogCatalogItemResource.from_json(json)
# print the JSON string representation of the object
print(BillingV1CatalogCatalogItemResource.to_json())

# convert the object into a dict
billing_v1_catalog_catalog_item_resource_dict = billing_v1_catalog_catalog_item_resource_instance.to_dict()
# create an instance of BillingV1CatalogCatalogItemResource from a dict
billing_v1_catalog_catalog_item_resource_from_dict = BillingV1CatalogCatalogItemResource.from_dict(billing_v1_catalog_catalog_item_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


