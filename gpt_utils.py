import openai
import os
import time
import requests
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI # pip install openai --upgrade

_ = load_dotenv(find_dotenv())
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

with open('instruction_mj.txt', 'r') as file:
    text_from_file = file.read().strip()


original_prompt = 'ERROR!'

styles = {"3d animation", "anime","animation", "cinematic", "film", "lego", "makoto shinkai", "pixel"}

def generate_prompt(ref_obj, instruction):
    try:
        response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "user", "content": f"{instruction} . Here's the input. {ref_obj} ->"},
          ]
        )
    except requests.RequestException as e:
    # Handle network-related errors
        print(f"Network error: {e}")
    except Exception as e:
    # Handle other unexpected errors
        print(f"Unexpected error: {e}")
    except:
        return "ERROR!!!"
    # except OpenAIError as e:
    # # Handle specific OpenAI-related errors
    #     print(f"OpenAI error: {e}")

    return response.choices[0].message.content ### [:-1]
    # probably need streaming at "inspire me"? or never need?


def is_word_in_sentence(word, sentence):
    pattern = r'\b' + re.escape(word) + r'\b'
    return re.search(pattern, sentence) is not None

def replace_word_in_sentence(word, replacement, sentence):
    pattern = r'\b' + re.escape(word) + r'\b'
    new_sentence = re.sub(pattern, replacement, sentence)
    return new_sentence

def rewrite_for_3D_and_cartoon(original_prompt):
    new_prompt = copy.deepcopy(original_prompt)
    new_prompt  = describe(new_prompt)
    return new_prompt         










# def generate_prompt(prompt):
#     assistant = client.beta.assistants.create(
#         name="Math Tutor",
#         instructions="Use descriptive words to rephrase the input.",
#         # tools=[{"type": "code_interpreter"}],
#         model="gpt-4-1106-preview"
#     )
#     thread = client.beta.threads.create()

#     message = client.beta.threads.messages.create(
#         thread_id=thread.id,
#         role="user",
#         content={prompt},
#     )
#     run = client.beta.threads.runs.create(
#         thread_id=thread.id,
#         assistant_id=assistant.id,
#         #instructions="Please address the user as Jane Doe. The user has a premium account."
#     )    
#     run = client.beta.threads.runs.retrieve(
#         thread_id=thread.id,
#         run_id=run.id
#     )
#     messages = client.beta.threads.messages.list(
#         thread_id=thread.id
#     )
#     return messages


# try:
#     client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

#     assistant = client.beta.assistants.create(
#         name="Midjourney Input Enhancer",
#         instructions='Use descriptive words to rephrase the input.',
#         #tools=[{'type': 'retrieval'}], 
#         model='gpt-4-1106-preview',
#         #file_ids=['file-R2D9wZymehervuVT4u14mXLr']
#     )

#     thread = client.beta.threads.create()

#     message = client.beta.threads.messages.create(
#         thread_id=thread.id,
#         role='user',
#         content='Can you tell me about the document you have?',
#     )

#     start_time = datetime.now()  # Start timing the response generation
#     run = client.beta.threads.runs.create(
#         thread_id=thread.id,
#         assistant_id=assistant.id
#     )

#     def wait_on_run_retrieve(run, thread):
#         while run.status == 'queued' or run.status == 'in_progress':
#             run = client.beta.threads.runs.retrieve(
#                 thread_id=thread.id,
#                 run_id=run.id,
#             )
            
#             time.sleep(0.5)

#         return run
    
#     run = wait_on_run_retrieve(run=run, thread=thread)
#     end_time = datetime.now()  # End timing after the run is complete
#     duration = (end_time - start_time).total_seconds()  # Calculate the duration
#     print(f'AI response time: {duration} seconds')  # Output the duration

#     messages = client.beta.threads.messages.list(
#         thread_id=thread.id,
#     )

    
#     for message in reversed(messages.data):
#         if hasattr(message.content[0], 'text'):
#             print(message.role + ' : ' + message.content[0].text.value) # type: ignore

# except Exception as e:
#     print(f'An error occurred: {e}')



# def generate_prompt_MJ(prompt):
#     PROMPT_MESSAGES = [
#     {
#         "role": "user",
#         "content": [
#             text_from_file, prompt
#         ],
#     },
#     ]
#     params = {
#     "model": "gpt-4-1106-preview",
#     "messages": PROMPT_MESSAGES,
#     "max_tokens": 100,
#     }
#     result = client.chat.completions.create(**params)
#     return (result.choices[0].message.content)

# def generate_prompt_Pika(prompt):
#     PROMPT_MESSAGES = [
#     {
#         "role": "user",
#         "content": [
#             text_from_file, prompt
#         ],
#     },
#     ]
#     params = {
#     "model": "gpt-3.5-turbo",
#     "messages": PROMPT_MESSAGES,
#     "max_tokens": 100,
#     }
#     result = client.chat.completions.create(**params)
#     return (result.choices[0].message.content)