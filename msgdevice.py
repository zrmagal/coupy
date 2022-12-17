from abc import ABC, abstractmethod
from typing import Type

class MsgDev:
    """
    Base class of message device.
    """
    ###########################################################################
    def write(self, req: str) -> None:
        """
        Abstract method to write into the device to communicate with players
        :req: string to be sent
        """
        print(req)
    
    ###########################################################################
    def read(self) -> str:
        """
        Abstract method to receive from the device to communicate with players
        """
        return input()
    
    ###########################################################################
    def ask(self, req: str) -> str:
        """
        Method that sends a message and receives the response
        :req: string to be sent
        :return: This methods returns the received message
        """
        self.write(req)
        return self.read()
