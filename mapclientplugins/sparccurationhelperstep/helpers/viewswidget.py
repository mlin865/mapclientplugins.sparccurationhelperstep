import csv
import json
import os.path

from PySide2 import QtCore, QtGui, QtWidgets
from mapclientplugins.sparccurationhelperstep.helpers.ui_viewswidget import Ui_ViewsWidget


class ViewsWidget(QtWidgets.QWidget):

    sample_changed = QtCore.Signal(str)

    def __init__(self, samples, annotations=None, parent=None):
        super(ViewsWidget, self).__init__(parent)
        self._ui = Ui_ViewsWidget()
        self._ui.setupUi(self)
        
        self._previous_location = QtCore.QDir.homePath()

        m = self._ui.comboBoxSample.model()
        for sample in samples:
            m.appendRow(QtGui.QStandardItem(sample))

        if annotations is not None:
            self.add_annotations(annotations)

        self._make_connections()

    def _make_connections(self):
        self._ui.pushButtonThumbnailFile.clicked.connect(self._open_thumbnail_file)
        self._ui.pushButtonViewFile.clicked.connect(self._open_view_file)
        self._ui.comboBoxSample.currentTextChanged.connect(self.sample_changed)

    def set_sample(self, sample):
        self._ui.comboBoxSample.blockSignals(True)
        self._ui.comboBoxSample.setCurrentText(sample)
        self._ui.comboBoxSample.blockSignals(False)

    def as_dict(self, header):
        return {
            "annotation": self._ui.comboBoxAnnotation.currentText(),
            "id": header,
            "path": self._ui.lineEditPath.text(),
            "sample": self._ui.comboBoxSample.currentText(),
            "thumbnail": self._ui.lineEditThumbnail.text(),
        }

    def add_annotations(self, annotations):
        m = self._ui.comboBoxAnnotation.model()
        existing_annotations = []
        for r in range(m.rowCount()):
            item = m.item(r)
            existing_annotations.append(item.text())

        for annotation in annotations:
            if annotation[0] not in existing_annotations:
                item = QtGui.QStandardItem(annotation[0])
                item.setToolTip(annotation[1])
                m.appendRow(item)

    def add_sample(self, sample):
        m = self._ui.comboBoxSample.model()
        item = QtGui.QStandardItem(sample)
        m.appendRow(item)

    def remove_sample(self, sample):
        m = self._ui.comboBoxSample.model()
        remove_row = None
        for r in range(m.rowCount()):
            item = m.item(r)
            if item.text() == sample:
                remove_row = r

        if remove_row is not None:
            if self._ui.comboBoxSample.currentIndex() == remove_row:
                self._ui.comboBoxSample.setCurrentIndex(0)
            m.takeRow(remove_row)

    def _open_view_file(self):
        self._open_file(self._ui.lineEditPath)

    def _open_thumbnail_file(self):
        self._open_file(self._ui.lineEditThumbnail)

    def _open_file(self, line_editor):
        result = QtWidgets.QFileDialog.getOpenFileName(self, "Open annotation map file", self._previous_location)
        file_name = result[0]
        if file_name:
            self._previous_location = os.path.dirname(file_name)
            with open(file_name) as f:
                # check if it's view/thumbnail file
                line_editor.setText(file_name)