# Pebble Prompter

## Inspiration
Composed of a diverse team, consisting of both high-school and university students, we strived to create an idea that would help us in our academic endeavours. Often, during school time we are asked to give presentations or lectures in activities/classes. Personally, we have seen many fellow classmates stumble and forget parts of their desired scripts/dialogues when presenting in front of large audiences. Generally, this occurs when the speech is quite large in length. A potential solution is to record the speech and play it through an earpiece as an audio file, however this method will not compensate for pauses or diversions during the speech, which are natural. To resolve this problem, we have created Pebble Prompter.

## What it does
Pebble prompter aims to simulate prompters offered to news anchors in major news corporations e.g. CBC. These prompters are controlled by humans, allowing for variations in the speed of the teleprompter to enable the news anchor to speak naturally during the newscast. We realized that this system could be replaced by an automated system using speech recognition techniques in order to reduce the amount of human effort/time spent manually controlling teleprompters. Essentially, our computer program analyzes speech samples from the user periodically using an in-built or external microphone. Initially, the user will enter the script of a speech which will be used for dynamically finding the position of the user in the speech. Throughout the speech, the program will constantly monitor the user's voice in order to determine how far the user has progressed in their speech. At any time, if the user needs assistance to remember the next part of their speech, they can look at the screen of their Pebble watch. Also, lecture supervisors or teachers can send comments through our Python interface such as "5 minutes left!" accompanied with haptic feedback to the user's watch. 

## How we built it
At its heart, Pebble Prompter is an automatic scrolling teleprompter. In order to determine the progress of the speech, it analyzes the voice of the user, nearly in real-time. PyAudio, a module, is used to record RAW audio files of 3 seconds constantly. These files are analyzed asynchronously by Google's Speech API to determine the position of the user within the speech's script. This is accomplished using fuzzy string analysis, specifically mathematical models and methods e.g. Levenshtein distance. Based on the information calculated, the Pebble smartwatch will display the appropriate words on its screen (a few words ahead of where the user currently is). 


## Challenges we ran into

* Speech recognition was a key part in this project, however it was also one of its most challenging. Initially, we planned on creating an Android application to act as a microphone for recording user audio to analyze. We tried using CMU (Carnegie Mellon University) Sphinx, a STT (speech-to-text) API with Android, however it was not found to be very inaccurate, potentially due to the poor quality of mobile microphones. After trying Android's Speech Recognizer class and several other APIs we determined Android to be insufficient for our needs. Therefore, we switched to recording and analyzing audio on a laptop. There was a great choice of speech-to-text APIs however many of them required payment, limiting our options. In the end, we used Google's Cloud Speech API which was extremely accurate and provided a sufficient amount of free credits. 
* Managing data across several platforms and architectures was extremely difficult. After deliberating over several methods to send data from one platform to another, we settled on using Google's Firebase. Using such a database allowed us to communicate effectively between our laptops and smartwatches.  

## Accomplishments that we're proud of 
* Getting speech recognition working after around 12 hours of endless frustration.
* Successfully creating a Heroku server that is integrated with Python program using the Flask framework 
* Asynchronous synchronization between audio recordings and speech analysis to reduce the amount of down time between recordings
* Figuring out the Pebble SDK using the C programming language to directly interface with the Pebble

## What we learned
* Speech recognition is much more difficult than Google makes it seem. Also, it is more difficult than text-to-speech recognition. 
* Pebble cannot handle C++ which results in the loss of the standard library, causing many tears and grievances due to the loss of beloved functions. 
* Sleep is a nice luxury we could not afford heavily. 

## What's next for Pebble Prompter
* Improve speech recognition capabilities to allow for continuous speech recognition. This will help avoid words to be split apart between two recordings, specifically complex words. 
* Improve the user interface to make it more usable and user-friendly. 
* Retry to construct an Android application since it would be more convenient for the user. 
