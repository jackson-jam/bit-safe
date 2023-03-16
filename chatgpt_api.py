# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import os
import openai

openai.api_key = "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"

start_sequence = "\nA:"
restart_sequence = "\n\nQ: "
while 1 == 1:
    prompt = input(restart_sequence)
    if prompt == 'quit':
        break
    else:
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0,
                max_tokens=100,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            print(start_sequence, response["choices"][0]["text"].strip())
        except Exception as exc:
            print(exc)
