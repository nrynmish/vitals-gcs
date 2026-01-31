from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt

class ControlPanel(QWidget):
    def __init__(self, mav):
        super().__init__()
        self.mav = mav

        self.setStyleSheet("""
            QWidget {
                background:#111;
                border-radius:14px;
            }
            QPushButton {
                background:#2a82da;
                color:white;
                border-radius:10px;
                padding:12px;
                font-size:14px;
            }
        """)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(14,14,14,14)
        layout.setSpacing(12)
        layout.setAlignment(Qt.AlignCenter)

        self.camera_idx = 0
        self.camera_states = [
            (500, "Camera 90°"),
            (950, "Camera 45°"),
            (1400, "Camera 0°"),
        ]

        self.servo2 = False
        self.mode_idx = 0
        self.modes = ["STABILIZE", "LOITER", "ALT_HOLD"]

        self.camera_btn = QPushButton("Camera 0°")
        self.camera_btn.clicked.connect(self.cycle_camera)

        self.servo2_btn = QPushButton("Gripper")
        self.servo2_btn.setCheckable(True)
        self.servo2_btn.clicked.connect(self.toggle_servo2)

        self.mode_btn = QPushButton("STABILIZE")
        self.mode_btn.clicked.connect(self.cycle_mode)

        layout.addWidget(self.camera_btn)
        layout.addWidget(self.servo2_btn)
        layout.addWidget(self.mode_btn)

    def cycle_camera(self):
        self.camera_idx = (self.camera_idx + 1) % 3
        pwm, label = self.camera_states[self.camera_idx]
        self.camera_btn.setText(label)
        self.mav.set_servo(6, pwm)

    def toggle_servo2(self):
        self.servo2 = not self.servo2
        pwm = 1900 if self.servo2 else 1100
        self.mav.set_servo(8, pwm)

    def cycle_mode(self):
        self.mode_idx = (self.mode_idx + 1) % 3
        mode = self.modes[self.mode_idx]
        self.mode_btn.setText(mode)
        self.mav.set_mode(mode)
