"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
#from Crypto.Cipher import AES

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, example_param=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.example_param = example_param

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        # key = b'\xc7\x0b\x177vMN\x0f\x16\x85r\x8c*\xcb\xaa\xd8'
        # cipher_aes = AES.new(key, AES.MODE_EAX) 
        # output_items[0][:] = cipher_aes.encrypt_and_digest(input_items[0] * self.example_param)
        output_items[0][:] = (input_items[0] * 499) % 16
        # print(output_items[0])
        return len(output_items[0])
