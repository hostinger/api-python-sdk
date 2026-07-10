# AgencyHostingV1DomainsLinkDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Fully qualified domain name to link to the website | 

## Example

```python
from hostinger_api.models.agency_hosting_v1_domains_link_domain_request import AgencyHostingV1DomainsLinkDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1DomainsLinkDomainRequest from a JSON string
agency_hosting_v1_domains_link_domain_request_instance = AgencyHostingV1DomainsLinkDomainRequest.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1DomainsLinkDomainRequest.to_json())

# convert the object into a dict
agency_hosting_v1_domains_link_domain_request_dict = agency_hosting_v1_domains_link_domain_request_instance.to_dict()
# create an instance of AgencyHostingV1DomainsLinkDomainRequest from a dict
agency_hosting_v1_domains_link_domain_request_from_dict = AgencyHostingV1DomainsLinkDomainRequest.from_dict(agency_hosting_v1_domains_link_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


