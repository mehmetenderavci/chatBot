import gradio as gr
import openai

openai.api_key = open("key.txt", "r").read().strip("\n")


class Chat:
    def __init__(self, label):
        self.message_history = [{"role": "user", "content": f""}, {"role": "assistant", "content": f""}]
        self.chatbot = gr.Chatbot(label=label)
        self.clear_button = gr.Button("Clear")

    def get_response(self, text):
        self.message_history.append({"role": "user", "content": f"{text}"})
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.message_history)
        reply_content = completion.choices[0].message.content
        self.message_history.append({"role": "assistant", "content": f"{reply_content}"})
        response = [(self.message_history[i]["content"], self.message_history[i + 1]["content"]) for i in
                    range(2, len(self.message_history) - 1, 2)]
        return response


def create_chat(label):
    chat = Chat(label)
    with gr.Column():
        txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(container=False)
        txt.submit(chat.get_response, txt, chat.chatbot)
        txt.submit(None, None, txt, _js="() => {''}")
        chat.clear_button.click(lambda: None, None, chat.chatbot, queue=False)
    return chat


with gr.Blocks() as demo:
    chat1 = create_chat("Chat1")
    chat2 = create_chat("Chat2")
    chat3 = create_chat("Chat3")
    chat4 = create_chat("Chat4")
    chat5 = create_chat("Chat5")
    chat6 = create_chat("Chat6")
    chat7 = create_chat("Chat7")
    chat8 = create_chat("Chat8")
    chat9 = create_chat("Chat9")
    chat10 = create_chat("Chat10")

demo.launch(server_name="0.0.0.0", server_port=7860)
