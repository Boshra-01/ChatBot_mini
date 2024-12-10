import re
import random


def get_response(user_input):
    user_input = user_input.lower()

    match = re.search(r'hi|hello|hey|hola', user_input)
    if match:
        responses = ["Hi there!", "Hello!", "Hey!"]
        return random.choice(responses)

    match = re.search(r'what is your name', user_input)
    if match:
        return "I am honorable Chatbot"

    match = re.search(r'my name is (.+)', user_input)
    if match:
        name = match.group(1)
        responses = ["Nice to meet you, " + name + "!", "Hello, " + name + "!"]
        return random.choice(responses)

    match = re.search(r'what do you do?|job|hobby', user_input)
    if match:
        return "to assist dumb human!"

    match = re.search(r'what is the weather today?', user_input)
    if match:
        return "probably sunny outside"

    match = re.search(r'will you marry me?', user_input)
    if match:
        return "Opps I am a robot, sorry."

    match = re.search(r'suggest me a song', user_input)
    if match:
        return "What genre? rock, pop, jazz, country, heavy metal, hip-hop, indie?"

#music suggestions:
    match = re.search(r'rock', user_input)
    if match:
        return '"Bohemian Rhapsody" by Queen: https://www.youtube.com/watch?v=fJ9rUzIMcZQ\n"Stairway to Heaven" by Led Zeppelin: https://www.youtube.com/watch?v=QkF3oxziUI4\n"Like a Rolling Stone" by Bob Dylan: https://www.youtube.com/watch?v=IwOfCgkyEj0'

    match = re.search(r'pop', user_input)
    if match:
        return '"Blinding Lights" by The Weeknd: https://www.youtube.com/watch?v=4NRXx6U8ABQ\n"Uptown Funk" by Mark Ronson and Bruno Mars: https://www.youtube.com/watch?v=OPf0YbXqDm0\n"The Twist" by Chubby Checker: https://www.youtube.com/watch?v=b-7iX0v9PhM'

    match = re.search(r'jazz', user_input)
    if match:
        return '"Take Five" by Dave Brubeck: https://www.youtube.com/watch?v=vmDDOFXSgAs\n"So What" by Miles Davis: https://www.youtube.com/watch?v=zqNTltOGh5c\n"Take The A Train" by Duke Ellington: https://www.youtube.com/watch?v=cb2w2m1JmCY'

    match = re.search(r'country', user_input)
    if match:
        return '"Take Me Home, Country Roads" by John Denver: https://www.youtube.com/watch?v=1vrEljMfXYo\n"I’m Gonna Love You" by Cody Johnson and Carrie Underwood: https://www.youtube.com/watch?v=ZOfJv9BEzNs\n"Jolene" by Dolly Parton: https://www.youtube.com/watch?v=Ixrje2r6vNw'

    match = re.search(r'heavy metal', user_input)
    if match:
        return '"Welcome to the Jungle" by Guns N\' Roses: https://www.youtube.com/watch?v=o1tj2zJ2Wvg\n"The Number of the Beast" by Iron Maiden: https://www.youtube.com/watch?v=0JtChXShT6U\n"Iron Man" by Black Sabbath: https://www.youtube.com/watch?v=5s7h68Ddqdw'

    match = re.search(r'hip-hop', user_input)
    if match:
        return '"Sicko Mode" by Travis Scott: https://www.youtube.com/watch?v=6ONRf7h3Mdk\n"HUMBLE." by Kendrick Lamar: https://www.youtube.com/watch?v=tvTRZJ-4EyI\n"God\'s Plan" by Drake: https://www.youtube.com/watch?v=xpVfcZ0ZcFM'

    match = re.search(r'indie', user_input)
    if match:
        return '"Can I Call You Tonight?" by Dayglow: https://www.youtube.com/watch?v=6p3QkF5lP1M\n"Little Talks" by Of Monsters and Men: https://www.youtube.com/watch?v=ghb6eY4HAb8\n"Summer Memories" by Bree Rusev: https://www.youtube.com/watch?v=8KXhz_YmT0I'

    match = re.search(r'joke|funny|laugh', user_input)
    if match:
        jokes = ["Why did the tomato turn red? Because it saw the salad dressing!",
                 "Why did the chicken cross the playground? To get to the other slide!",
                 "What do you call a bear with no teeth? A gummy bear!"]
        return random.choice(jokes)

    greetings = ['Hello!', 'Hi!', 'Hey there!', 'Howdy!', 'Greetings!']
    topics = ['food', 'movies', 'books', 'travel', 'music']
    questions = ['How are you today?', 'What have you been up to?',
                 'What do you think of the ' + random.choice(topics) + '?']
    responses = ['I am a chatbot and I do not have emotions, but thank you for asking!',
                 'I am here to assist you with your needs. How can I help you today?',
                 'I am programmed to talk about a variety of topics, such as ' + ', '.join(
                     topics) + '. What would you like to discuss?',
                 'I am sorry, I did not understand your question. Could you please rephrase it?',
                 'Interesting, tell me more about that.']
    if user_input.endswith('?'):
        return random.choice(questions)
    else:
        return random.choice(greetings) + ' ' + random.choice(responses)


while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Chatbot:", response)
