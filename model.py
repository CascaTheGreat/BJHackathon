import cgi
import json
import cgitb
from werkzeug.datastructures import ImmutableMultiDict

form = cgi.FieldStorage()
searchterm = form.getvalue('searchbox')
searchterm = "I dont like change and sleep and I feel guilty about my self"
#defining our score counters for each mental illness
depression_score = 0
autism_score = 0

def userInputList(allTheData):
  #Step 1 change with .keys()
  stringInput = allTheData.keys()
  #Step 2 strip unnecessary characters from front and end
  newTestCase = str(stringInput)[12:-3]
  #Step 3 split into list
  testCaseList = newTestCase.split("', '")
  #Step 4, remove 'searchbar'
  #testCaseList.remove("searchbar")

  return testCaseList

#symptom distionaries with respective keywords
jdepression = '{"sad": "sadness", "hopeless":"hopeless", "irritable": "irritability", "involved": "less involved", "enjoy":"stop enjoying activities", "motiv": "unmotivated", "eat": "smaller appetite, larger appetite, changes in eating", "sleep": "sleeping more, sleeping less, changes in sleep", "energy":"changes in energy", "slug": "sluggish", "tense": "tense", "rest":"restless", "attention": "struggle paying attention", "worth": "worthless", "use": "useless", "guilt": "guilty", "self": "self-injury, self-destructive", "suicide": "suicidal thoughts"}'

jautism = '{"eye": "avoids eye contact", "respond": "does not respond to name by 9 months old", "express": "does not show facial expressions", "gesture": "uses few or no gestures", "interest": "does not share interests with others", "emotions": "struggles noticing others emotions", "pretend": "does not pretend in play", "line": "lines up objects", "order": "upset when order is changed", "repeat":"repeats words or phrases", "focus": "focused on parts of objects", "obsess":"obsessive interests", "change": "upset by minor changes", "routine": "must follow certain routines", "flap": "flaps hands","stim":"stim", "spin": "spins self in circles", "sens": "unusual sensory reactions", "delay": "delayed language skills, delayed movement, delayed learning skills", "activ": "hyperactive", "impulse": "impulsive", "attent": "inattentive behavior", "eat": "unusual eating", "sleep": "unusual sleeping habits", "emotion": "unusual emotional reactions", "anxi": "anxiety", "stress": "stress", "worr": "excessive worry", "fear": "lack of fear, excessive fear"}'


#Returns possible symptoms based on search phrase
def word_check(dict1):
    myList = []
    key_terms = dict1.keys()
    #checking for a match between the key and word
    for key in key_terms:
        if key in searchterm:
            myList.append(dict1[key])
    return myList


#identifying the illness and keeping
def add_score(symptom, dict1):
    if symptom in dict1.values():
        return 1
    return 0

def diagnosis(score_a, name_a, link_a, score_b, name_b, link_b):
  if score_a > score_b:
    diagList = [name_a, link_a, name_b, link_b]
  else:
    diagList= [name_b, link_b, name_a, link_a]
  return diagList

#performs word_check on the depression dictionary
depression = json.loads(jdepression)
dw = word_check(depression)

#performs word_check on the autism dictionary
autism = json.loads(jautism)
aw = word_check(autism)


def output(userInput):
  depression_score = 0
  autism_score = 0
  userInputActualList = userInputList(userInput)

  for i in userInputActualList:
    depression_score += add_score(i, depression)
    autism_score += add_score(i, autism)

  return(diagnosis(depression_score, "Depression","https://www.psychiatry.org/patients-families/depression/what-is-depression", autism_score, "Autism","https://www.cdc.gov/ncbddd/autism/facts.html"))