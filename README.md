# Discord-Bot---Guild-Wars-Skill-Templates
A discord bot for linking skill bars from the ArenaNet game Guild Wars.  

![Screenshot](https://i.imgur.com/R1zh4RR.jpg)

You can use, modify, and share this code as you wish. 

This code is still under development.  Please be patient, but I will try to answer all questions and issues ASAP.  

This code was written to work with Guild Wars Prophecies, Guild Wars Factions, Guild Wars Nightfall, and Guild Wars Eye of the North skill templates for all released professions.

To use this, you will need to run your own discord bot either on a server or on your private computer.

In the discordway.py file, please be sure to edit the file path where applicable and the Discord key to get this running.

_______________
How it works:
_______________

1) See if a template is asked for in the discord channel it is set up for.
2) Decode the template using the ANet provided guidelines.
3) Take decoded values and assign corresponding attributes, profession, skills, etc.
4) Scrape the Guild Wars Wiki website for skill images.
  4.5) Store image locally for future skill bars to speed up the process!
5) Combine images into a skill-bar.
6) Post result back.
