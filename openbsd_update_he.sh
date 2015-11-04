#!/bin/sh

# Hurricane Electric tunnelbroker.net IPv4 Endpoint Updater for OpenBSD
# Copyright (c) 2015 Jonathan Chapman
# http://www.glitchwrks.com

# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later 
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more 
# details.

# You should have received a copy of the GNU General Public License along with
# this program. If not, see http://www.gnu.org/licenses/.

USERNAME=your-he.net-username
PASSWORD=your-tunnel-password
TUNNEL_ID=your-tunnel-id
TUNNEL_IF=gif0
HE_ENDPOINT=209.51.161.14

function error_exit
{
	>&2 echo "Update failed, result was $1"
	exit 1
}

result=$(/usr/local/bin/curl -sS https://ipv4.tunnelbroker.net/nic/update?username=$USERNAME\&password=$PASSWORD\&hostname=$TUNNEL_ID)

case $( echo "$result" | awk '{ print $1 }' ) in
	nochg)
		echo "Update succeeded, no change in IP"
		;;
	good)
		new_ip=$( echo "$result" | awk '{ print $2 }' )
		
		if [ "$new_ip" = "127.0.0.1" ]; then
			error_exit $result
		else
			echo "Update succeeded, updating $TUNNEL_IF to $new_ip"
			/sbin/ifconfig $TUNNEL_IF tunnel $new_ip $HE_ENDPOINT
		fi;
		;;
	*)
		error_exit $result
esac

