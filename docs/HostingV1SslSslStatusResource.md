# HostingV1SslSslStatusResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Current certificate status | 
**provider** | **str** | Provider of the assigned certificate, or of the last recorded installation when none is assigned. &#x60;custom&#x60; means an uploaded certificate. Null when no certificate is assigned and no installation is recorded, which is also the case for free subdomains on the platform-managed certificate. | 
**is_lifetime** | **bool** | Whether the certificate comes from a lifetime provider managed by the platform, not an uploaded one. Follows &#x60;provider&#x60;: it reflects the last recorded installation when no certificate is assigned, and is false when &#x60;provider&#x60; is null. | 
**is_https_redirect_enabled** | **bool** | Whether HTTP requests to the website are redirected to HTTPS | 
**expires_at** | **datetime** | End of the assigned certificate validity period; null when no certificate details are available. | 
**last_error** | **str** | Last installation error, when it is one of the known displayable messages | 

## Example

```python
from hostinger_api.models.hosting_v1_ssl_ssl_status_resource import HostingV1SslSslStatusResource

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1SslSslStatusResource from a JSON string
hosting_v1_ssl_ssl_status_resource_instance = HostingV1SslSslStatusResource.from_json(json)
# print the JSON string representation of the object
print(HostingV1SslSslStatusResource.to_json())

# convert the object into a dict
hosting_v1_ssl_ssl_status_resource_dict = hosting_v1_ssl_ssl_status_resource_instance.to_dict()
# create an instance of HostingV1SslSslStatusResource from a dict
hosting_v1_ssl_ssl_status_resource_from_dict = HostingV1SslSslStatusResource.from_dict(hosting_v1_ssl_ssl_status_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


