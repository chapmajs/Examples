HE.net IPv6 Tunnel Update
-------------------------

More detailed writeup: [http://www.glitchwrks.com/2015/11/04/openbsd-and-hurricane-electric](http://www.glitchwrks.com/2015/11/04/openbsd-and-hurricane-electric)

Here's my solution to keeping my HE.net tunnel up-to-date with a dynamic WAN IP. `hostname.gif0` dynamically picks the egress interface's IPv4 address as the local end of the tunnel. `update_he.sh` is intended to run periodically to keep the tunnel up-to-date.

Configuring update_he.sh
------------------------

You'll need to set a few variables in `update_he.sh`:

* USERNAME is your tunnelbroker.net username
* PASSWORD can be either your tunnelbroker.net password or a specific password for the tunnel (recommend configuring tunnel password)
* TUNNEL_ID is provided in your Hurricane Electric tunnel info
* TUNNEL_IF should be your gif interface, most often `gif0`
* HE_ENDPOINT is provided in your Hurricane Electric sample configs, mine has always been `209.51.161.14`

Additionally, `update_he.sh` currently uses `curl` which is not part of the base OpenBSD install. You can add it from packages, or build it as a port. This is the only dependency not included in base.

Once you've modified `update_he.sh` as required, place it somewhere in the filesystem (mine lives in `/usr/local/bin/`) and set appropriate permissions (try `chmod 540` to make it +rx for root and +r for wheel). Then, add it to root's crontab:

```
# Update HE.net tunnel every 5 minutes
*/5     *       *       *       *       /usr/local/bin/update_he.sh > /dev/null
```

This will run the script every 5 minutes. You can omit the redirect to `/dev/null` for testing. Errors (and debug output, if you omit the redirect) will be emailed to the default recipient for root's crontab mail.