#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Jul 13 09:38:26 2022
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import math
import numpy
import sip
import sys
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.constellation_2 = constellation_2 = (0,1)
        self.module = module = constellation_2
        self.Sps = Sps = 8
        self.Rs = Rs = 48828.125
        self.M = M = len(module)
        self.samp_rate = samp_rate = Rs*Sps
        self.bps = bps = int(math.log(M,2))
        self.samp_rate_2 = samp_rate_2 = samp_rate*16
        self.h = h = [1]*Sps
        self.TrueBoardConstellation = TrueBoardConstellation = (0.77+0.77j,-0.77+0.77j,-0.77-0.77j,0.77-0.77j)
        self.Sps_0 = Sps_0 = int(Sps/2)
        self.Rb = Rb = Rs*bps

        ##################################################
        # Blocks
        ##################################################
        self._module_options = (TrueBoardConstellation, constellation_2, )
        self._module_labels = ('TrueBoardConstellation', 'constellation_2', )
        self._module_group_box = Qt.QGroupBox('Modulaci\xc3\xb3n')
        self._module_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._module_button_group = variable_chooser_button_group()
        self._module_group_box.setLayout(self._module_box)
        for i, label in enumerate(self._module_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._module_box.addWidget(radio_button)
        	self._module_button_group.addButton(radio_button, i)
        self._module_callback = lambda i: Qt.QMetaObject.invokeMethod(self._module_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._module_options.index(i)))
        self._module_callback(self.module)
        self._module_button_group.buttonClicked[int].connect(
        	lambda i: self.set_module(self._module_options[i]))
        self.top_grid_layout.addWidget(self._module_group_box, 0, 7, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(0,1)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(7,8)]
        self.Widget = Qt.QTabWidget()
        self.Widget_widget_0 = Qt.QWidget()
        self.Widget_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Widget_widget_0)
        self.Widget_grid_layout_0 = Qt.QGridLayout()
        self.Widget_layout_0.addLayout(self.Widget_grid_layout_0)
        self.Widget.addTab(self.Widget_widget_0, 'PHG')
        self.Widget_widget_1 = Qt.QWidget()
        self.Widget_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Widget_widget_1)
        self.Widget_grid_layout_1 = Qt.QGridLayout()
        self.Widget_layout_1.addLayout(self.Widget_grid_layout_1)
        self.Widget.addTab(self.Widget_widget_1, 'Antes de Chunks')
        self.Widget_widget_2 = Qt.QWidget()
        self.Widget_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Widget_widget_2)
        self.Widget_grid_layout_2 = Qt.QGridLayout()
        self.Widget_layout_2.addLayout(self.Widget_grid_layout_2)
        self.Widget.addTab(self.Widget_widget_2, 'Despu\xc3\xa9s de Chunks')
        self.Widget_widget_3 = Qt.QWidget()
        self.Widget_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Widget_widget_3)
        self.Widget_grid_layout_3 = Qt.QGridLayout()
        self.Widget_layout_3.addLayout(self.Widget_grid_layout_3)
        self.Widget.addTab(self.Widget_widget_3, 'Se\xc3\xb1al Interpolada')
        self.Widget_widget_4 = Qt.QWidget()
        self.Widget_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Widget_widget_4)
        self.Widget_grid_layout_4 = Qt.QGridLayout()
        self.Widget_layout_4.addLayout(self.Widget_grid_layout_4)
        self.Widget.addTab(self.Widget_widget_4, 'Diagrama de Constelaciones')
        self.Widget_widget_5 = Qt.QWidget()
        self.Widget_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Widget_widget_5)
        self.Widget_grid_layout_5 = Qt.QGridLayout()
        self.Widget_layout_5.addLayout(self.Widget_grid_layout_5)
        self.Widget.addTab(self.Widget_widget_5, 'Antes de desempaquetar')
        self.top_grid_layout.addWidget(self.Widget, 0, 0, 1, 7)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(0,1)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,7)]
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(830e6, 0)
        self.uhd_usrp_sink_0.set_gain(0, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.qtgui_time_sink_x_2 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"Señal interpolada", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(False)
        self.qtgui_time_sink_x_2.enable_grid(False)
        self.qtgui_time_sink_x_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_2.enable_control_panel(True)
        self.qtgui_time_sink_x_2.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_2.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_2.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_2.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.pyqwidget(), Qt.QWidget)
        self.Widget_layout_3.addWidget(self._qtgui_time_sink_x_2_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"Después de Chunks", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(True)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.Widget_layout_2.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Antes de desempaquetar", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.Widget_layout_5.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"PHG", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.Widget_layout_0.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Antes de Chunks", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.Widget_layout_1.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.Widget_layout_4.addWidget(self._qtgui_const_sink_x_0_win)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(Sps, (h))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_correlate_access_code_xx_ts_0 = digital.correlate_access_code_bb_ts('0000 0100 0001 0100',
          0, 'packet_len')
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((module), 1)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_uchar_to_float_0_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 100, "packet_len")
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_gr_complex*1, Sps)
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/alex/Documents/ProgrammingProject/Melendi - Destino o Casualidad ft. Ha Ash VDownloader.wav', False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/alex/Documents/ProgrammingProject/MaquinaNativa1/cancion.wav', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_correlate_access_code_xx_ts_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_uchar_to_float_0_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_uchar_to_float_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_2, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.uhd_usrp_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_constellation_2(self):
        return self.constellation_2

    def set_constellation_2(self, constellation_2):
        self.constellation_2 = constellation_2
        self.set_module(self.constellation_2)

    def get_module(self):
        return self.module

    def set_module(self, module):
        self.module = module
        self._module_callback(self.module)
        self.digital_chunks_to_symbols_xx_0.set_symbol_table((self.module))
        self.set_M(len(self.module))

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_samp_rate(self.Rs*self.Sps)
        self.set_h([1]*self.Sps)
        self.blocks_keep_one_in_n_0.set_n(self.Sps)
        self.set_Sps_0(int(self.Sps/2))

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_samp_rate(self.Rs*self.Sps)
        self.set_Rb(self.Rs*self.bps)

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_bps(int(math.log(self.M,2)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.set_samp_rate_2(self.samp_rate*16)
        self.qtgui_time_sink_x_2.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_bps(self):
        return self.bps

    def set_bps(self, bps):
        self.bps = bps
        self.set_Rb(self.Rs*self.bps)

    def get_samp_rate_2(self):
        return self.samp_rate_2

    def set_samp_rate_2(self, samp_rate_2):
        self.samp_rate_2 = samp_rate_2

    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h
        self.interp_fir_filter_xxx_0.set_taps((self.h))

    def get_TrueBoardConstellation(self):
        return self.TrueBoardConstellation

    def set_TrueBoardConstellation(self, TrueBoardConstellation):
        self.TrueBoardConstellation = TrueBoardConstellation

    def get_Sps_0(self):
        return self.Sps_0

    def set_Sps_0(self, Sps_0):
        self.Sps_0 = Sps_0

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb


def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
