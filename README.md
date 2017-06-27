Example Code for The Glitch Works
=================================

The following files are bits of example code from writeups at http://www.glitchwrks.com

display_test.py
---------------

This Python script will write a bitmapped test pattern to the Sabernetics Mini-I2C OLED display connected to a Bus Pirate. Tested with Python 3.2.3 and pySerial 2.6-2.

injector.py and injectable.py
-----------------------------

Demonstrate dependency injection with Python 2. Hi ragechin!

ssltest.py and hb_honeypot.pl
-----------------------------

`ssltest.py` is a modified version of a modified version of the PoC for CVE-2014-0160 'Heartbleed' by Jared Stafford (jspenguin@jspenguin.org). Scans single hosts, doesn't do the hex dump.

`hb_honeypot.pl` listens on TCP port 443 and pukes bogus SSL messages into the socket while looking for something like part of the HELO from Jared's demo. It logs IPs to the console and returns a vulnerable-looking heartbeat response.

eprom_timer.rb
--------------

`eprom_timer.rb` is a quick little script to control one of my [relay switched outlets](http://www.glitchwrks.com/2013/02/28/relay-board) using the handshake lines on a USB -> RS-232 adapter. Requires the `serialport` and `ruby-progressbar` gems. Read more [here](http://www.glitchwrks.com/2016/03/21/eprom-timer)

equality.py
-----------

`equality.py` demonstrates why "truth of x==y does not imply falsehood of x!=y" by implementing `__eq__` and `__ne__` in a stupid manner. Remember that `==` and `!=` are effectively method aliases to `__eq__` and `__ne__`, respectively.