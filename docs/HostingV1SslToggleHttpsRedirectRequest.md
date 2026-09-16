# HostingV1SslToggleHttpsRedirectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Turn the HTTP to HTTPS redirect on (true) or off (false) for the website. | 

## Example

```python
from hostinger_api.models.hosting_v1_ssl_toggle_https_redirect_request import HostingV1SslToggleHttpsRedirectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HostingV1SslToggleHttpsRedirectRequest from a JSON string
hosting_v1_ssl_toggle_https_redirect_request_instance = HostingV1SslToggleHttpsRedirectRequest.from_json(json)
# print the JSON string representation of the object
print(HostingV1SslToggleHttpsRedirectRequest.to_json())

# convert the object into a dict
hosting_v1_ssl_toggle_https_redirect_request_dict = hosting_v1_ssl_toggle_https_redirect_request_instance.to_dict()
# create an instance of HostingV1SslToggleHttpsRedirectRequest from a dict
hosting_v1_ssl_toggle_https_redirect_request_from_dict = HostingV1SslToggleHttpsRedirectRequest.from_dict(hosting_v1_ssl_toggle_https_redirect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


