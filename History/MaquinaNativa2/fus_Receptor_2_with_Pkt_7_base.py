#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: fus_Receptor_2_with_Pkt_7_base
# GNU Radio version: 3.9.5.0

from distutils.version import StrictVersion

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

class fus_Receptor_2_with_Pkt_7_base(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "fus_Receptor_2_with_Pkt_7_base", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("fus_Receptor_2_with_Pkt_7_base")
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

        self.settings = Qt.QSettings("GNU Radio", "fus_Receptor_2_with_Pkt_7_base")

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
        self.samp_rate = samp_rate = 1562500
        self.num_key = num_key = "packet_num"
        self.len_key = len_key = "packet_len"
        self.decimation = decimation = 4
        self.samp_rate_3 = samp_rate_3 = 480000
        self.samp_rate_2 = samp_rate_2 = samp_rate/decimation
        self.hdr_format = hdr_format = digital.header_format_crc(len_key, num_key)
        self.h = h = 1
        self.amplificador = amplificador = 100

        ##################################################
        # Blocks
        ##################################################
        self._amplificador_range = Range(0, 200, 10, 100, 200)
        self._amplificador_win = RangeWidget(self._amplificador_range, self.set_amplificador, "'amplificador'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._amplificador_win)
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
        self.Widget.addTab(self.Widget_widget_1, 'Señal binaria?')
        self.Widget_widget_2 = Qt.QWidget()
        self.Widget_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Widget_widget_2)
        self.Widget_grid_layout_2 = Qt.QGridLayout()
        self.Widget_layout_2.addLayout(self.Widget_grid_layout_2)
        self.Widget.addTab(self.Widget_widget_2, 'Analizador de espectro')
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
        # No synchronization enforced.

        self.uhd_usrp_source_0.set_center_freq(830e6, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0.set_bandwidth(200e3, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decimation,
                taps=[],
                fractional_bw=0)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            1024, #size
            samp_rate_2, #samp_rate
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
        self.digital_protocol_parser_b_0 = digital.protocol_parser_b(hdr_format)
        self.digital_header_payload_demux_0 = digital.header_payload_demux(
            32,
            1,
            0,
            "packet_len",
            "packet_len",
            False,
            gr.sizeof_char,
            "burst",
            int(samp_rate),
            (),
            0)
        self.digital_crc32_async_bb_0 = digital.crc32_async_bb(True)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(2, 2, 0)
        self.blocks_tagged_stream_to_pdu_0 = blocks.tagged_stream_to_pdu(blocks.byte_t, 'packet_len')
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_char*1, '', "")
        self.blocks_tag_debug_0.set_display(True)
        self.blocks_repack_bits_bb_1 = blocks.repack_bits_bb(1, 8, "packet_len", False, gr.GR_MSB_FIRST)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(amplificador)
        self.blocks_message_debug_1 = blocks.message_debug(True)
        self.blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_float, 1, 8, 0)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 3*samp_rate)
        self.blocks_complex_to_magphase_0 = blocks.complex_to_magphase(1)
        self.band_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.band_pass(
                1,
                samp_rate/decimation,
                10000,
                50000,
                50000,
                window.WIN_HAMMING,
                6.76))


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0, 'pdus'), (self.digital_crc32_async_bb_0, 'in'))
        self.msg_connect((self.digital_crc32_async_bb_0, 'out'), (self.blocks_message_debug_1, 'print'))
        self.msg_connect((self.digital_protocol_parser_b_0, 'info'), (self.digital_header_payload_demux_0, 'header_data'))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_complex_to_magphase_0, 0))
        self.connect((self.blocks_complex_to_magphase_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_complex_to_magphase_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.blocks_complex_to_magphase_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_delay_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.digital_header_payload_demux_0, 0))
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_repack_bits_bb_1, 0), (self.blocks_tag_debug_0, 0))
        self.connect((self.blocks_repack_bits_bb_1, 0), (self.blocks_tagged_stream_to_pdu_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_keep_m_in_n_0, 0))
        self.connect((self.digital_header_payload_demux_0, 1), (self.blocks_repack_bits_bb_1, 0))
        self.connect((self.digital_header_payload_demux_0, 0), (self.digital_protocol_parser_b_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_delay_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fus_Receptor_2_with_Pkt_7_base")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samp_rate_2(self.samp_rate/self.decimation)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate/self.decimation, 10000, 50000, 50000, window.WIN_HAMMING, 6.76))
        self.blocks_delay_0.set_dly(3*self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_num_key(self):
        return self.num_key

    def set_num_key(self, num_key):
        self.num_key = num_key
        self.set_hdr_format(digital.header_format_crc(self.len_key, self.num_key))

    def get_len_key(self):
        return self.len_key

    def set_len_key(self, len_key):
        self.len_key = len_key
        self.set_hdr_format(digital.header_format_crc(self.len_key, self.num_key))

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation
        self.set_samp_rate_2(self.samp_rate/self.decimation)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate/self.decimation, 10000, 50000, 50000, window.WIN_HAMMING, 6.76))

    def get_samp_rate_3(self):
        return self.samp_rate_3

    def set_samp_rate_3(self, samp_rate_3):
        self.samp_rate_3 = samp_rate_3

    def get_samp_rate_2(self):
        return self.samp_rate_2

    def set_samp_rate_2(self, samp_rate_2):
        self.samp_rate_2 = samp_rate_2
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate_2)

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format

    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h

    def get_amplificador(self):
        return self.amplificador

    def set_amplificador(self, amplificador):
        self.amplificador = amplificador
        self.blocks_multiply_const_vxx_0.set_k(self.amplificador)




def main(top_block_cls=fus_Receptor_2_with_Pkt_7_base, options=None):

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
