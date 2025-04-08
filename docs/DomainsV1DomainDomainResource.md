# DomainsV1DomainDomainResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Domain ID | [optional] 
**name** | **str** | Domain name, &#x60;null&#x60; when not claimed free domain | [optional] 
**type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger-api.models.domains_v1_domain_domain_resource import DomainsV1DomainDomainResource

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1DomainDomainResource from a JSON string
domains_v1_domain_domain_resource_instance = DomainsV1DomainDomainResource.from_json(json)
# print the JSON string representation of the object
print(DomainsV1DomainDomainResource.to_json())

# convert the object into a dict
domains_v1_domain_domain_resource_dict = domains_v1_domain_domain_resource_instance.to_dict()
# create an instance of DomainsV1DomainDomainResource from a dict
domains_v1_domain_domain_resource_from_dict = DomainsV1DomainDomainResource.from_dict(domains_v1_domain_domain_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


