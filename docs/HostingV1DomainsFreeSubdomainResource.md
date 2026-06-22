# HostingV1DomainsFreeSubdomainResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Generated free subdomain | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_domains_free_subdomain_resource import HostingV1DomainsFreeSubdomainResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1DomainsFreeSubdomainResource from a JSON string
hosting_v1_domains_free_subdomain_resource_instance = HostingV1DomainsFreeSubdomainResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1DomainsFreeSubdomainResource.to_json())

# convert the object into a dict
hosting_v1_domains_free_subdomain_resource_dict = hosting_v1_domains_free_subdomain_resource_instance.to_dict()
# create an instance of HostingV1DomainsFreeSubdomainResource from a dict
hosting_v1_domains_free_subdomain_resource_from_dict = HostingV1DomainsFreeSubdomainResource.from_dict(hosting_v1_domains_free_subdomain_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


