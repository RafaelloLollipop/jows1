#!/usr/bin/python

'This example creates a simple network topology with 1 AP and 2 stations and 1 host'

import sys

from mininet.node import Controller
from mininet.log import setLogLevel, info
from mininet.wifi.node import OVSKernelAP
from mininet.wifi.cli import CLI_wifi
from mininet.wifi.net import Mininet_wifi


def topology(isVirtual):
    "Create a network."
    net = Mininet_wifi(controller=Controller, accessPoint=OVSKernelAP)

    info("*** Creating nodes\n")
    h1= net.addHost('h1',ip='10.0.0.1')
    sta1 = net.addStation( 'sta1' )
    sta2 = net.addStation( 'sta2' )
    ap1 = net.addAccessPoint( 'ap1', ssid="simplewifi", mode="g", channel="5" )
    c0 = net.addController('c0', controller=Controller, ip='127.0.0.1', port=6633 )
    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Associating Stations\n")
    net.addLink(sta1, ap1)
    net.addLink(sta2, ap1)
    net.addLink(h1, ap1)

    info("*** Starting network\n")
    net.build()
    c0.start()
    ap1.start([c0])

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    isVirtual = True if '-v' in sys.argv else False
    topology(isVirtual)
