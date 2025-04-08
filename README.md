# PROJECKT_NAME
> [!caution]
> Currently, this API is in beta stage, meaning that breaking changes, while unlikely, might be introduced.
> If you encounter any issues or have any feedback, please create an issue on the [Github Repository](https://github.com/hostinger/api/issues).
# Overview
The Hostinger API provides a comprehensive set of endpoints that allow developers to interact with Hostinger's services programmatically. 
This API enables you to manage various aspects of your Hostinger account.

The Hostinger API is a (mostly) RESTful API that uses standard HTTP methods and status codes.
# Authentication
The Hostinger API uses tokens for authentication. To authenticate your requests, you need to include a valid bearer token in the Authorization header of your HTTP requests:
```yaml
Authorization: Bearer YOUR_API_TOKEN
```
API tokens for individual users can be created and managed from the [VPS page](https://hpanel.hostinger.com/vps) of the Hostinger Panel.
Tokens will have same permissions as the owning user. Optionally, tokens can be set to expire after a certain period of time.
# Rate Limiting
To ensure fair usage and prevent abuse, the API enforces rate limits on the number of requests that can be made within a certain time period. 
If you exceed the rate limit, you will receive a 429 Too Many Requests response. Rate limit headers are included in the response to help you manage your requests.
Your IP address might get temporarily blocked if you exceed the rate limit multiple times.
# Parameters
All requests sent to API must have the content type `application/json`. `POST`, `PUT`, `PATCH` methods may include a JSON object in the request body. Documentation provides required structure and examples of the object.
Some endpoints require path parameters. These parameters are included in the URL path and are marked with curly braces.
# Pagination
Some endpoints return a large number of items. To make these responses more manageable, the API uses pagination.
By default, the API returns 50 items per page. 
 
 The page number can be specified using the `page` query parameter, for example: `/api/vps/v1/public-keys?page=2`
# Errors
The Hostinger API uses standard HTTP status codes to indicate the success or failure of a request.
In case of an error, the API will return a JSON response with an `error` field, containing a human-readable error message.
Error responses also contain a `correlation_id` field which can be used to identify the request in case you need to contact support.
# Change log
For information on the latest changes to the API, please refer to the [change log](https://github.com/hostinger/api/blob/main/CHANGELOG.md).
# Support            
If you have any questions, feedback or feature requests, please create an [issue](https://github.com/hostinger/api/issues) or [discussion](https://github.com/hostinger/api/discussions) on the repository.

For any support take a look at our [Github Repository](https://github.com/hostinger/api/), dedicated to the Hostinger API.

- API version: 0.0.1-beta
- Package version: 1.0.0
- Generator version: 7.12.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.hostinger.com](https://www.hostinger.com)

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import hostinger-api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import hostinger-api
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import hostinger-api
from hostinger-api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://developers.hostinger.com
# See configuration.py for a list of all supported configuration parameters.
configuration = hostinger-api.Configuration(
    host = "https://developers.hostinger.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: apiToken
configuration = hostinger-api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with hostinger-api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger-api.BillingCatalogApi(api_client)

    try:
        # Get catalog item list
        api_response = api_instance.get_catalog_item_list_v1()
        print("The response of BillingCatalogApi->get_catalog_item_list_v1:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingCatalogApi->get_catalog_item_list_v1: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://developers.hostinger.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BillingCatalogApi* | [**get_catalog_item_list_v1**](docs/BillingCatalogApi.md#get_catalog_item_list_v1) | **GET** /api/billing/v1/catalog | Get catalog item list
*BillingOrdersApi* | [**create_new_service_order_v1**](docs/BillingOrdersApi.md#create_new_service_order_v1) | **POST** /api/billing/v1/orders | Create new service order
*BillingPaymentMethodsApi* | [**delete_payment_method_v1**](docs/BillingPaymentMethodsApi.md#delete_payment_method_v1) | **DELETE** /api/billing/v1/payment-methods/{paymentMethodId} | Delete payment method
*BillingPaymentMethodsApi* | [**get_payment_method_list_v1**](docs/BillingPaymentMethodsApi.md#get_payment_method_list_v1) | **GET** /api/billing/v1/payment-methods | Get payment method list
*BillingPaymentMethodsApi* | [**set_default_payment_method_v1**](docs/BillingPaymentMethodsApi.md#set_default_payment_method_v1) | **POST** /api/billing/v1/payment-methods/{paymentMethodId} | Set default payment method
*BillingSubscriptionsApi* | [**get_subscription_list_v1**](docs/BillingSubscriptionsApi.md#get_subscription_list_v1) | **GET** /api/billing/v1/subscriptions | Get subscription list
*DomainsPortfolioApi* | [**get_domain_list_v1**](docs/DomainsPortfolioApi.md#get_domain_list_v1) | **GET** /api/domains/v1/portfolio | Get domain list
*VPSActionsApi* | [**get_action_list_v1**](docs/VPSActionsApi.md#get_action_list_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/actions | Get action list
*VPSActionsApi* | [**get_action_v1**](docs/VPSActionsApi.md#get_action_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/actions/{actionId} | Get action
*VPSBackupsApi* | [**delete_backup_v1**](docs/VPSBackupsApi.md#delete_backup_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/backups/{backupId} | Delete backup
*VPSBackupsApi* | [**get_backup_list_v1**](docs/VPSBackupsApi.md#get_backup_list_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/backups | Get backup list
*VPSBackupsApi* | [**restore_backup_v1**](docs/VPSBackupsApi.md#restore_backup_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/backups/{backupId}/restore | Restore backup
*VPSDataCentersApi* | [**get_data_centers_list_v1**](docs/VPSDataCentersApi.md#get_data_centers_list_v1) | **GET** /api/vps/v1/data-centers | Get data centers list
*VPSFirewallApi* | [**activate_firewall_v1**](docs/VPSFirewallApi.md#activate_firewall_v1) | **POST** /api/vps/v1/firewall/{firewallId}/activate/{virtualMachineId} | Activate firewall
*VPSFirewallApi* | [**create_firewall_rule_v1**](docs/VPSFirewallApi.md#create_firewall_rule_v1) | **POST** /api/vps/v1/firewall/{firewallId}/rules | Create firewall rule
*VPSFirewallApi* | [**create_new_firewall_v1**](docs/VPSFirewallApi.md#create_new_firewall_v1) | **POST** /api/vps/v1/firewall | Create new firewall
*VPSFirewallApi* | [**deactivate_firewall_v1**](docs/VPSFirewallApi.md#deactivate_firewall_v1) | **POST** /api/vps/v1/firewall/{firewallId}/deactivate/{virtualMachineId} | Deactivate firewall
*VPSFirewallApi* | [**delete_firewall_rule_v1**](docs/VPSFirewallApi.md#delete_firewall_rule_v1) | **DELETE** /api/vps/v1/firewall/{firewallId}/rules/{ruleId} | Delete firewall rule
*VPSFirewallApi* | [**delete_firewall_v1**](docs/VPSFirewallApi.md#delete_firewall_v1) | **DELETE** /api/vps/v1/firewall/{firewallId} | Delete firewall
*VPSFirewallApi* | [**get_firewall_list_v1**](docs/VPSFirewallApi.md#get_firewall_list_v1) | **GET** /api/vps/v1/firewall | Get firewall list
*VPSFirewallApi* | [**get_firewall_v1**](docs/VPSFirewallApi.md#get_firewall_v1) | **GET** /api/vps/v1/firewall/{firewallId} | Get firewall
*VPSFirewallApi* | [**sync_firewall_v1**](docs/VPSFirewallApi.md#sync_firewall_v1) | **POST** /api/vps/v1/firewall/{firewallId}/sync/{virtualMachineId} | Sync firewall
*VPSFirewallApi* | [**update_firewall_rule_v1**](docs/VPSFirewallApi.md#update_firewall_rule_v1) | **PUT** /api/vps/v1/firewall/{firewallId}/rules/{ruleId} | Update firewall rule
*VPSMalwareScannerApi* | [**get_scan_metrics_v1**](docs/VPSMalwareScannerApi.md#get_scan_metrics_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/monarx | Get scan metrics
*VPSMalwareScannerApi* | [**install_monarx_v1**](docs/VPSMalwareScannerApi.md#install_monarx_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/monarx | Install Monarx
*VPSMalwareScannerApi* | [**uninstall_monarx_v1**](docs/VPSMalwareScannerApi.md#uninstall_monarx_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/monarx | Uninstall Monarx
*VPSOSTemplatesApi* | [**get_template_list_v1**](docs/VPSOSTemplatesApi.md#get_template_list_v1) | **GET** /api/vps/v1/templates | Get template list
*VPSOSTemplatesApi* | [**get_template_v1**](docs/VPSOSTemplatesApi.md#get_template_v1) | **GET** /api/vps/v1/templates/{templateId} | Get template
*VPSPTRRecordsApi* | [**create_ptr_record_v1**](docs/VPSPTRRecordsApi.md#create_ptr_record_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/ptr | Create PTR record
*VPSPTRRecordsApi* | [**delete_ptr_record_v1**](docs/VPSPTRRecordsApi.md#delete_ptr_record_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/ptr | Delete PTR record
*VPSPostInstallScriptsApi* | [**create_post_install_script_v1**](docs/VPSPostInstallScriptsApi.md#create_post_install_script_v1) | **POST** /api/vps/v1/post-install-scripts | Create post-install script
*VPSPostInstallScriptsApi* | [**delete_a_post_install_script_v1**](docs/VPSPostInstallScriptsApi.md#delete_a_post_install_script_v1) | **DELETE** /api/vps/v1/post-install-scripts/{postInstallScriptId} | Delete a post-install script
*VPSPostInstallScriptsApi* | [**get_post_install_script_list_v1**](docs/VPSPostInstallScriptsApi.md#get_post_install_script_list_v1) | **GET** /api/vps/v1/post-install-scripts | Get post-install script list
*VPSPostInstallScriptsApi* | [**get_post_install_script_v1**](docs/VPSPostInstallScriptsApi.md#get_post_install_script_v1) | **GET** /api/vps/v1/post-install-scripts/{postInstallScriptId} | Get post-install script
*VPSPostInstallScriptsApi* | [**update_post_install_script_v1**](docs/VPSPostInstallScriptsApi.md#update_post_install_script_v1) | **PUT** /api/vps/v1/post-install-scripts/{postInstallScriptId} | Update post-install script
*VPSPublicKeysApi* | [**attach_public_key_v1**](docs/VPSPublicKeysApi.md#attach_public_key_v1) | **POST** /api/vps/v1/public-keys/attach/{virtualMachineId} | Attach public key
*VPSPublicKeysApi* | [**create_new_public_key_v1**](docs/VPSPublicKeysApi.md#create_new_public_key_v1) | **POST** /api/vps/v1/public-keys | Create new public key
*VPSPublicKeysApi* | [**delete_a_public_key_v1**](docs/VPSPublicKeysApi.md#delete_a_public_key_v1) | **DELETE** /api/vps/v1/public-keys/{publicKeyId} | Delete a public key
*VPSPublicKeysApi* | [**get_public_key_list_v1**](docs/VPSPublicKeysApi.md#get_public_key_list_v1) | **GET** /api/vps/v1/public-keys | Get public key list
*VPSRecoveryApi* | [**start_recovery_mode_v1**](docs/VPSRecoveryApi.md#start_recovery_mode_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/recovery | Start recovery mode
*VPSRecoveryApi* | [**stop_recovery_mode_v1**](docs/VPSRecoveryApi.md#stop_recovery_mode_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/recovery | Stop recovery mode
*VPSSnapshotsApi* | [**create_snapshot_v1**](docs/VPSSnapshotsApi.md#create_snapshot_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/snapshot | Create snapshot
*VPSSnapshotsApi* | [**delete_snapshot_v1**](docs/VPSSnapshotsApi.md#delete_snapshot_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/snapshot | Delete snapshot
*VPSSnapshotsApi* | [**get_snapshot_v1**](docs/VPSSnapshotsApi.md#get_snapshot_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/snapshot | Get snapshot
*VPSSnapshotsApi* | [**restore_snapshot_v1**](docs/VPSSnapshotsApi.md#restore_snapshot_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/snapshot/restore | Restore snapshot
*VPSVirtualMachineApi* | [**get_metrics_v1**](docs/VPSVirtualMachineApi.md#get_metrics_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/metrics | Get metrics
*VPSVirtualMachineApi* | [**get_virtual_machine_list_v1**](docs/VPSVirtualMachineApi.md#get_virtual_machine_list_v1) | **GET** /api/vps/v1/virtual-machines | Get virtual machine list
*VPSVirtualMachineApi* | [**get_virtual_machine_v1**](docs/VPSVirtualMachineApi.md#get_virtual_machine_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId} | Get virtual machine
*VPSVirtualMachineApi* | [**recreate_virtual_machine_v1**](docs/VPSVirtualMachineApi.md#recreate_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/recreate | Recreate virtual machine
*VPSVirtualMachineApi* | [**reset_hostname_v1**](docs/VPSVirtualMachineApi.md#reset_hostname_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/hostname | Reset hostname
*VPSVirtualMachineApi* | [**restart_virtual_machine_v1**](docs/VPSVirtualMachineApi.md#restart_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/restart | Restart virtual machine
*VPSVirtualMachineApi* | [**set_hostname_v1**](docs/VPSVirtualMachineApi.md#set_hostname_v1) | **PUT** /api/vps/v1/virtual-machines/{virtualMachineId}/hostname | Set hostname
*VPSVirtualMachineApi* | [**set_nameservers_v1**](docs/VPSVirtualMachineApi.md#set_nameservers_v1) | **PUT** /api/vps/v1/virtual-machines/{virtualMachineId}/nameservers | Set nameservers
*VPSVirtualMachineApi* | [**set_panel_password_v1**](docs/VPSVirtualMachineApi.md#set_panel_password_v1) | **PUT** /api/vps/v1/virtual-machines/{virtualMachineId}/panel-password | Set panel password
*VPSVirtualMachineApi* | [**set_root_password_v1**](docs/VPSVirtualMachineApi.md#set_root_password_v1) | **PUT** /api/vps/v1/virtual-machines/{virtualMachineId}/root-password | Set root password
*VPSVirtualMachineApi* | [**setup_new_virtual_machine_v1**](docs/VPSVirtualMachineApi.md#setup_new_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/setup | Setup new virtual machine
*VPSVirtualMachineApi* | [**start_virtual_machine_v1**](docs/VPSVirtualMachineApi.md#start_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/start | Start virtual machine
*VPSVirtualMachineApi* | [**stop_virtual_machine_v1**](docs/VPSVirtualMachineApi.md#stop_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/stop | Stop virtual machine


## Documentation For Models

 - [BillingV1CatalogCatalogItemPriceResource](docs/BillingV1CatalogCatalogItemPriceResource.md)
 - [BillingV1CatalogCatalogItemResource](docs/BillingV1CatalogCatalogItemResource.md)
 - [BillingV1OrderOrderBillingAddressResource](docs/BillingV1OrderOrderBillingAddressResource.md)
 - [BillingV1OrderOrderResource](docs/BillingV1OrderOrderResource.md)
 - [BillingV1OrderStoreRequest](docs/BillingV1OrderStoreRequest.md)
 - [BillingV1OrderStoreRequestItemsInner](docs/BillingV1OrderStoreRequestItemsInner.md)
 - [BillingV1PaymentMethodPaymentMethodResource](docs/BillingV1PaymentMethodPaymentMethodResource.md)
 - [BillingV1SubscriptionSubscriptionResource](docs/BillingV1SubscriptionSubscriptionResource.md)
 - [CommonSchemaErrorResponseSchema](docs/CommonSchemaErrorResponseSchema.md)
 - [CommonSchemaUnauthorizedResponseSchema](docs/CommonSchemaUnauthorizedResponseSchema.md)
 - [CommonSchemaUnprocessableContentResponseSchema](docs/CommonSchemaUnprocessableContentResponseSchema.md)
 - [CommonSchemaUnprocessableContentResponseSchemaErrors](docs/CommonSchemaUnprocessableContentResponseSchemaErrors.md)
 - [CommonSuccessEmptyResource](docs/CommonSuccessEmptyResource.md)
 - [DomainsV1DomainDomainResource](docs/DomainsV1DomainDomainResource.md)
 - [VPSGetActionListV1200Response](docs/VPSGetActionListV1200Response.md)
 - [VPSGetBackupListV1200Response](docs/VPSGetBackupListV1200Response.md)
 - [VPSGetFirewallListV1200Response](docs/VPSGetFirewallListV1200Response.md)
 - [VPSGetFirewallListV1200ResponseMeta](docs/VPSGetFirewallListV1200ResponseMeta.md)
 - [VPSGetPostInstallScriptListV1200Response](docs/VPSGetPostInstallScriptListV1200Response.md)
 - [VPSGetPublicKeyListV1200Response](docs/VPSGetPublicKeyListV1200Response.md)
 - [VPSV1ActionActionResource](docs/VPSV1ActionActionResource.md)
 - [VPSV1BackupBackupResource](docs/VPSV1BackupBackupResource.md)
 - [VPSV1DataCenterDataCenterResource](docs/VPSV1DataCenterDataCenterResource.md)
 - [VPSV1FirewallFirewallResource](docs/VPSV1FirewallFirewallResource.md)
 - [VPSV1FirewallFirewallRuleResource](docs/VPSV1FirewallFirewallRuleResource.md)
 - [VPSV1FirewallRulesStoreRequest](docs/VPSV1FirewallRulesStoreRequest.md)
 - [VPSV1FirewallStoreRequest](docs/VPSV1FirewallStoreRequest.md)
 - [VPSV1IPAddressIPAddressResource](docs/VPSV1IPAddressIPAddressResource.md)
 - [VPSV1MalwareMetricsResource](docs/VPSV1MalwareMetricsResource.md)
 - [VPSV1MetricsMetricsCollection](docs/VPSV1MetricsMetricsCollection.md)
 - [VPSV1MetricsMetricsCollectionCpuUsage](docs/VPSV1MetricsMetricsCollectionCpuUsage.md)
 - [VPSV1MetricsMetricsCollectionDiskSpace](docs/VPSV1MetricsMetricsCollectionDiskSpace.md)
 - [VPSV1MetricsMetricsCollectionIncomingTraffic](docs/VPSV1MetricsMetricsCollectionIncomingTraffic.md)
 - [VPSV1MetricsMetricsCollectionOutgoingTraffic](docs/VPSV1MetricsMetricsCollectionOutgoingTraffic.md)
 - [VPSV1MetricsMetricsCollectionRamUsage](docs/VPSV1MetricsMetricsCollectionRamUsage.md)
 - [VPSV1MetricsMetricsCollectionUptime](docs/VPSV1MetricsMetricsCollectionUptime.md)
 - [VPSV1MetricsMetricsResource](docs/VPSV1MetricsMetricsResource.md)
 - [VPSV1PostInstallScriptPostInstallScriptResource](docs/VPSV1PostInstallScriptPostInstallScriptResource.md)
 - [VPSV1PostInstallScriptStoreRequest](docs/VPSV1PostInstallScriptStoreRequest.md)
 - [VPSV1PublicKeyAttachRequest](docs/VPSV1PublicKeyAttachRequest.md)
 - [VPSV1PublicKeyPublicKeyResource](docs/VPSV1PublicKeyPublicKeyResource.md)
 - [VPSV1PublicKeyStoreRequest](docs/VPSV1PublicKeyStoreRequest.md)
 - [VPSV1SnapshotSnapshotResource](docs/VPSV1SnapshotSnapshotResource.md)
 - [VPSV1TemplateTemplateResource](docs/VPSV1TemplateTemplateResource.md)
 - [VPSV1VirtualMachineHostnameUpdateRequest](docs/VPSV1VirtualMachineHostnameUpdateRequest.md)
 - [VPSV1VirtualMachineMetricGetRequest](docs/VPSV1VirtualMachineMetricGetRequest.md)
 - [VPSV1VirtualMachineNameserversUpdateRequest](docs/VPSV1VirtualMachineNameserversUpdateRequest.md)
 - [VPSV1VirtualMachinePanelPasswordUpdateRequest](docs/VPSV1VirtualMachinePanelPasswordUpdateRequest.md)
 - [VPSV1VirtualMachineRecoveryStartRequest](docs/VPSV1VirtualMachineRecoveryStartRequest.md)
 - [VPSV1VirtualMachineRecreateRequest](docs/VPSV1VirtualMachineRecreateRequest.md)
 - [VPSV1VirtualMachineRootPasswordUpdateRequest](docs/VPSV1VirtualMachineRootPasswordUpdateRequest.md)
 - [VPSV1VirtualMachineSetupRequest](docs/VPSV1VirtualMachineSetupRequest.md)
 - [VPSV1VirtualMachineSetupRequestPublicKey](docs/VPSV1VirtualMachineSetupRequestPublicKey.md)
 - [VPSV1VirtualMachineVirtualMachineResource](docs/VPSV1VirtualMachineVirtualMachineResource.md)
 - [VPSV1VirtualMachineVirtualMachineResourceIpv4](docs/VPSV1VirtualMachineVirtualMachineResourceIpv4.md)
 - [VPSV1VirtualMachineVirtualMachineResourceIpv6](docs/VPSV1VirtualMachineVirtualMachineResourceIpv6.md)
 - [VPSV1VirtualMachineVirtualMachineResourceTemplate](docs/VPSV1VirtualMachineVirtualMachineResourceTemplate.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="apiToken"></a>
### apiToken

- **Type**: Bearer authentication


## Author




