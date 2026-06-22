# HostingV1DomainsCreateParkedDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parked_domain** | **str** | Domain name or IP address to park on the selected website | 

## Example

```python
from hostinger_api.models.hosting_v1_domains_create_parked_domain_request import HostingV1DomainsCreateParkedDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1DomainsCreateParkedDomainRequest from a JSON string
hosting_v1_domains_create_parked_domain_request_instance = HostingV1DomainsCreateParkedDomainRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1DomainsCreateParkedDomainRequest.to_json())

# convert the object into a dict
hosting_v1_domains_create_parked_domain_request_dict = hosting_v1_domains_create_parked_domain_request_instance.to_dict()
# create an instance of HostingV1DomainsCreateParkedDomainRequest from a dict
hosting_v1_domains_create_parked_domain_request_from_dict = HostingV1DomainsCreateParkedDomainRequest.from_dict(hosting_v1_domains_create_parked_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


