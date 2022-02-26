Student Helper
==============

This project is created to simplify and automate the process of managing a study group.
The developer is a student at the Mogilev State A. Kuleshov University at the Faculty of Mathematics and Natural Science.

**Opportunities:**
* Registration of a new chat for a group, entered into the database
* Сheck and update server, key and ts before launch

**In the plans:**
* Client in the form of a web application for android for managing a study group
  * Adding and removing students
  * Marking sick people



Version History
===============
```
0.1.1 In progress (26.02.2022)
* Added check and update server, key and ts
* Check time once per hour
* If there is an error, it is printed to the console

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


Licence and Copyright
=====================
If you use this library for any cool project let me know!

```
Copyright (c) 2022 Ivan Titov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
