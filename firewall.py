'''
Programming Assignment

Professor: Marcos Vieira

Student: Mauricio de Oliveira

'''

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
import csv

log = core.getLogger()
policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ[ 'HOME' ]  

''' Add your global variables here ... '''

class Firewall (EventMixin):

    def __init__ (self):

        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")
        
        self.firewall_rules = []
        
        # read csv file
        # https://docs.python.org/2/library/csv.html

        with open(policyFile, 'rb') as firewall_rules:

            fr = csv.reader(firewall_rules, delimiter = ',')
            next(fr) # skip header

            for row in fr:
                self.firewall_rules.append((EthAddr(row[1]), EthAddr(row[2])))
                self.firewall_rules.append((EthAddr(row[2]), EthAddr(row[1])))

    def _handle_ConnectionUp (self, event):    

        ''' Implements the switch logic. '''

        for tup in self.firewall_rules:
           
            # create match
            match = of.ofp_match(dl_src = tup[0], dl_dst = tup[1])
            
            # create a flow mod to send
            msg = of.ofp_flow_mod(match = match)
            #, action = of.ofp_action_output(port=of.OFPP_NONE))

            # send flow mod to install on table
            event.connection.send(msg)
    
        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    '''
    Starting the Firewall module
    '''
    core.registerNew(Firewall)





