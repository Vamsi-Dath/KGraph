import gradio as gr

from src.KGraph.gui.index import index as index_demo
from src.KGraph.gui.graphviz import graph as graph_demo

tab = gr.TabbedInterface(
    [index_demo, graph_demo],
    tab_names=["Process Data", "Graph Visualization"]
)

with gr.Blocks(
    title="KGraph: Knowledge Graph Visualization",
    theme=gr.themes.Default(
        primary_hue="blue",
        secondary_hue="green",
        font="Arial"
    )
) as demo:
    gr.Markdown("# KGraph: Knowledge Graph Visualization")
    
    tab.render()


if __name__ == "__main__":
    demo.launch()
