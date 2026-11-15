from qfluentwidgets_pro import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class FriendCard(CardWidget):
    def __init__(self, parent = None, avatar: QPixmap = None, name: str = None, recentMessage: str = None):
        super().__init__(parent)
        self.avatar = avatar
        self.name = name
        self.recentMessage = recentMessage
        self.initFriendCard()

    def initFriendCard(self):
        self.createFriendCardLayout()
        self.createAvatar()
        self.createDetail()

    def createFriendCardLayout(self):
        self.friendCardLayout = QHBoxLayout()
        self.setLayout(self.friendCardLayout)

    def createAvatar(self):
        if self.avatar:
            self.avatarWidget = ImageLabel(self.avatar)
        else:
            self.avatarWidget = CirclePersonalInfoSkeleton()
        self.friendCardLayout.addWidget(self.avatarWidget)

    def createDetail(self):
        if self.name or self.recentMessage:
            self.detailWidget = QWidget()
            self.detailLayout = QVBoxLayout()

            if self.name:
                self.userNameLabel = TitleLabel(self.name)
                self.detailLayout.addWidget(self.userNameLabel)

            if self.recentMessageWidget:
                self.recentMessageWidget = SubtitleLabel(self.recentMessage)
                self.detailLayout.addWidget(self.recentMessageWidget)

            self.detailWidget.setLayout(self.detailLayout)
            self.friendCardLayout.addWidget(self.detailWidget)
        else:
            self.detailWidget = SkeletonWidget()
            self.detailLayout.addWidget(SkeletonWidget)
