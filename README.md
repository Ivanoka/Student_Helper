Student Helper (server)
=======================

Version History
===============
```
0.1 In progress (26.02.2022)
* Added group registration
* Registration is based on an authorization code
* After registration, the code is removed from the database
* 5 minutes to register:
  * After the time is out, a message is sent and the subprocess 
    ends, for a new attempt, you must enter the command /start
* When registering a new chat for a group with 
  a registered chat, the ID of the new chat is recorded, and 
  a re-registration message is sent to the old conversation
* There is error handling and sending appropriate messages
```
