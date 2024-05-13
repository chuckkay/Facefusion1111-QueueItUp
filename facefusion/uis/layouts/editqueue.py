import multiprocessing
import gradio
from typing import Optional

from facefusion.uis.components import frame_processors, frame_processors_options, execution, execution_thread_count, source
ABOUT_BUTTON = gradio.Button(
    value = "MORE FEATURES COMING SOON",
    variant = 'primary',
    link = 'https://github.com/chuckkay/Facefusion-QueueItUp-sd-webui'
    )
DONATE_BUTTON = gradio.Button(
    value = "DONATE",
    link = 'https://www.paypal.com/paypalme/CharlesKadish',
    size = 'sm'
    )

def pre_check() -> bool:
    return True


def pre_render() -> bool:
    return True
    
def render() -> gradio.Blocks:
    with gradio.Blocks() as layout:
        with gradio.Row():
            with gradio.Column(scale = 2):
                with gradio.Blocks():
                    ABOUT_BUTTON.render()
                    DONATE_BUTTON.render()
    return layout

def listen() -> None:
    frame_processors.listen()

def run(ui : gradio.Blocks) -> None:
    concurrency_count = min(8, multiprocessing.cpu_count())
    ui.queue(concurrency_count = concurrency_count).launch(show_api = False, quiet = True)
