# Firewall Using Software Defined Networking

This project implements a firewall using the mininet environment and the SDN controller pox. [mininet](https://github.com/mininet/mininet) [pox](https://github.com/noxrepo/pox)

The easiest way to run it is by installing a mininet virtual machine, available [here.](https://homepages.dcc.ufmg.br/~mmvieira/cc/pyretic_0.2.0.ova)

All the files in this repo should go under pox/pox/misc on the virtual machine.

You may wanna watch [this](https://www.youtube.com/watch?v=yNmv7GiHIKE) mininet tutorial.

# Overview

The network you'll use in this exercise includes 3 hosts and a switch with an OpenFlow controller (POX):

![Image1](http://homepages.dcc.ufmg.br/~mmvieira/cc/Assignment%20Details%20_%20Coursera4_files/JgNextBvzib8PTXVvnA-4QF-D5J3GdqxIoVKvuRwo0gPhgqRppQ6DH32SdWb.png)

Again, you may need to watch [the mininet tutorial.](https://www.youtube.com/watch?v=yNmv7GiHIKE)

# Files

1. firewall.py: a skeleton class which you will update with the logic for installing firewall rules.
2. firewall-policies.csv:  a list of MAC pairs (i.e., policies) read as input by the firewall application.
3. test.py: used to test your code.

If your firewall implementation is correct, some pairs of hosts are not able to reach each other.
Once you have your code, copy the firewall.py in the ~/pox/pox/misc directory on your VM, as well as test.py and firewall-policies.csv.

Start pox:

```$ pox.py forwarding.l2_learning misc.firewall```

Start mininet:

```$ sudo mn --topo single,3 --controller remote --mac```

In the mininet terminal, you can use ping to see if the policies were succesfully implemented. For example,

```$ h1 ping -c1 h3```

```$ h2 ping -c2 h4```

# Testing your code

Run test.py with sudo privileges. The script starts both pox and mininet and perform a few pings between hosts.
The first ping between host 3 and host 6 should not be succesful, but the ping between 4 and 6 should.
