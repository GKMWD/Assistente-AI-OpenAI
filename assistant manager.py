from openai import OpenAI

class AssistantManager:
    def __init__(self, client):
        self.client = client
        self.assistants = []
        self.threads = []

    def create_assistants(self, assistants_data):
        for assistant_data in assistants_data:
            assistant = self.client.beta.assistants.create(**assistant_data)
            self.assistants.append(assistant)

    def create_threads(self, num_threads):
        self.threads = [self.client.beta.threads.create() for _ in range(num_threads)]

    def send_messages(self, messages_data):
        for message_data in messages_data:
            self.client.beta.threads.messages.create(**message_data)

    def submit_tool_outputs(self, tool_outputs_data):
        for tool_output_data in tool_outputs_data:
            self.client.beta.threads.runs.submit_t