#!/usr/bin/env python3

import gradio as gr
from modules import script_callbacks

import facefusion.globals
from facefusion import logger, face_analyser, content_analyser
from facefusion.core import apply_args, get_argument_parser, pre_check
from facefusion.core2 import apply_args as apply_args2
from facefusion.processors.frame.modules import (
    face_debugger,
    face_enhancer,
    face_swapper,
    frame_enhancer,
    frame_colorizer,
    lip_syncer,
)
from facefusion.uis.layouts import QueueItUp, editqueue, webcam #, benchmark


def on_ui_tabs():
    apply_args(get_argument_parser())
    logger.init(facefusion.globals.log_level)

    if not pre_check():
        return

    if (
        not face_debugger.pre_check()
        or not face_analyser.pre_check()
        or not content_analyser.pre_check()
        or not face_enhancer.pre_check()
        or not face_swapper.pre_check()
        or not frame_colorizer.pre_check()
        or not frame_enhancer.pre_check()
        or not lip_syncer.pre_check()
    ):
        return
    if not QueueItUp.pre_check():
        return
        
    if not editqueue.pre_check():
        return
        
#    if not benchmark.pre_check():
#        return
        
    if not webcam.pre_check():
        return

    with gr.Blocks() as block:
        with gr.Tab("Facefusion with QueueItUp"):
            if QueueItUp.pre_render():
                QueueItUp.count_existing_jobs()
                QueueItUp.default_values = QueueItUp.get_values_from_FF("default_values")
                QueueItUp.render()
                QueueItUp.listen()
        with gr.Tab("Edit Queue"):
            if editqueue.pre_render():
                editqueue.render()
                editqueue.listen()
#        with gr.Tab("Benchmark"):
#            if benchmark.pre_render():
#                benchmark.render()
#                benchmark.listen()
        with gr.Tab("Webcam"):
            if webcam.pre_render():
                webcam.render()
                webcam.listen()

        return ((block, "FaceFusion", "facefusion"),)


script_callbacks.on_ui_tabs(on_ui_tabs)
