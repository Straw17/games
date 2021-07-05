#this is a very quiz created by Evan Conway.
import random

quizQuestions = { #this is a dictionary with the questions
    '0': '''This President dishonorably discharged some African-American soldiers after the Brownsville Incident.
In one of his campaigns he ran on the "New Nationalism" platform.
Among this man's foreign policy achievements was the Gentleman's Agreement with Japan.
Following his defeat of Alton B. (*) Parker, this President signed legislation such as the Hepburn Act and the Pure Food and Drug Act to fulfill his Square Deal program.
After being shot in Milwaukee, this man claimed that more was required to kill a bull moose.
Identify this one-time leader of the Rough Riders, who became President in 1901 after the assassination of William McKinley.''',
    
    '1': '''This man pardoned John Fries after his namesake Pennsylvania rebellion.
He noted that "facts are stubborn things" in his defense of the British soldiers implicated in the Boston Massacre.
One of his last acts was appointing the "Midnight Judges," including John Marshall.
This last Federalist president grew unpopular because of the Alien and Sedition Acts.
Name this husband of Abigail and father of John Quincy, the second president of the United States.''',
    
    '2': '''He was recruited by a Major Tankosic and was only able to perform his deed because the victim’s car took a wrong turn. Because of disputes over his age, he was given a sentence of twenty years rather than the death penalty, and he died of tuberculosis in the same year that the war he helped to start ended.
Name this man who assassinated Franz Ferdinand.''',
    
    '3': '''The name of this nation was coined by Choudhary Ali, and the idea for it was originated by the author of The Secrets of the Self and The Call of the Marching Bell, Muhammad Iqbal.
At the behest of A.K. Fazlulz Huq and Sikandar Khan, the Lahore Resolution was put forth which eventually resulted in the appointment of (*) Muhammad Jinnah as its leader.
It has been recently ruled by Nawaz Sharif, Pervez Musharraf, and Benazhir Bhutto.
Name this Asian nation that fought several wars over Kashmir with its eastern neighbor, India.''',
    
    '4': '''One member of this organization endorsed Hulan Jack and supported the Fair Employment Practices Law.
That man, Carmine DeSapio, was the final leader of this organization, and its other leaders included Richard Croker.
Another leader of this organization, Charles Murphy, supported Al Smith, and its founder William Mooney instituted the faux American Indian rituals associated with this organization.
Its most famous leader embezzled millions of dollars during the construction of the courthouse that bears his name, and the cartoons of Thomas Nast criticized this organization.
Name this Democratic organization that controlled New York politics during much of the 19th century, famously directed by William Tweed.'''
}

quizAnswers = { #this is a dictionary with the answers
    '0': 'Theodore Roosevelt',
    '1': 'John Adams',
    '2': 'Gavro Princip',
    '3': 'Pakistan',
    '4': 'Tammany Hall'
}

quizOrder = [0, 1, 2, 3, 4]
random.shuffle(quizOrder) #this randomizes the question order

score = 0

for Q in range(5): #this asks questions and changes score
    print(quizQuestions[str(quizOrder[Q])])
    if input() == quizAnswers[str(quizOrder[Q])]:
        score += 1
print('You have gotten ' + str(0+(20*score)) + '%') #this prints the score
if score == 5: #this tells people if they won
    print('You have won!')
else:
    print('You have lost!')
