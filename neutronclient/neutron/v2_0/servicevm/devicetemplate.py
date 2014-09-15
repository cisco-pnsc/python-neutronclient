# Copyright 2013 Mirantis Inc.
# All Rights Reserved
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# @author: Ilya Shakhat, Mirantis Inc.
#
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import logging
import argparse
from neutronclient.neutron import v2_0 as neutronV20
from neutronclient.openstack.common.gettextutils import _
from neutronclient.common import utils
import pdb

class ListDeviceTemplate(neutronV20.ListCommand):
    """List device templates that belong to a given tenant."""

    resource = 'device_template'
    log = logging.getLogger(__name__ + '.ListDeviceTemplate')
    list_columns = ['id', 'name', 'description', 'device_driver', 'mgmt_driver',
                    'service_types', 'attributes']
    pagination_support = True
    sorting_support = True


class ShowDeviceTemplate(neutronV20.ShowCommand):
    """Show information of a given device template."""

    resource = 'device_template'
    log = logging.getLogger(__name__ + '.ShowDeviceTemplate')


class CreateDeviceTemplate(neutronV20.CreateCommand):
    """Create a device template."""

    resource = 'device_template'
    log = logging.getLogger(__name__ + '.CreateDeviceTemplate')    
    def add_known_arguments(self, parser):
        mandatory_attributes= "\n MANDATORY-ATTRIBUTES : ['admin_user', 'admin_password','platform'] \n "
        optional_attributes = """  'OPTIONAL-ATTRIBUTES : [enable_ha','version','throughput_level',
                             'feature_level','availability_zone','availability_zone_primary',
                            'availability_zone_secondary','license_category']"""
        parser.add_argument(
            '--description',
            help='description of the device template')
        parser.add_argument(
            '--service-type',
            required=True, dest='service_types',
            #choices=['lbaas', 'l3_router'],
            help='the service type of the Cisco device template are [l3router,lbaas]')
        parser.add_argument(
            '--name',
            required=True,
            help='the name of the device template')
        parser.add_argument(
            '--attribute',
            dest='attributes',
            required=True,
            help='attributes for the Cisco device template are ' 
             + mandatory_attributes  + optional_attributes)
        parser.add_argument(
            '--scope',
            help=' Scope of the device template, for global scope --scope=global')
    def args2body(self, parsed_args):
        body = {
            'device_template': {
            'name': parsed_args.name,
            'description': parsed_args.description,
            'mgmt_driver': 'noop',
            'device_driver': 'noop',
            'scope': parsed_args.scope
            }
	}
        attr_dict = utils.str2dict(parsed_args.attributes)
        body['device_template'].update({'attributes':attr_dict})
        services = []
        serv_dict = utils.str2dict(parsed_args.service_types)
	services.append(serv_dict)
        body['device_template'].update({'service_types':services})
        if parsed_args.tenant_id:
            body['device_template'].update({'tenant_id': parsed_args.tenant_id})
        return body


class UpdateDeviceTemplate(neutronV20.UpdateCommand):
    """Update a given device template."""

    resource = 'device_template'
    log = logging.getLogger(__name__ + '.UpdateDeviceTemplate')


class DeleteDeviceTemplate(neutronV20.DeleteCommand):
    """Delete a given device template."""

    resource = 'device_template'
    log = logging.getLogger(__name__ + '.DeleteDeviceTemplate')

