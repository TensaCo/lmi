from pydantic import BaseModel
from lmi.components.MenuList import MenuList


class ComboBox(MenuList):
    multiple_select: bool

    # TODO
