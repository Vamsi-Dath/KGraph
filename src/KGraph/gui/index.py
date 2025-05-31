import gradio as gr

def load_file(file):
    with open(file, "r") as f:
        contents = f.read()
    return contents

with gr.Blocks() as index:
    gr.Markdown('# Process Data')
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown('## Upload Data')
            files = gr.File(
                label="Allowed file types .json or .txt",
                file_types=[".json", ".txt"],
                file_count='single',
                render=True,
                type="filepath"
            )

        with gr.Column(scale=2):
            gr.Markdown('## Data Preview')
            data_preview = gr.Textbox(
                label="Preview",
                placeholder="The data will be displayed here.",
                lines=9,
                interactive=False
            )

        files.change(fn=load_file, inputs=files, outputs=data_preview)

        with gr.Column(scale=1):
            button = gr.Button(
                "Process Data",
                variant="primary",
                interactive=True
            )
            alert_msg = gr.Textbox(label="Alert", interactive=False)

    button.click(
        lambda files: "Success!" if files else "No files uploaded.",
        inputs=files,
        outputs=alert_msg
    )