# AgencyHostingV1SslSslStatusResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | &#x60;installing&#x60; while a certificate setup is running or retrying, &#x60;active&#x60; when a valid certificate is in place (uploaded, platform-issued, or a lifetime certificate bought for the domain), &#x60;failed&#x60; when the last setup gave up and no valid certificate is in place, &#x60;expired&#x60; when the certificate has run out, &#x60;not_installed&#x60; when the domain has no certificate and no setup process. | 
**is_custom** | **bool** | Whether the certificate was uploaded by the customer instead of issued or sold by the platform. | 
**expires_at** | **datetime** | End of the validity period of the certificate in place; null when there is none or the uploaded certificate carries no expiry. | 

## Example

```python
from hostinger_api.models.agency_hosting_v1_ssl_ssl_status_resource import AgencyHostingV1SslSslStatusResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1SslSslStatusResource from a JSON string
agency_hosting_v1_ssl_ssl_status_resource_instance = AgencyHostingV1SslSslStatusResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1SslSslStatusResource.to_json())

# convert the object into a dict
agency_hosting_v1_ssl_ssl_status_resource_dict = agency_hosting_v1_ssl_ssl_status_resource_instance.to_dict()
# create an instance of AgencyHostingV1SslSslStatusResource from a dict
agency_hosting_v1_ssl_ssl_status_resource_from_dict = AgencyHostingV1SslSslStatusResource.from_dict(agency_hosting_v1_ssl_ssl_status_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


