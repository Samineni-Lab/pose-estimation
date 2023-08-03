import os
from pathlib import Path

from PySide6 import QtWidgets
from PySide6.QtCore import Qt

from deeplabcut.gui.components import (
    DefaultTab,
    VideoSelectionWidget,
    _create_grid_layout,
    _create_label_widget,
    _create_horizontal_layout
)
from deeplabcut.gui.dlc_params import DLCParams

from aniposelib.boards import CalibrationObject, Checkerboard, CharucoBoard


class Calibrate(DefaultTab):

    def __init__(self, root, parent, h1_description):
        super(Calibrate, self).__init__(root, parent, h1_description)
        self._set_page()

    @property
    def files(self):
        return self.video_selection_widget.files

    def _set_page(self):
        self.main_layout.addWidget(_create_label_widget("Video Selection", "font:bold"))
        self.layout_video_setup = _create_horizontal_layout()
        self._generate_layout_video_setup(self.layout_video_setup)
        self.main_layout.addLayout(self.layout_video_setup)

        self.main_layout.addWidget(_create_label_widget("Attributes", "font:bold"))
        self.layout_attributes = _create_grid_layout(margins=(20, 0, 0, 0))
        self._generate_layout_attributes(self.layout_attributes)
        self.main_layout.addLayout(self.layout_attributes)

        self.calibrate_button = QtWidgets.QPushButton("Calibrate")
        self.calibrate_button.setMinimumWidth(150)
        self.calibrate_button.clicked.connect(self._calibrate)

        self.main_layout.addWidget(self.calibrate_button, alignment=Qt.AlignRight)

    def _generate_layout_video_setup(self, layout: QtWidgets.QHBoxLayout):
        self.video_selection_widget = VideoSelectionWidget(self.root, self)

        camera_name_label = QtWidgets.QLabel("Camera Name Regex")

        self.cam_regex = QtWidgets.QLineEdit("Cam([A-Z])")

        layout.addWidget(self.video_selection_widget)
        layout.addWidget(camera_name_label)
        layout.addWidget(self.cam_regex)

    def _generate_layout_attributes(self, layout: QtWidgets.QGridLayout):

        type_label = QtWidgets.QLabel("Board type")

        self.board_type = QtWidgets.QComboBox()
        self.board_type.addItems(DLCParams.CALIBRATION_BOARDS)
        self.board_type.setCurrentText("ChArUco")
        self.board_type.currentTextChanged.connect(self._board_type_changed)
        self.board_type.currentTextChanged.connect(self.log_board_type_choice)

        width_label = QtWidgets.QLabel("Board width (squares)")

        self.board_width = QtWidgets.QSpinBox()
        self.board_width.setValue(7)

        height_label = QtWidgets.QLabel("Board height (squares)")

        self.board_height = QtWidgets.QSpinBox()
        self.board_height.setValue(10)

        for spinbox in self.board_width, self.board_height:
            spinbox.setRange(1, 100)  # very unlikely that board dimensions will even be close to 100

        square_length_label = QtWidgets.QLabel("Square side length (mm)")

        self.square_length = QtWidgets.QSpinBox()
        self.square_length.setRange(1, 1000000)
        self.square_length.setValue(15)

        marker_length_label = QtWidgets.QLabel("ArUco Marker Length (mm)")

        self.marker_length = QtWidgets.QSpinBox()
        self.marker_length.setRange(1, 1000000)
        self.marker_length.setValue(12)

        bits_label = QtWidgets.QLabel("ArUco marker bits")

        self.marker_bits = QtWidgets.QComboBox()
        self.marker_bits.addItems(list(map(str, range(4, 8))))
        self.marker_bits.setCurrentText("4")

        dict_size_label = QtWidgets.QLabel("ArUco dictionary size")

        self.dict_size = QtWidgets.QComboBox()
        self.dict_size.addItems(["50", "100", "250", "1000"])
        self.dict_size.setCurrentText("50")

        layout.addWidget(type_label, 0, 0)
        layout.addWidget(self.board_type, 0, 1)
        layout.addWidget(square_length_label, 1, 0)
        layout.addWidget(self.square_length, 1, 1)
        layout.addWidget(width_label, 1, 2)
        layout.addWidget(self.board_width, 1, 3)
        layout.addWidget(height_label, 1, 4)
        layout.addWidget(self.board_height, 1, 5)
        layout.addWidget(marker_length_label, 2, 0)
        layout.addWidget(self.marker_length, 2, 1)
        layout.addWidget(bits_label, 2, 2)
        layout.addWidget(self.marker_bits, 2, 3)
        layout.addWidget(dict_size_label, 2, 4)
        layout.addWidget(self.dict_size, 2, 5)

    def _calibrate(self):
        """Run calibration"""

        # TODO: needs implementation

        board: CalibrationObject

        if self.board_type.currentText() == "ChArUco":
            pass
            # board = CharucoBoard()
        else:  # checkerboard
            pass
            # board = Checkerboard()

        pass

    def _board_type_changed(self, board_type):
        """Changes what attributes are enabled based on board type."""
        widgets = [self.marker_bits, self.marker_length, self.dict_size]
        enable = board_type == "ChArUco"

        for w in widgets:
            w.setEnabled(enable)

    def log_board_type_choice(self, board_type: str):
        self.root.logger.info(f"Board type set to {board_type}")

    # TODO: more loggers? (check other tab for reference)
