class OpeningMessage:
    """
    Class imported by main.py,
    executed right after the start of the execution of main.py
    message display, and importing cards.csv
    """

    def __init__(self, filename="TarotAI/BeforetheExecution.txt"):
        """
        defining the filename that will be used.
        """
        self.__filename = filename

    def open_file(self):
        """
        open the file that is defined in __init__
        return the content to the variable 'msg'
        """
        opening_message = open(self.__filename, "r")
        msg = opening_message.read()
        return msg

    def close_file(self):
        """
        verifying that the file is closed
        """
        open(self.__filename, "r").close()
