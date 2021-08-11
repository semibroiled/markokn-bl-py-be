import random
def ask(answer=True):

    body =''''
        Are lizards small?

        Are apples red fruit?

        Are muscles needed to move our body?

        Are scoops of ice cream sweet?

        Are bananas and oranges sweet vegetables?

        Are dogs and cats animals that live in the jungle?

        Are roses tall trees?

        Are wild animals dangerous?

        Are coffee and hot chocolate cold drinks?

        Are shovels something you would use to dig a hole with?

        Are computers used to brush your teeth with?

        Are fruits and vegetables healthy to eat?

        Are musicians and artists creative?

        Are pencils and markers used to write on a whiteboard?

        Are Spanish and German different languages?

        Are cars used to drive on the water?

        Are rattlesnakes poisonous?

        Are band-aids used for healing?

        Are umbrellas used to keep you wet?

        Are the letters "d" and "s" in the word "dressing"?

        Are flies and robins small insects?

        Are clocks and bikes used to tell time?

        Are violins and pianos musical instruments?

        Are paint and syrup used to take a bath in?

        Are aspirin and tylenol pain relievers?

        Are airplanes flown inside?

        Are pillows and mattresses used to sleep on?

        Are shoes worn over the top of socks?

        Are football and baseball types of food?

        Are chips and pretzels salty?

        Are houses more than $50 dollars?

        Are lasagna and spaghetti Chinese dishes?

        Are peanuts made into jam?

        Are ovens used to freeze things?

        Are there 80 minutes in an hour?

        Can pigs walk on two feet?

        Can you touch your elbow with your nose?

        Can you fry vegetables in a pan?

        Can you brush your teeth with a shoe?

        Can you stretch a rock?

        Can you grow a mustache on your foot?

        Can you sleep in the day time?

        Can you ride a bike without a helmet?

        Can you drive a car wearing a blindfold?

        Can a backpack get a cold?

        Can you stir something with a spoon?

        Can you wear pajama's to school / work?

        Can you jump over a puddle?

        Can you eat tomato soup with a fork?

        Can you keep a horse inside your house?

        Can you see in the dark without a flashlight?

        Can you buy eggs by the dozen?

        Can you teach a cat to talk?

        Can a tiger be your pet?

        Can you rake leaves with a hammer?

        Can you ride a camel?

        Can you use a shovel at the beach?

        Can you eat without a mouth?

        Can a circle have corners?

        Can a fish live out of water?

        Can you rip concrete?

        Can you wear a tie?

        Can you drive a car without wearing a seatbelt?

        Can you make bread without using flour?

        Can you freeze orange juice?'''
    pool = body.split('?')
    x = random.choice(pool)
    question = input (f'{x} ? \n')
    
    if 'y' in question.lower():
        return True
    elif 'n'  in question.lower():
        return False
    else: 
        return 'Unkown parameters. Try again'
print(ask())

