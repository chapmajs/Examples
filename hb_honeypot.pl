#!/usr/bin/perl

# hb_honeypot.pl -- a quick 'n dirty honeypot hack for Heartbleed
#
# This Perl script listens on TCP port 443 and responds with completely bogus
# SSL heartbeat responses, unless it detects the start of a byte pattern
# similar to that used in Jared Stafford's (jspenguin@jspenguin.org) demo for
# CVE-2014-0160 'Heartbleed'.
#
# Run as root for the privileged port. Outputs IPs of suspected heartbleed scan
# to the console. Rickrolls scanner in the hex dump.
#
# shouts to binrev
#
# Copyright (c) 8 April 2014 The Glitch Works
# http://www.glitchwrks.com/
# Version 0.1.1

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

use strict;
use warnings;
use IO::Socket;

my $sock = new IO::Socket::INET (
                                  LocalPort => '443',
                                  Proto => 'tcp',
                                  Listen => 1,
                                  Reuse => 1,
                                );

die "Could not create socket!" unless $sock;

# The "done" bit of the handshake response
my $done = pack ("H*", '16030100010E');

# Your message here
my $taunt = "09809*)(*)(76&^%&(*&^7657332         Hi there!                  Your scan has   been logged!                    Have no fear,   this is for     research only --                                We're never gonna give you up,  never gonna let you down!";
my $troll = pack ("H*", ('180301' . sprintf( "%04x", length($taunt))));

# main "barf responses into the socket" loop
while (my $client = $sock->accept()) {
  $client->autoflush(1);
 
  my $found = 0;

  # read things that look like lines, puke nonsense heartbeat responses until
  # a line that looks like it's from the PoC shows up
  while (<$client>) {
    my $line = unpack("H*", $_);

    if ($line =~ /^0034.*/) {
      print $client $done;
      $found = 1;
    } else {
      print $client $troll;
      print $client $taunt;
    }

    if ($found == 1) {
      print $client $troll;
      print $client $taunt;
      print $client->peerhost . "\n";
      $found = 0;
    }
  }  
}

close($sock);

