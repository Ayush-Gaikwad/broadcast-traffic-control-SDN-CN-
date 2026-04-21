from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI

class SingleSwitchTopo(Topo):
    def build(self):
        # Create one switch
        s1 = self.addSwitch('s1')

        # Create four hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Connect all hosts to the switch
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)
        self.addLink(h4, s1)

if __name__ == '__main__':
    topo = SingleSwitchTopo()
    net = Mininet(topo=topo, controller=RemoteController)
    net.start()
    print("Network Started")
    CLI(net)
    net.stop()
