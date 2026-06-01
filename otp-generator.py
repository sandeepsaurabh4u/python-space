import string
import secrets
import gradio as gr

def otp_generator(length=6):
    choice = string.digits
    otp = ''.join(secrets.choice(choice) for _ in range(length))
    return otp

with gr.Blocks() as demo:
    gr.Markdown("# OTP Generator")
    length_input = gr.Number(label="OTP Length", value=6, minimum=1, maximum=10)
    generate_btn = gr.Button("Generate OTP")
    otp_output = gr.Textbox(label="Generated OTP")

    generate_btn.click(fn=otp_generator, inputs=length_input, outputs=otp_output)

demo.launch()
