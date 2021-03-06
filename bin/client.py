#!/usr/bin/env python
#
# Copyright (c) 2014-2015 SUSE LLC
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
import argparse

from src.client.config import ClientConfig
from src.client.client import Client
from src.daemonize import daemonize

DEFAULT_CONFIG_FILE = '/etc/sysconfig/rhn/osad.conf'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config',
                        default=DEFAULT_CONFIG_FILE,
                        dest='config_file',
                        help='alternative configuration file')
    parser.add_argument('-d', '--daemon',
                        dest='daemon',
                        action='store_true',
                        help='run as daemon',
                        default=False)
    args = parser.parse_args()

    config = ClientConfig(args.config_file)
    client = Client(config)

    if args.daemon:
        daemonize(client)
    else:
        try:
            client.start()
        finally:
            client.stop()
