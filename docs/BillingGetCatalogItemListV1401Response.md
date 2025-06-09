# BillingGetCatalogItemListV1401Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message of the error | [optional] 
**correlation_id** | **str** | Request correlation ID | [optional] 

## Example

```python
from hostinger_api.models.billing_get_catalog_item_list_v1401_response import BillingGetCatalogItemListV1401Response

# TODO update the JSON string below
json = "{}"
# create an instance of BillingGetCatalogItemListV1401Response from a JSON string
billing_get_catalog_item_list_v1401_response_instance = BillingGetCatalogItemListV1401Response.from_json(json)
# print the JSON string representation of the object
print(BillingGetCatalogItemListV1401Response.to_json())

# convert the object into a dict
billing_get_catalog_item_list_v1401_response_dict = billing_get_catalog_item_list_v1401_response_instance.to_dict()
# create an instance of BillingGetCatalogItemListV1401Response from a dict
billing_get_catalog_item_list_v1401_response_from_dict = BillingGetCatalogItemListV1401Response.from_dict(billing_get_catalog_item_list_v1401_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


