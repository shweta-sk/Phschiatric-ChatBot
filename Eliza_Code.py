#!/usr/bin/env python
# coding: utf-8

# In[ ]:



# *************Eliza Chatbot*******************

#Group Member Names: 1.Saksham Arora
#                    2.Preyaa Atri
#                    
#Date: 17 September 2019


#Introduction  to Eliza:

#    Eliza was Created in 1966 as an early natural language processing (NLP) computer program that emulates a Rogerian 
#    psychotherapist, a clinical practice that allows clients to take more action and progression in discussions. 
#    This is also known as person-centered therapy. Developed by Joseph Weizenbaum, ELIZA, named after a character in the play 
#    Pygmalion by George Bernard Shaw, is generally known as the first chatbot.


# In[ ]:


#Importing Libraries
import time

#
import sys

#
import re

#
from nltk.chat.util import Chat, reflections

#Defining the function for Regular Expressions!!

def expression_for_conversation(person_name):
    expressions = (

       # Default Expression in Conversation
        (r'(.*)',
        ( "Could you please tell me more!",
         "Do you care to explain that a little more?",
         "Tell me something about your near and dear ones!",
         "Is it possible or you to elaborate on that?",
         "How do you feel abut it??",
         "Is there a reaso for you to say %1?",
         "Well Well!!.",
         "What goes through your mind when you say that? Can you tell me?")),

        
        # Dangerous and impulsive words
        (r'(.*)((K|k)ill|(S|s)uicide|(H|h)omicide|(M|m)urder|(D|d)eath|(S|s)lay)(.*)',
        ("What makes you say that?",
        "I think you need serious attention and care.",
         "Please call the prevention lifeline at 1-800-273-8255",
         "Please listen to me and calm down.",
        "I think its an emergency. I am dailing 911!")),
        
        # Therapy and counseling words
        (r'(.*)((P|p)rocess|(C|c)ounselor|(P|p)sychologist|(S|s)ocial worker|(P|p)sychotherapist|(T|t)herapist)(.*)',
        ("Have you seen a counselor before?",
        "Have you discussed your issues with someone?",
         "What do you expect from the counseling process?",
         "Do you want to talk about your issues?")),
        
        # Problematic words
        (r'(.*)((P|p)roblem|(I|i)ssue|(D|d)epress|(H|h)ate|(B|b)ull(ied|y))(.*)',
        ("What is the problem from your viewpoint?",
        "Have you discussed your issues with someone?",
         "How does this problem make you feel?",
         "What makes the problem better?")),
        
        # Relationships
        (r'(.*)((B|b)oyfriend|(G|g)irlfriend|(F|f)riend|(F|f)amily|(R|r)elative|(P|p)eople)(.*)',
        ("How often do you get to meet up them?",
         "Do you have someone to talk to?",
         "Are you happy with them?",
         "Is there anyone who you feel understands you and is close to you?",
         "What involvement do you have with them?")),
        
        (r'(.*)(P|p)arent(.*)',
         ("Tell me more about your parents?",
          "How do you feel about them?",
          "How strong is your relationship with them?",
          "Good family relations are extremely important.")),
 
        (r'(.*)(C|c)hild(.*)',
        ("Did you have a childhood best friend?",
          "What is your favorite childhood memory?",
          "Did you get bullied as a child?")),
        
        # Life
        (r'(.*)(L|l)ife(.*)',
        ("What choice do you have about what happens in your life?",
        "Do you have a clear sense of where you want to take things in life?",
         "Do you feel excited by stuff in your life?")),
        
        # Mind, Body and Health
        (r'(.*)((D|d)iet|(S|s)leep|(E|e)xercise|(H|h)ealth|(B|b)ody)(.*)',
        ("Are you sleeping these days?",
        "Are you happy with your diet?",
         "How much exercise are you getting?")),
        
        # Statements about machines or code
        (r'((C|c)omputer |(R|r)obot |(B|b)ot |(M|m)achine |(C|c)reate)(.*)',
        ("Are you talking about me?",
         "My person_name is Eliza and I am here to help you!",
         "How do you feel speaking to a robotic Psychotherapist?",
        "Do you like machines?")),
        
        # Starting with I
        (r'(I|i) need (.*)',
        (person_name+" Why do you need %2?",
        person_name+" How important is %2 to you?",
        person_name+" Are you sure you need %2?")),

        (r'(I|i) feel (.*)',
        ( "Why "+person_name+" are you feeling %2?",
        person_name+" How often do you feel %2",
        person_name+" What do you do when you feel %2?",
        "Is there anything I can do to make you feel better?")),

        (r'(I|i) want (.*)',
        ( "Why do you want %2?",
        "Will you be happy if you get %2?")),

        (r'(I|i) would (.*)',
        ( "Why would you %2?",
        "Is anyone aware that you would %2?")),
        
        (r'(I|i) will (.*)',
        ("Are you sure you will %2",
        "Are you sure that you want to do it",
        "I encourage you to do good and useful things")),

        (r'(I|i) think (.*)',
        ("Why do you think %2?",
        "When did you get that thought?")),

        (r'(I|i) can\'t (.*)',
        ( "Why you can't %2?",
        "How do you know you can't %2?",
        "I think you can %2 if you try")), 
        
        # Asking questions
        (r'(C|c)an you (.*)',
        ( "Sure I am here to help you out.",
        "I will try my level best %2?",
        "If I cant then what will you do?")), 

        (r'(A|a)re you (.*)',
        ( "You think I am %2?",
        "How does that bother you?",
        "I might be %2, what do you think?")),

        (r'(.*)(W|w)hat (.*)',
        ( "Why do you want to know?",
        "How important is it for you to know?")),

        (r'(Y|y)ou are (.*)',
        ("You think I'm %2",
        "I think you are talking about yourself?",
        "How can you say that?")),
        
        # Reasoning statements
        (r'(.*)(B|b)ecause (.*)',
        ( "Are you sure?",
        "Are there any other reasons for it?")),
        
        # Apology statements
        (r'(.*)((S|s)orry |(A|a)polog)(.*)',
        ( "Thats fine, I can understand.",
        "No problem.",
        "Its totally fine")),
        
        # Acknowlegdements
        (r'(.*)(T|t)hank (.*)',
        ( "You are welcome!",
         "Sure. No worries!",
        "Do you need any other help?")),

        (r'(Y|y)es (.*)',
        ("You seem confident",
         "I understand.",
        "Looks like you are confident about it",
         "Okay, so tell me more.",
        "I will recommend you to concerned doctor. He shall help you out with it.")),
        
        (r'((S|s)ure |(O|o)kay|(R|r)ight)(.*)',
        ("Great! So, tell me more about yourself",
         "Alright. Good luck",
        "Sounds good")), 

        (r'(N|n)o (.*)',
        ("If you dont want to,its fine",
        "You are confident about it?",
         "Okay, so tell me more about yourself."
         "Alright.",
        "Do you want to think about it?")),

        # Statements for quiting
        (r'((Q|q)uit|(B|b)ye|(E|e)nd(.*))',
        ("Thank you for consulting me.",
         "Good-bye and take care.",
         "Your bill will be sent to your mail.",
         "Take care and have a great day!"))
        
    )
    return expressions




