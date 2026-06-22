# HostingV1DomainsCreateSubdomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subdomain** | **str** | Subdomain prefix to create under the selected website | 
**directory** | **str** | Directory name for the subdomain relative to the website root | [optional] 
**is_using_public_directory** | **bool** | Use the website public directory as the subdomain root directory | [optional] 

## Example

```python
from hostinger_api.models.hosting_v1_domains_create_subdomain_request import HostingV1DomainsCreateSubdomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1DomainsCreateSubdomainRequest from a JSON string
hosting_v1_domains_create_subdomain_request_instance = HostingV1DomainsCreateSubdomainRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1DomainsCreateSubdomainRequest.to_json())

# convert the object into a dict
hosting_v1_domains_create_subdomain_request_dict = hosting_v1_domains_create_subdomain_request_instance.to_dict()
# create an instance of HostingV1DomainsCreateSubdomainRequest from a dict
hosting_v1_domains_create_subdomain_request_from_dict = HostingV1DomainsCreateSubdomainRequest.from_dict(hosting_v1_domains_create_subdomain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


