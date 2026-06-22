# HostingV1DomainsDomainAccessResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name | [optional] 
**is_accessible** | **bool** | Whether domain is accessible | [optional] 
**txt_to_verify** | **str** | TXT record for verification | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_domains_domain_access_resource import HostingV1DomainsDomainAccessResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1DomainsDomainAccessResource from a JSON string
hosting_v1_domains_domain_access_resource_instance = HostingV1DomainsDomainAccessResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1DomainsDomainAccessResource.to_json())

# convert the object into a dict
hosting_v1_domains_domain_access_resource_dict = hosting_v1_domains_domain_access_resource_instance.to_dict()
# create an instance of HostingV1DomainsDomainAccessResource from a dict
hosting_v1_domains_domain_access_resource_from_dict = HostingV1DomainsDomainAccessResource.from_dict(hosting_v1_domains_domain_access_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


