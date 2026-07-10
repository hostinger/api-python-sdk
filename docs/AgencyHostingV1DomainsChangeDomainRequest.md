# AgencyHostingV1DomainsChangeDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | New domain to assign to the website. Set to null to revert to the temporary domain. | 

## Example

```python
from hostinger_api.models.agency_hosting_v1_domains_change_domain_request import AgencyHostingV1DomainsChangeDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1DomainsChangeDomainRequest from a JSON string
agency_hosting_v1_domains_change_domain_request_instance = AgencyHostingV1DomainsChangeDomainRequest.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1DomainsChangeDomainRequest.to_json())

# convert the object into a dict
agency_hosting_v1_domains_change_domain_request_dict = agency_hosting_v1_domains_change_domain_request_instance.to_dict()
# create an instance of AgencyHostingV1DomainsChangeDomainRequest from a dict
agency_hosting_v1_domains_change_domain_request_from_dict = AgencyHostingV1DomainsChangeDomainRequest.from_dict(agency_hosting_v1_domains_change_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


