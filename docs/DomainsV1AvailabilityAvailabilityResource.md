# DomainsV1AvailabilityAvailabilityResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name, &#x60;null&#x60; when not claimed free domain | [optional] 
**is_available** | **bool** |  | [optional] 
**is_alternative** | **bool** |  | [optional] 
**restriction** | **str** |  | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_availability_availability_resource import DomainsV1AvailabilityAvailabilityResource

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1AvailabilityAvailabilityResource from a JSON string
domains_v1_availability_availability_resource_instance = DomainsV1AvailabilityAvailabilityResource.from_json(json)
# print the JSON string representation of the object
print(DomainsV1AvailabilityAvailabilityResource.to_json())

# convert the object into a dict
domains_v1_availability_availability_resource_dict = domains_v1_availability_availability_resource_instance.to_dict()
# create an instance of DomainsV1AvailabilityAvailabilityResource from a dict
domains_v1_availability_availability_resource_from_dict = DomainsV1AvailabilityAvailabilityResource.from_dict(domains_v1_availability_availability_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


