#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: USRP_RX_2
# Author: proyecto
# GNU Radio version: 3.10.1.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class USRP_RX_2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "USRP_RX_2", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("USRP_RX_2")
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

        self.settings = Qt.QSettings("GNU Radio", "USRP_RX_2")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 8
        self.samp_rate = samp_rate = 3125000
        self.th = th = 0.00075
        self.symbol_rate = symbol_rate = samp_rate/(sps*2)
        self.low = low = 0.0002
        self.high = high = 0.0006
        self.h = h = 1
        self.amplificador = amplificador = 180

        ##################################################
        # Blocks
        ##################################################
        self.Widget = Qt.QTabWidget()
        self.Widget_widget_0 = Qt.QWidget()
        self.Widget_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Widget_widget_0)
        self.Widget_grid_layout_0 = Qt.QGridLayout()
        self.Widget_layout_0.addLayout(self.Widget_grid_layout_0)
        self.Widget.addTab(self.Widget_widget_0, 'Señal cuadrada')
        self.Widget_widget_1 = Qt.QWidget()
        self.Widget_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Widget_widget_1)
        self.Widget_grid_layout_1 = Qt.QGridLayout()
        self.Widget_layout_1.addLayout(self.Widget_grid_layout_1)
        self.Widget.addTab(self.Widget_widget_1, 'Señal decimada')
        self.Widget_widget_2 = Qt.QWidget()
        self.Widget_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Widget_widget_2)
        self.Widget_grid_layout_2 = Qt.QGridLayout()
        self.Widget_layout_2.addLayout(self.Widget_grid_layout_2)
        self.Widget.addTab(self.Widget_widget_2, 'Diagrama de constelaciones')
        self.Widget_widget_3 = Qt.QWidget()
        self.Widget_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Widget_widget_3)
        self.Widget_grid_layout_3 = Qt.QGridLayout()
        self.Widget_layout_3.addLayout(self.Widget_grid_layout_3)
        self.Widget.addTab(self.Widget_widget_3, 'Señal Recibida Absoluta')
        self.Widget_widget_4 = Qt.QWidget()
        self.Widget_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Widget_widget_4)
        self.Widget_grid_layout_4 = Qt.QGridLayout()
        self.Widget_layout_4.addLayout(self.Widget_grid_layout_4)
        self.Widget.addTab(self.Widget_widget_4, 'Señal Recibida')
        self.top_layout.addWidget(self.Widget)
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)

        self.uhd_usrp_source_0.set_center_freq(830e6, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_source_0.set_bandwidth(200e3, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            'Señal Recibida Absoluta', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1.enable_grid(True)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(True)
        self.qtgui_time_sink_x_1.enable_stem_plot(True)


        labels = ['Señal Recibida', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.qwidget(), Qt.QWidget)
        self.Widget_layout_3.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            'Señal Cuadrada', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['Señal cuadrada', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.qwidget(), Qt.QWidget)
        self.Widget_layout_0.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            'Señal decimada filtrada', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(True)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.Widget_layout_1.addWidget(self._qtgui_time_sink_x_0_win)
        self.digital_crc32_bb_0 = digital.crc32_bb(False, "packet_len", True)
        self.digital_correlate_access_code_xx_ts_0 = digital.correlate_access_code_bb_ts('11001100101001010100110111110101',
          0, 'packet_len')
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(sps*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.125)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(low, high, 0)
        self.blocks_tagged_stream_align_0 = blocks.tagged_stream_align(gr.sizeof_char*1, 'packet_len')
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/proyecto/Documents/ProgrammingProject/MaquinaNativa2/encrypted_data_r.bin', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                500,
                samp_rate/4,
                samp_rate/4,
                window.WIN_HAMMING,
                6.76))
        self._amplificador_range = Range(0, 1000, 10, 180, 200)
        self._amplificador_win = RangeWidget(self._amplificador_range, self.set_amplificador, "'amplificador'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._amplificador_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.digital_correlate_access_code_xx_ts_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_crc32_bb_0, 0))
        self.connect((self.blocks_tagged_stream_align_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0, 0), (self.blocks_tagged_stream_align_0, 0))
        self.connect((self.digital_crc32_bb_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_complex_to_mag_squared_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "USRP_RX_2")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_symbol_rate(self.samp_rate/(self.sps*2))
        self.digital_clock_recovery_mm_xx_0.set_omega(self.sps*(1+0.0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_symbol_rate(self.samp_rate/(self.sps*2))
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 500, self.samp_rate/4, self.samp_rate/4, window.WIN_HAMMING, 6.76))
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_th(self):
        return self.th

    def set_th(self, th):
        self.th = th

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate

    def get_low(self):
        return self.low

    def set_low(self, low):
        self.low = low
        self.blocks_threshold_ff_0.set_lo(self.low)

    def get_high(self):
        return self.high

    def set_high(self, high):
        self.high = high
        self.blocks_threshold_ff_0.set_hi(self.high)

    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h

    def get_amplificador(self):
        return self.amplificador

    def set_amplificador(self, amplificador):
        self.amplificador = amplificador




def main(top_block_cls=USRP_RX_2, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
