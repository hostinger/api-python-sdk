# HostingV1DomainsSubdomainResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Website username | [optional] 
**domain** | **str** | Full subdomain | [optional] 
**parent_domain** | **str** | Parent website domain | [optional] 
**root_directory** | **str** | Subdomain root directory | [optional] 
**subdomain** | **str** | Subdomain prefix | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_domains_subdomain_resource import HostingV1DomainsSubdomainResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1DomainsSubdomainResource from a JSON string
hosting_v1_domains_subdomain_resource_instance = HostingV1DomainsSubdomainResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1DomainsSubdomainResource.to_json())

# convert the object into a dict
hosting_v1_domains_subdomain_resource_dict = hosting_v1_domains_subdomain_resource_instance.to_dict()
# create an instance of HostingV1DomainsSubdomainResource from a dict
hosting_v1_domains_subdomain_resource_from_dict = HostingV1DomainsSubdomainResource.from_dict(hosting_v1_domains_subdomain_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


