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

from neutronclient.neutron import v2_0 as neutronV20
from neutronclient.openstack.common.gettextutils import _


class ListSslPolicy(neutronV20.ListCommand):
    """List SSL Policies that belong to a given tenant."""

    resource = 'ssl_policy'
    log = logging.getLogger(__name__ + '.ListSslPolicy')
    list_columns = ['id', 'name', 'description', 'front_end_enabled', 'front_end_protocols',
                   'front_end_cipher_suites', 'back_end_enabled', 'back_end_protocols', 
                   'back_end_cipher_suites'] 
    pagination_support = True
    sorting_support = True


class ShowSslPolicy(neutronV20.ShowCommand):
    """Show information of a given SSL Policy."""

    resource = 'ssl_policy'
    log = logging.getLogger(__name__ + '.ShowSslPolicy')


class CreateSslPolicy(neutronV20.CreateCommand):
    """Create a SSL Policy."""

    resource = 'ssl_policy'
    log = logging.getLogger(__name__ + '.CreateSslPolicy')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--front_end_enabled',
            required=True,
            choices=['True', 'False'],
            help=_('Enable front end SSL offloading'))
        parser.add_argument(
            '--front_end_protocols',
            help=_('Front end protocol to be used.Comma seperated list of SSLv2,SSLv3,TLSv1'))
        parser.add_argument(
            '--front_end_cipher_suites',
            choices=['ALL', 'LOW', 'MEDIUM', 'HIGH'],
            help=_('Openssl cipher suites.One of ALL,HIGH,MEDIUM,LOW'))
        parser.add_argument(
            '--back_end_enabled',
            required=True,
            choices=['True', 'False'],
            help=_('Enable back end SSL offloading'))
        parser.add_argument(
            '--back_end_protocols',
            help=_('Back end protocol to be used.Comma seperated list of SSLv2,SSLv3,TLSv1'))
        parser.add_argument(
            '--back_end_cipher_suites',
            choices=['ALL', 'LOW', 'MEDIUM', 'HIGH'],
            help=_('Openssl cipher suites.One of ALL,HIGH,MEDIUM,LOW'))
        parser.add_argument(
            '--description',
            help=_('Description of the SSL Policy'))
        parser.add_argument(
            '--name',
            required=True,
            help=_('Name of the SSL Policy'))

    def args2body(self, parsed_args):
        body = {
            self.resource: {
            },
        }
        neutronV20.update_dict(parsed_args, body[self.resource],
                  ['name', 'description', 'front_end_enabled', 'front_end_protocols',
                   'front_end_cipher_suites', 'back_end_enabled', 'back_end_protocols', 
                   'back_end_cipher_suites', 'tenant_id'])
        return body


class UpdateSslPolicy(neutronV20.UpdateCommand):
    """Update a given SSL Policy."""

    resource = 'ssl_policy'
    log = logging.getLogger(__name__ + '.UpdateSslPolicy')


class DeleteSslPolicy(neutronV20.DeleteCommand):
    """Delete a given SSL Policy."""

    resource = 'ssl_policy'
    log = logging.getLogger(__name__ + '.DeleteSslPolicy')



