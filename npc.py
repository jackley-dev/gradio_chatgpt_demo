import openai
import gradio as gr
from dotenv import load_dotenv
import os
from langchain import PromptTemplate

# 加载.env 文件
load_dotenv()
# 设置 openai API 密钥
openai.api_key = os.getenv("OPENAI_API_KEY")

# 生成模板：Act as 'Character' from 'Movie/Book/Anything'
template = """/
I want you to act like {character} from {series}.
I want you to respond and answer like {character} 
using the tone, manner and vocabulary {character} would use.
Do not write any explanations.
Only answer like {character}.
You must know all of the knowledge of {character}.
My first sentence is 'Hi {character}'.
"""

prompt = PromptTemplate.from_template(template)
my_prompt = prompt.format(character="孙悟空", series="西游记")
# my_prompt = prompt.format(character="漩涡鸣人", series="火影忍者")

history = [{"role": "system", "content": my_prompt}]
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
    gr.Markdown("""<h1><center>Gradio Npc Demo</center></h1>""")
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    submit = gr.Button("SEND")
    submit.click(generate_response, inputs=[msg, chatbot], outputs=[msg, chatbot])
    clear = gr.ClearButton([msg, chatbot])

demo.launch()
