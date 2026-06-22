# HostingV1DomainsParkedDomainResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Website username | [optional] 
**domain** | **str** | Parked domain name or IP address | [optional] 
**parent_domain** | **str** | Parent website domain | [optional] 
**root_directory** | **str** | Parked domain root directory | [optional] 
**type** | **str** | Whether the parked value is a domain name or an IP address (IPv4 or IPv6) | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_domains_parked_domain_resource import HostingV1DomainsParkedDomainResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1DomainsParkedDomainResource from a JSON string
hosting_v1_domains_parked_domain_resource_instance = HostingV1DomainsParkedDomainResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1DomainsParkedDomainResource.to_json())

# convert the object into a dict
hosting_v1_domains_parked_domain_resource_dict = hosting_v1_domains_parked_domain_resource_instance.to_dict()
# create an instance of HostingV1DomainsParkedDomainResource from a dict
hosting_v1_domains_parked_domain_resource_from_dict = HostingV1DomainsParkedDomainResource.from_dict(hosting_v1_domains_parked_domain_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