def chatBot_eliza():
    
    statement1 = "\t\t\t\tWelcome! This is the right place to get some help!!\n"
    print('\t' + '#'*110)
    
    statement2 = "A note on Positivity - \n"

    #We add a random positie quote (Some python programming required!

    statement3 = 'Hey there Amigo! To whom do I owe the pleasure of helping today?' # need to update 

    for s in statement1:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(0.1)

    for s in statement2:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(0.1)

    for s in statement3:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(0.1)
        
    # Interaction with the user to get his/her person_name
    user_interaction_input = str(input())
    
    # In case the user wants to exit the chatbot
    if re.match(r'(Q|q)uit', user_interaction_input) is not None:
        return
    
    # In case the user wants to continue with talking to the chatbot
    else:
        interaction = re.match(r'(Hi.|Hello.)?(Hi|I am|Myself|This is|My name is)?(.*)', user_interaction_input, re.I)
        person_name = interaction.group(3)
        print("Heya", person_name +". Seems like you need my help with something? Tell me about it!!") 

        # Creation of expression for the chatbot to converse with the user
        expressions = expression_for_conversation(person_name)
        # create the chat instance by passing pairs and reflections
        conversation = Chat(expressions, reflections)
        #start conversation 
        conversation.converse()


if __name__ == "__main__":
    chatBot_eliza()


# In[ ]:




