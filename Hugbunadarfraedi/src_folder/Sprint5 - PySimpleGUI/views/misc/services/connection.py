import asyncio
import websockets
import json

"""
Connection contains the actions necessary to communicate to the server 
and get a response back.
"""
class Connection:
    def __init__(self):
        # The address of the server
        self.addr = "ws://websock.alexfreyr.com:12789"

    """
    Performs the call to the server asynchronously

    @param 'dict_action' contains the dictionary that will be sent to the server
    @return <'dict'> the information returned by the server
    """
    def execute(self, dict_action):
        return asyncio.get_event_loop().run_until_complete(self._send(dict_action))

    """ 
    Sends a dictionary over to the server which then returns the requested information

    @param 'dict_action' contains the operation that the server performs and any data necessary
    @returns <'dict'> the information returned by the server
    """
    async def _send(self, dict_action):
        return_val = ""
        try:
            async with websockets.connect(self.addr) as websocket:
                await websocket.send(json.dumps(dict_action))
                return_val = await websocket.recv()
        except Exception as e:
            print("Server raised an error: " + str(e))
            return "Error"
        
        try:
            return json.loads(return_val)
        except:
            return return_val