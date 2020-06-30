# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration_async import NetworkManagementClientConfiguration
from .operations_async import ApplicationGatewaysOperations
from .operations_async import NetworkManagementClientOperationsMixin
from .operations_async import ExpressRouteCircuitAuthorizationsOperations
from .operations_async import ExpressRouteCircuitPeeringsOperations
from .operations_async import ExpressRouteCircuitsOperations
from .operations_async import ExpressRouteServiceProvidersOperations
from .operations_async import LoadBalancersOperations
from .operations_async import NetworkInterfacesOperations
from .operations_async import NetworkSecurityGroupsOperations
from .operations_async import SecurityRulesOperations
from .operations_async import PublicIPAddressesOperations
from .operations_async import RouteTablesOperations
from .operations_async import RoutesOperations
from .operations_async import UsagesOperations
from .operations_async import VirtualNetworksOperations
from .operations_async import SubnetsOperations
from .operations_async import VirtualNetworkGatewaysOperations
from .operations_async import VirtualNetworkGatewayConnectionsOperations
from .operations_async import LocalNetworkGatewaysOperations
from .. import models


class NetworkManagementClient(NetworkManagementClientOperationsMixin):
    """Network Client.

    :ivar application_gateways: ApplicationGatewaysOperations operations
    :vartype application_gateways: azure.mgmt.network.v2015_06_15.aio.operations_async.ApplicationGatewaysOperations
    :ivar express_route_circuit_authorizations: ExpressRouteCircuitAuthorizationsOperations operations
    :vartype express_route_circuit_authorizations: azure.mgmt.network.v2015_06_15.aio.operations_async.ExpressRouteCircuitAuthorizationsOperations
    :ivar express_route_circuit_peerings: ExpressRouteCircuitPeeringsOperations operations
    :vartype express_route_circuit_peerings: azure.mgmt.network.v2015_06_15.aio.operations_async.ExpressRouteCircuitPeeringsOperations
    :ivar express_route_circuits: ExpressRouteCircuitsOperations operations
    :vartype express_route_circuits: azure.mgmt.network.v2015_06_15.aio.operations_async.ExpressRouteCircuitsOperations
    :ivar express_route_service_providers: ExpressRouteServiceProvidersOperations operations
    :vartype express_route_service_providers: azure.mgmt.network.v2015_06_15.aio.operations_async.ExpressRouteServiceProvidersOperations
    :ivar load_balancers: LoadBalancersOperations operations
    :vartype load_balancers: azure.mgmt.network.v2015_06_15.aio.operations_async.LoadBalancersOperations
    :ivar network_interfaces: NetworkInterfacesOperations operations
    :vartype network_interfaces: azure.mgmt.network.v2015_06_15.aio.operations_async.NetworkInterfacesOperations
    :ivar network_security_groups: NetworkSecurityGroupsOperations operations
    :vartype network_security_groups: azure.mgmt.network.v2015_06_15.aio.operations_async.NetworkSecurityGroupsOperations
    :ivar security_rules: SecurityRulesOperations operations
    :vartype security_rules: azure.mgmt.network.v2015_06_15.aio.operations_async.SecurityRulesOperations
    :ivar public_ip_addresses: PublicIPAddressesOperations operations
    :vartype public_ip_addresses: azure.mgmt.network.v2015_06_15.aio.operations_async.PublicIPAddressesOperations
    :ivar route_tables: RouteTablesOperations operations
    :vartype route_tables: azure.mgmt.network.v2015_06_15.aio.operations_async.RouteTablesOperations
    :ivar routes: RoutesOperations operations
    :vartype routes: azure.mgmt.network.v2015_06_15.aio.operations_async.RoutesOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.network.v2015_06_15.aio.operations_async.UsagesOperations
    :ivar virtual_networks: VirtualNetworksOperations operations
    :vartype virtual_networks: azure.mgmt.network.v2015_06_15.aio.operations_async.VirtualNetworksOperations
    :ivar subnets: SubnetsOperations operations
    :vartype subnets: azure.mgmt.network.v2015_06_15.aio.operations_async.SubnetsOperations
    :ivar virtual_network_gateways: VirtualNetworkGatewaysOperations operations
    :vartype virtual_network_gateways: azure.mgmt.network.v2015_06_15.aio.operations_async.VirtualNetworkGatewaysOperations
    :ivar virtual_network_gateway_connections: VirtualNetworkGatewayConnectionsOperations operations
    :vartype virtual_network_gateway_connections: azure.mgmt.network.v2015_06_15.aio.operations_async.VirtualNetworkGatewayConnectionsOperations
    :ivar local_network_gateways: LocalNetworkGatewaysOperations operations
    :vartype local_network_gateways: azure.mgmt.network.v2015_06_15.aio.operations_async.LocalNetworkGatewaysOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = NetworkManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.application_gateways = ApplicationGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.express_route_circuit_authorizations = ExpressRouteCircuitAuthorizationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.express_route_circuit_peerings = ExpressRouteCircuitPeeringsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.express_route_circuits = ExpressRouteCircuitsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.express_route_service_providers = ExpressRouteServiceProvidersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.load_balancers = LoadBalancersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.network_interfaces = NetworkInterfacesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.network_security_groups = NetworkSecurityGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.security_rules = SecurityRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.public_ip_addresses = PublicIPAddressesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.route_tables = RouteTablesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.routes = RoutesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_networks = VirtualNetworksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.subnets = SubnetsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_network_gateways = VirtualNetworkGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_network_gateway_connections = VirtualNetworkGatewayConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.local_network_gateways = LocalNetworkGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "NetworkManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
