# ReachV1StoresStoreResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**store_id** | **str** | Pass this to the disconnect eCommerce store endpoint. | [optional] 
**business_name** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**sales_channels** | [**List[ReachV1StoresStoreResourceSalesChannelsInner]**](ReachV1StoresStoreResourceSalesChannelsInner.md) | Storefronts of the store. | [optional] 
**connection_status** | **str** | &#x60;connected&#x60; to the profile in the path, &#x60;connected_to_other_profile&#x60; when another profile of the account holds it, or &#x60;not_connected&#x60;. | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_stores_store_resource import ReachV1StoresStoreResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1StoresStoreResource from a JSON string
reach_v1_stores_store_resource_instance = ReachV1StoresStoreResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1StoresStoreResource.to_json())

# convert the object into a dict
reach_v1_stores_store_resource_dict = reach_v1_stores_store_resource_instance.to_dict()
# create an instance of ReachV1StoresStoreResource from a dict
reach_v1_stores_store_resource_from_dict = ReachV1StoresStoreResource.from_dict(reach_v1_stores_store_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


