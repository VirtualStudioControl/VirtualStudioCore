import json

from virtualstudio.common.net.tcp_server import TCPServer
from virtualstudio.common.net.protocols.virtualstudiocom.constants import *
from .requesthandlers.devicerequesthandlers import *


class ComServer (TCPServer):

    def __init__(self, listenAddress="", port=4400):
        super().__init__(listenAddress, port)
        self.requestHandler = {}
        self.loadRequestHandlers()

    def loadRequestHandlers(self):
        self.addRequestHandler(REQ_DEVICE_LIST, onSendDeviceList)

    def addRequestHandler(self, request, handler):
        self.requestHandler[request] = handler

    def onMessageRecv(self, message: bytes):
        msg = json.loads(message.decode("utf-8"))
        if msg is None:
            return

        msg_id = msg[INTERN_MESSAGE_ID]
        response = None
        print(msg)
        print(self.requestHandler)
        if msg[INTERN_REQUEST_TYPE] in self.requestHandler.keys():
            print("Generating Response")
            response = self.requestHandler[msg[INTERN_REQUEST_TYPE]](msg)

        if response is not None:
            response[INTERN_MESSAGE_ID] = msg_id
            self.sendMessageJSON(response)

    def sendMessageJSON(self, message: dict):
        content = json.dumps(message)
        self.sendMessage(content.encode("utf-8"))
