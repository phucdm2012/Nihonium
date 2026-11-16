from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from qfluentwidgets_pro import *
from qfluentwidgets_pro.window.fluent_window import *
from qfluentwidgets_pro.components.widgets.line_edit import *
from qfluentwidgets_pro.components.widgets.scroll_area import *
from qfluentwidgets_pro.components.widgets.card_widget import *
from typing import List
from pathlib import Path

from ....core.searchFriend import SearchFriend

CURRENT_PATH = Path(__file__)
RESOUCE_PATH = CURRENT_PATH.parent / "resouces"


class FriendsBar(CardWidget):
    blurFilterPath = RESOUCE_PATH / "blur.svg"
    searchFriendCore = SearchFriend()
    friendsSearchResult: List[dict]

    def __init__(self, friends: List[dict], parent=None):
        super().__init__(parent)
        self.initFriendsBar()

    def initFriendsBar(self):
        self.friendsBarLayout = QGridLayout(self)
        self.friendsBarLayout.setContentsMargins(0, 0, 0, 0)

        self.friendsBarScroll = ScrollArea(self)
        self.friendsBarLayout.addWidget(self.friendsBarScroll, 0, 0)

        self.createSearch()
        self.friendsBarLayout.addWidget(
            self.friendsSearchWidget, 0, 0, Qt.AlignmentFlag.AlignTop
        )
        self.friendsSearchWidget.raise_()

    def createSearch(self):
        self.friendsSearchWidget = QWidget(self)
        self.friendsSearchLayout = QHBoxLayout()
        self.customFriendsSearchWidget()

        self.searchEntry = LineEdit()
        self.searchEntry.textChanged.connect(self.searchFriendCore.search())

        self.friendsSearchLayout.addWidget(self.searchEntry)
        self.friendsSearchWidget.setLayout(self.friendsSearchLayout)

    def searchEntryTextChanged(self):
        prompt = self.searchEntry.text()
        self.searchFriendCore.search(prompt)
        self.friendsSearchResult = self.searchFriendCore.getSearchedList()
        #refreshFriendsList

    def customFriendsSearchWidget(self):
        self.friendsSearchWidget.setFixedHeight(49)
        self.friendsSearchWidget.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        self.blurFriendsSearchWidget()

    def blurFriendsSearchWidget(self):
        self.friendsSearchWidget.setStyleSheet(
            f"""
            background-image: {self.blurFilterPath};
            background-repeat: repeat;
            """
        )

    def createFriendsList(self):
        ...
