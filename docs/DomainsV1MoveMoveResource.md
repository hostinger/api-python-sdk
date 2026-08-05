# DomainsV1MoveMoveResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name | [optional] 
**status** | **str** | Status of the move | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_move_move_resource import DomainsV1MoveMoveResource

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1MoveMoveResource from a JSON string
domains_v1_move_move_resource_instance = DomainsV1MoveMoveResource.from_json(json)
# print the JSON string representation of the object
print(DomainsV1MoveMoveResource.to_json())

# convert the object into a dict
domains_v1_move_move_resource_dict = domains_v1_move_move_resource_instance.to_dict()
# create an instance of DomainsV1MoveMoveResource from a dict
domains_v1_move_move_resource_from_dict = DomainsV1MoveMoveResource.from_dict(domains_v1_move_move_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


