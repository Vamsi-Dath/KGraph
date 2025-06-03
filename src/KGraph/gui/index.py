import gradio as gr
import os
from pathlib import Path
import datetime
import time

_CURRENT_DATABASE = None

def load_file(files):
    if not files:
        return
    contents = ""
    for file in files:
        with open(file, "r") as f:
            contents += "-"*50 + "\n👉 " + file + "\n\n"
            yield contents
            time.sleep(0.5)
            contents += f.read()
            yield contents
            contents += "\n\n"
            time.sleep(1)
    return

def index_file_uploaded(
    file_path:list[str],
    base_url: str | None = None,
    api_key: str | None = None,
    llm_model: str | None = None,
):
    if not file_path:
        yield "Upload file to continue."
        return

    if base_url:
        os.environ["BASE_URL"] = base_url
    if api_key:
        os.environ["API_KEY"] = api_key
    if llm_model:
        os.environ["LLM_MODEL"] = llm_model
    

    result_log = (
        "Program configs:\n"
        + f"BASE_URL: {base_url}\n\nAPI_KEY: ....\n\nLLM_MODEL: {llm_model}\n\nDatabase: {_CURRENT_DATABASE}\n"
    )
    yield result_log
    result_log += f"\nStart indexing {[Path(p).name for p in file_path].__str__()} at {datetime.datetime.now()}...\n"
    yield result_log

    # Implement the indexing logic
    
    result_log += "\nSave to database...\n"
    result_log += f"END!"
    yield result_log
    return


with gr.Blocks() as index:
    gr.Markdown('# Process Data')
    with gr.Row():
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown('## Upload Data')
                files = gr.File(
                    label="Allowed file types .json",
                    file_types=[".json"],
                    file_count="multiple",
                    render=True,
                    type="filepath"
                )

            with gr.Accordion(label="LLM Configuration", open=False):
                    base_url = gr.Textbox(
                        placeholder="baseurl", label="LLM Baseurl"
                    )
                    api_key = gr.Textbox(
                        placeholder="API key",
                        label="API Key",
                        type="password",
                    )
                    llm_model = gr.Dropdown(
                        ["gpt-4o-mini", "gpt-4o", "claude-3.5-sonnet"],
                        allow_custom_value=True,
                        label="LLM Model",
                        interactive=True,
                    )

        with gr.Column(scale=1):
            gr.Markdown('## Data Preview')
            data_preview = gr.Textbox(
                label="Preview",
                placeholder="The data will be displayed here.",
                lines=9,
                interactive=False
            )

        files.change(fn=load_file, inputs=files, outputs=data_preview)

        with gr.Column(scale=2):
            button = gr.Button(
                "Start Indexing",
                variant="primary",
                interactive=True
            )
            alert_msg = gr.Textbox(label="Status", interactive=False)

    button.click(
        index_file_uploaded,
        inputs=[
            files,
            base_url,
            api_key,
            llm_model
        ],
        outputs=alert_msg
    )