# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class FileServer(Resource):
    """Contains information about an Azure Batch AI file server.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The ID of the resource
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource
    :vartype type: str
    :ivar location: The location of the resource
    :vartype location: str
    :ivar tags: The tags of the resource
    :vartype tags: dict
    :param vm_size: The size of the virtual machine of the file server. For
     information about available VM sizes for fileservers from the Virtual
     Machines Marketplace, see Sizes for Virtual Machines (Linux).
    :type vm_size: str
    :param ssh_configuration: SSH settings for the file server.
    :type ssh_configuration: :class:`SshConfiguration
     <azure.mgmt.batchai.models.SshConfiguration>`
    :param data_disks: Settings for the data disk which would be created for
     the file server.
    :type data_disks: :class:`DataDisks <azure.mgmt.batchai.models.DataDisks>`
    :param subnet: Specifies the identifier of the subnet.
    :type subnet: :class:`ResourceId <azure.mgmt.batchai.models.ResourceId>`
    :ivar mount_settings: Details of the file Server.
    :vartype mount_settings: :class:`MountSettings
     <azure.mgmt.batchai.models.MountSettings>`
    :ivar provisioning_state_transition_time: Time when the status was
     changed.
    :vartype provisioning_state_transition_time: datetime
    :ivar creation_time: Time when the FileServer was created.
    :vartype creation_time: datetime
    :ivar provisioning_state: Specifies the provisioning state of the file
     server. Possible values: creating - The fileServer is just getting
     created. Updating - The file server creation has been accepted and it is
     getting updated. Deleting - The user has requested that the cluster be
     deleted, but the delete operation has not yet completed. Failed - The file
     server creation has failed with the specified errorCode. Details about the
     error code are specified in the message field. Succeeded - The file server
     creation has succeeded. Possible values include: 'creating', 'updating',
     'deleting', 'succeeded', 'failed'
    :vartype provisioning_state: str or :class:`FileServerProvisioningState
     <azure.mgmt.batchai.models.FileServerProvisioningState>`
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'readonly': True},
        'tags': {'readonly': True},
        'mount_settings': {'readonly': True},
        'provisioning_state_transition_time': {'readonly': True},
        'creation_time': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'vm_size': {'key': 'properties.vmSize', 'type': 'str'},
        'ssh_configuration': {'key': 'properties.sshConfiguration', 'type': 'SshConfiguration'},
        'data_disks': {'key': 'properties.dataDisks', 'type': 'DataDisks'},
        'subnet': {'key': 'properties.subnet', 'type': 'ResourceId'},
        'mount_settings': {'key': 'properties.mountSettings', 'type': 'MountSettings'},
        'provisioning_state_transition_time': {'key': 'properties.provisioningStateTransitionTime', 'type': 'iso-8601'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'FileServerProvisioningState'},
    }

    def __init__(self, vm_size=None, ssh_configuration=None, data_disks=None, subnet=None):
        super(FileServer, self).__init__()
        self.vm_size = vm_size
        self.ssh_configuration = ssh_configuration
        self.data_disks = data_disks
        self.subnet = subnet
        self.mount_settings = None
        self.provisioning_state_transition_time = None
        self.creation_time = None
        self.provisioning_state = None
