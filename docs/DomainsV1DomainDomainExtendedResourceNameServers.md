# DomainsV1DomainDomainExtendedResourceNameServers

Name servers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ns1** | **str** | Name server 1 | [optional] 
**ns2** | **str** | Name server 2 | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_domain_domain_extended_resource_name_servers import DomainsV1DomainDomainExtendedResourceNameServers

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1DomainDomainExtendedResourceNameServers from a JSON string
domains_v1_domain_domain_extended_resource_name_servers_instance = DomainsV1DomainDomainExtendedResourceNameServers.from_json(json)
# print the JSON string representation of the object
print(DomainsV1DomainDomainExtendedResourceNameServers.to_json())

# convert the object into a dict
domains_v1_domain_domain_extended_resource_name_servers_dict = domains_v1_domain_domain_extended_resource_name_servers_instance.to_dict()
# create an instance of DomainsV1DomainDomainExtendedResourceNameServers from a dict
domains_v1_domain_domain_extended_resource_name_servers_from_dict = DomainsV1DomainDomainExtendedResourceNameServers.from_dict(domains_v1_domain_domain_extended_resource_name_servers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


