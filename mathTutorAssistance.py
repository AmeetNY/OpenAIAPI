# we're creating an Assistant that is a personal math tutor, 
# with the Code Interpreter tool enabled

import openai
import time
openai.api_key = "sk-api_key"

assistant_id = "asst_id"

def create_thread(assistant_id,prompt):
    
    # Create an Assistant
    assistant = openai.beta.assistants.create(
        name="Math Tutor",
        instructions="You are a personal math tutor. Write and run code to answer math questions.",
        tools=[{"type": "code_interpreter"}],
        model="gpt-4-turbo-preview"
    )
    
    # Create a thread
    thread = openai.beta.threads.create()
    my_thread_id = thread.id
    
    # Add a Message to a Thread
    message = openai.beta.threads.messages.create(
        thread_id=my_thread_id,
        role="user",
        content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
    )
    
    # Run the Assistant
    run = openai.beta.threads.runs.create(
        thread_id=my_thread_id,
        assistant_id=assistant.id,
        instructions="Please address the user as Jane Doe. The user has a premium account."
    )
    
    # Check the run status
    run = openai.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    
    # Display the Assistant's Response
    messages = openai.beta.threads.messages.list(
        thread_id=thread.id
    )
    
    # Here is an example of what that might look like:
    '''   
    ROLE	CONTENT
    user	I need to solve the equation 3x + 11 = 14. Can you help me?
    assistant	Certainly, Jane Doe. To solve the equation (3x + 11 = 14) for (x), you'll want to isolate (x) on one side of the equation. Here's how you can do that:
    Subtract 11 from both sides of the equation to get (3x = 3).
    Then, divide both sides by 3 to solve for (x).
    Let me calculate the value of (x) for you.
    assistant	The solution to the equation (3x + 11 = 14) is (x = 1).
    '''
