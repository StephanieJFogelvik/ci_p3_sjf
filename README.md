![image](assets/images/p-3-amiresponsive.png)
# A Flashcard Game for Practicing Swedish Vocabulary
## Words selected from a list of 100 basic Swedish words and simple phrases.
### Game marketed at beginner learners of Swedish who are English speakers - but it should be accessible even to those with no prior knowledge of the language (as long as they speak English). Some basic, everyday words which share similarity with English (such as the names of the months) are included for the purpose of impressing upon the user the similarities between the Swedish and English language. No words or phrases are repeated in a game. There is an option added for to play a new game once the game is over.

# Validator Testing
- http//pep8online.com/

# Python Libraries
---
## random
- Used to randomise the selection of the "flashcards" (Swedish words and phrases)
## time
- Used to create pauses between flashcards

# Personal Testing
 - I tested every new code added to the game via the command terminal & on the deployment page for bugs & errors.

# Deployment
The site was deployed using Heroku using the folowing guidelines:

Ensure that the project has the correct content within the requirements.txt document by running the following commands in the IDE terminal: -pip freeze > requirements.txt
Check requirements folder to confirm. Now select the option for New App, (You may have upto 5 applications live with a free heroku account)
Insert project a name, and choose your location
Once successful the project dashboard will display
As this project does not make any API calls there is no requirement to add an authorisation key
Add Buildpacks required, both Python and Nodejs (to be added in that order!)
Select the deployment tab and choose Github at the bottom of the deploy page
Search for your repository, and select the correct match
Deploying to Heroku can be done automatically & manually, I enabled automatic builds when code commited & manually built the application
See live project on Heroku at the top of the page under Live Prototype Demo.

# Credits:

100 Basic Swedish word list (with some modifications of my own) credit goes to: https://www.swedishpod101.com/swedish-word-lists/?page=1

ASCII art credit goes to Max Strandberg, at: https://www.asciiart.eu/buildings-and-places/flags