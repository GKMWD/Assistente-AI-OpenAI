# Assistant data

Assistants_data = [

{

"Name": "Math Tutor",

"Instructions": "You are a personal math tutor. Write and run code to answer math questions.",

"Tools": [{"type": "code_interpreter"}]

},

{

"Name": "Data Visualizer",

"Description": "You are great at creating beautiful data visualizations. You analyze data present in .csv files, understand trends, and come up with data visualizations relevant to those trends. You also share a brief text summary of the trends observed.",

"Tools": [{"type": "code_interpreter"}],

"File_ids": [file_speech.id]

},

# Add the remaining data from the assistants here

]

# Message data

Messages_data = [

{"Thread_id": thread_math.id, "role": "user", "content": "I need to solve the equation `3x + 11 = 14`. Can you help me?"},

{"Thread_id": thread_customer_support.id, "role": "user", "content": "I can not find in the PDF manual how to turn off this device.", "file_ids": [file_knowledge_pdf.id]},

{"Thread_id": thread_training.id, "role": "user", "content": "I need to train you. Can you assist me?", "file_ids": [file_training_code.id]}

]

# Data from tool outputs

Tool_outputs_data = [

# Add the tool output data here

]