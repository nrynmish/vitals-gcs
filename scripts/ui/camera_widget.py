from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtMultimedia import QCamera, QMediaCaptureSession
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import Qt

class CameraWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.video_widget = QVideoWidget()
        self.video_widget.setAspectRatioMode(Qt.KeepAspectRatio)
        self.video_widget.setStyleSheet("""
            background:#2a2a2a;
            border-radius:16px;
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.video_widget)

        self.camera = QCamera()
        self.capture = QMediaCaptureSession()
        self.capture.setCamera(self.camera)
        self.capture.setVideoOutput(self.video_widget)

        self.camera.start()

    def closeEvent(self, event):
        if self.camera.isActive():
            self.camera.stop()
        event.accept()