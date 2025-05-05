#SAMPLE EXAMPLE ON HOW TO RUN ACCELERGY WITH HIGHLIGHT MODULE 
import os
from loaders import *
from nvidia import Nvidia
from highlight import HighLight
HighLight.quick_install_this_file()
result = run_accelergy(
    jinja_parse_data=dict(
        mapping='designs/untiled.map.yaml',
        sparse_optimizations='designs/sparse_opts/buffer_gating.yaml',
        constraints='designs/untiled.constraints.yaml',
        WORD_SIZE=8
    ),
    alt_top='designs/hl.yaml.jinja2',
)
