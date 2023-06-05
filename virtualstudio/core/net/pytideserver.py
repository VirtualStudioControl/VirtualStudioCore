from config import EVENT_SERVER_PORT
from pytidenetworking.message import Message, create as createMessage, MessageSendMode
from pytidenetworking.server import Server
from pytidenetworking.threading.fixedupdatethreads import FixedUpdateThread
from pytidenetworking.transports.tcp.tcp_server import TCPServer

from typing import TYPE_CHECKING

from virtualstudio.common.logging import logengine
from virtualstudio.core.net.eventmessages.eventmessagetypes import *

if TYPE_CHECKING:
    from virtualstudio.common.structs.hardware.hardware_wrapper import HardwareWrapper

server: Server = None
serverUpdater: FixedUpdateThread = None

logger = logengine.getLogger()

def runServer():
    global server, serverUpdater
    tcpTransport = TCPServer()
    server = Server(tcpTransport)
    server.start(EVENT_SERVER_PORT, 10)

    serverUpdater = FixedUpdateThread(server.update)
    serverUpdater.start()

def stopServer():
    server.stop()
    serverUpdater.requestClose()
    serverUpdater.join(5)
    logger.info("Stopped PyTide Server with Port {}".format(EVENT_SERVER_PORT))


def addHardwareWrapperToMsg(msg: Message, hardware: 'HardwareWrapper'):
    msg.addString(hardware.manufacturer)
    msg.addString(hardware.name)
    msg.addString(hardware.label)


def sendProfileChange(profileName: str, device: 'HardwareWrapper'):
    msg: Message = createMessage(MessageSendMode.Unreliable, EVENT_MESSAGE_PROFILE_CHANGE)
    addHardwareWrapperToMsg(msg, device)
    msg.addString(profileName)
    if server is not None:
        server.sendToAll(msg)


def sendButtonPress(contorlID: int, device: 'HardwareWrapper'):
    msg: Message = createMessage(MessageSendMode.Unreliable, EVENT_MESSAGE_BUTTON_PRESS)
    addHardwareWrapperToMsg(msg, device)
    msg.addInt(contorlID)
    if server is not None:
        server.sendToAll(msg)


def sendButtonRelease(contorlID: int, device: 'HardwareWrapper'):
    msg: Message = createMessage(MessageSendMode.Unreliable, EVENT_MESSAGE_BUTTON_RELEASE)
    addHardwareWrapperToMsg(msg, device)
    msg.addInt(contorlID)
    if server is not None:
        server.sendToAll(msg)


def sendFaderTouchBegin(contorlID: int, device: 'HardwareWrapper'):
    msg: Message = createMessage(MessageSendMode.Unreliable, EVENT_MESSAGE_FADER_TOUCH_BEGIN)
    addHardwareWrapperToMsg(msg, device)
    msg.addInt(contorlID)
    if server is not None:
        server.sendToAll(msg)


def sendFaderTouchEnd(contorlID: int, device: 'HardwareWrapper'):
    msg: Message = createMessage(MessageSendMode.Unreliable, EVENT_MESSAGE_FADER_TOUCH_END)
    addHardwareWrapperToMsg(msg, device)
    msg.addInt(contorlID)
    if server is not None:
        server.sendToAll(msg)


def sendFaderValueChange(value: int, contorlID: int, device: 'HardwareWrapper'):
    msg: Message = createMessage(MessageSendMode.Unreliable, EVENT_MESSAGE_FADER_VALUE_CHANGE)
    addHardwareWrapperToMsg(msg, device)
    msg.addInt(contorlID)
    msg.addInt(value)
    if server is not None:
        server.sendToAll(msg)


def sendRotaryEncoderPress(contorlID: int, device: 'HardwareWrapper'):
    msg: Message = createMessage(MessageSendMode.Unreliable, EVENT_MESSAGE_ROTARY_ENCODER_PRESS)
    addHardwareWrapperToMsg(msg, device)
    msg.addInt(contorlID)
    if server is not None:
        server.sendToAll(msg)


def sendRotaryEncoderRelease(contorlID: int, device: 'HardwareWrapper'):
    msg: Message = createMessage(MessageSendMode.Unreliable, EVENT_MESSAGE_ROTARY_ENCODER_RELEASE)
    addHardwareWrapperToMsg(msg, device)
    msg.addInt(contorlID)
    if server is not None:
        server.sendToAll(msg)


def sendRotaryEncoderValueChange(value: int, contorlID: int, device: 'HardwareWrapper'):
    msg: Message = createMessage(MessageSendMode.Unreliable, EVENT_MESSAGE_ROTARY_ENCODER_VALUE_CHANGE)
    addHardwareWrapperToMsg(msg, device)
    msg.addInt(contorlID)
    msg.addInt(value)
    if server is not None:
        server.sendToAll(msg)
