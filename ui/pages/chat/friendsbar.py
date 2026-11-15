from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from qfluentwidgets_pro import *
from qfluentwidgets_pro.window.fluent_window import *
from qfluentwidgets_pro.components.widgets.scroll_area import *
from qfluentwidgets_pro.components.widgets.card_widget import *
from typing import List


class FriendsBar(CardWidget):
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
        self.friendsSearchWidget.setFixedHeight(49)
        self.friendsSearchWidget.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )

    def createFriendsList(self):
        ...
