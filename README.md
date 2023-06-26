# 项目简介
- 旨在实现一个基于gradio和chatgpt的最简版的chatbot web客户端
- 参考项目：gradio doc文档

# 使用方法
- 配置.env文件中的openai key
- 安装gradio库
- 在文件所在目录下，运行：gradio app.py

# 实现逻辑介绍（app.py）
- 前端页面元素采用gradio框架生成
- 使用gradio Chatbot组件来呈现对话内容，自动呈现聊天对话内容，聊天内容需要以类似[user_chat, ai_chat]二维列表的形式传入
- 使用数组history保存chatgpt接口使用的历史对话信息，chat_history用于保存Chatbot组件使用的历史对话信息

# npc实现逻辑(npc.py)
- 尝试实现一个最简版的聊天npc：可扮演特定系列中的特定角色
- 使用langchain、chatgpt实现chatbot，前端使用gradio实现