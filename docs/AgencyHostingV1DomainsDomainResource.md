# AgencyHostingV1DomainsDomainResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | Domain name | [optional] 
**website_uid** | **str** | Owner website UID | [optional] 
**created_at** | **datetime** | Creation date | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_domains_domain_resource import AgencyHostingV1DomainsDomainResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1DomainsDomainResource from a JSON string
agency_hosting_v1_domains_domain_resource_instance = AgencyHostingV1DomainsDomainResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1DomainsDomainResource.to_json())

# convert the object into a dict
agency_hosting_v1_domains_domain_resource_dict = agency_hosting_v1_domains_domain_resource_instance.to_dict()
# create an instance of AgencyHostingV1DomainsDomainResource from a dict
agency_hosting_v1_domains_domain_resource_from_dict = AgencyHostingV1DomainsDomainResource.from_dict(agency_hosting_v1_domains_domain_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


