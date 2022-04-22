class Television:
    """
    Class to represent the television objects.
    """
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self) -> None:
        """
        Method to set the default state of the TV.
        """
        self.__tv_channel: int = Television.MIN_CHANNEL
        self.__tv_volume: int = Television.MIN_VOLUME
        self.__tv_status: bool = False

    def power(self) -> None:
        """
        Method to turn TV on/off.
        """
        if not self.__tv_status:
            self.__tv_status = True
        else:
            self.__tv_status = False

    def channel_up(self) -> None:
        """
        Method to turn the TV channel up.
        """
        if self.__tv_status and self.__tv_channel < Television.MAX_CHANNEL:
            self.__tv_channel += 1
        elif self.__tv_status and self.__tv_channel == Television.MAX_CHANNEL:
            self.__tv_channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to turn the TV channel down.
        """
        if self.__tv_status and self.__tv_channel > Television.MIN_CHANNEL:
            self.__tv_channel -= 1
        elif self.__tv_status and self.__tv_channel == Television.MIN_CHANNEL:
            self.__tv_channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to turn the TV volume up.
        """
        if self.__tv_status and self.__tv_volume < Television.MAX_VOLUME:
            self.__tv_volume += 1
        elif self.__tv_status and self.__tv_volume == Television.MAX_VOLUME:
            self.__tv_volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        Method to turn the TV volume down.
        """
        if self.__tv_status and self.__tv_volume > Television.MIN_VOLUME:
            self.__tv_volume -= 1
        elif self.__tv_status and self.__tv_volume == Television.MIN_VOLUME:
            self.__tv_volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        return f"TV status: Is on = {self.__tv_status}, Channel = {self.__tv_channel}, Volume = {self.__tv_volume}"
