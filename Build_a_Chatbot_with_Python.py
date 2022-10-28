#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.chat.util import Chat, reflections


# In[2]:


print(Chat)


# In[4]:


reflections


# In[9]:


set_pairs = [
    [
        r'mi nombre es (.*)',
        ['Hola %1, Como estas hoy?',]
    ],
    [
        r'hola|ola|hello',
        ['Hola', 'Hola a todos',]
    ],
    [
        r'cual es tu nombre?',
        ['Puedes llamarme kBot',]
    ],
    [
        r'como estas?',
        ['Estoy bien, gracias!, como puedo ayudarte?',]
    ],
    [
        r'como puedo ayudarte?',
        ['estoy buscando guías y cursos online para aprender ciencia de datos, ¿me puedes sugerir?', 'estoy buscando plataformas de formación en ciencia de datos',]
    ],
    [
        r'estoy (.*) haciendolo bien',
        ['Me alegro de oírlo', '¿En qué puedo ayudarle?:)',]
    ],
    [
        r'estoy buscando guías y cursos online para aprender ciencia de datos, ¿me puedes sugerir?',
        ['Pluralsight es una gran opción para aprender ciencia de datos. Puedes consultar su página web',]
    ],
    [
        r'gracias por la sugerencia. ¿tienen grandes autores e instructores?',
        ['Sí, tienen los mejores autores del mundo, ese es su punto fuerte;)',]
    ],
    [
        r'(.*) muchas gracias, ha sido de gran ayuda',
        ['Estoy encantado de ayudarte', 'Sin problema, de nada',]
    ],
    [
        r'quit',
        ['Adiós, cuídate. Nos vemos pronto :) ', 'Ha sido un placer hablar contigo. Nos vemos pronto :)']
    ],
]


# In[10]:


def chatbot():
        print('Hola, soy el bot que has creado')

chatbot()


# In[11]:


chat = Chat(set_pairs, reflections)
print(chat)


# In[12]:


chat.converse()
if __name__ == '__main__':
    chatbot()

