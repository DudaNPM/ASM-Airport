import jsonpickle

from spade import agent
from spade.behaviour import CyclicBehaviour


def printInfo(received):
    print('\n##################################################################################################################################')
    print('################################### LANDINGS')
    for landing in received.get('aterragens'):
        print(landing.toString())
    
    print('##################################################################################################################################')
    print('################################### TAKEOFFS')
    for takeoff in received.get('descolagens'):
        print(takeoff.toString())
    
    print('##################################################################################################################################')
    print('################################### GARES')
    for gare in received.get('gares'):
        print(gare.toString())
    
    print('##################################################################################################################################\n')


class Info(agent.Agent):

    async def setup(self):
        print("Agent {}".format(str(self.jid)) + " starting...")

        ## Behaviours
        self.info = self.Info()
        self.add_behaviour(self.info)
    

    class Info(CyclicBehaviour):
        async def run(self):
            ## esperar pela msg da torre com informação dos voos
            msg = await self.receive(timeout=10)
            
            if msg:
                performative = msg.get_metadata('performative')

                if performative == 'global_info':
                    received = jsonpickle.decode(msg.body)
                    printInfo(received)