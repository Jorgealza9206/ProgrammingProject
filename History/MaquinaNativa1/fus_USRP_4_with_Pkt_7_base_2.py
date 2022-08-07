#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: fus_USRP_4_with_Pkt_7_base_2
# Description: https://www.youtube.com/watch?v=2rsu-c26Tqo
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

from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation



from gnuradio import qtgui

class fus_USRP_4_with_Pkt_7_base_2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "fus_USRP_4_with_Pkt_7_base_2", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("fus_USRP_4_with_Pkt_7_base_2")
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

        self.settings = Qt.QSettings("GNU Radio", "fus_USRP_4_with_Pkt_7_base_2")

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
        self.num_key = num_key = "packet_num"
        self.len_key = len_key = "packet_len"
        self.hdr_format = hdr_format = digital.header_format_crc(len_key, num_key)

        ##################################################
        # Blocks
        ##################################################
        self.digital_correlate_access_code_xx_ts_0 = digital.correlate_access_code_bb_ts('11100001010110101110100010010011',
          0, 'packet_len')
        self.blocks_vector_source_x_0 = blocks.vector_source_b((1,1,0,0,1,1,0,0,1,0,1,0,0,1,0,1), True, 1, [])
        self.blocks_unpacked_to_packed_xx_0 = blocks.unpacked_to_packed_bb(1, gr.GR_MSB_FIRST)
        self.blocks_tagged_stream_to_pdu_0 = blocks.tagged_stream_to_pdu(blocks.byte_t, 'packet_len')
        self.blocks_tagged_stream_align_0 = blocks.tagged_stream_align(gr.sizeof_char*1, 'packet_len')
        self.blocks_pdu_to_tagged_stream_2 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_file_sink_1_0 = blocks.file_sink(gr.sizeof_char*1, 'G:\\My Drive\\ProgrammingProject\\MaquinaNativa1\\encrypted_data_rr.bin', False)
        self.blocks_file_sink_1_0.set_unbuffered(False)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0, 'pdus'), (self.blocks_pdu_to_tagged_stream_2, 'pdus'))
        self.connect((self.blocks_pdu_to_tagged_stream_2, 0), (self.blocks_unpacked_to_packed_xx_0, 0))
        self.connect((self.blocks_tagged_stream_align_0, 0), (self.blocks_tagged_stream_to_pdu_0, 0))
        self.connect((self.blocks_unpacked_to_packed_xx_0, 0), (self.blocks_file_sink_1_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.digital_correlate_access_code_xx_ts_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0, 0), (self.blocks_tagged_stream_align_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fus_USRP_4_with_Pkt_7_base_2")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

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

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format




def main(top_block_cls=fus_USRP_4_with_Pkt_7_base_2, options=None):

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
