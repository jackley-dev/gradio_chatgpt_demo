import os
import openai
import gradio as gr
from dotenv import load_dotenv
import os

# 加载.env 文件
load_dotenv()
# 设置 openai API 密钥
openai.api_key = os.getenv("OPENAI_API_KEY")

history = [{"role": "system", "content": "You are a helpful assistant."}]
model = "gpt-3.5-turbo"


# generate a response
def generate_response(user_prompt="", chat_history=[]):
    # 用户会话
    history.append({"role": "user", "content": user_prompt})
    completion = openai.ChatCompletion.create(
        model=model,
        messages=history
    )
    response = completion.choices[0].message.content
    # AI回复会话
    history.append({"role": "assistant", "content": response})
    chat_history.append([user_prompt, response])

    total_tokens = completion.usage.total_tokens
    prompt_tokens = completion.usage.prompt_tokens
    completion_tokens = completion.usage.completion_tokens
    return "", chat_history


# 一个简单chatbot demo
with gr.Blocks() as demo:
    gr.Markdown("""<h1><center>Gradio Chatbot Demo</center></h1>""")
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    submit = gr.Button("SEND")
    submit.click(generate_response, inputs=[msg, chatbot], outputs=[msg, chatbot])
    clear = gr.ClearButton([msg, chatbot])

demo.launch()
