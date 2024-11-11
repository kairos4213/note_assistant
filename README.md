# Note Assistant
A simple cli tool to store a note for user reference later (and I mean simple.)

## The "Why" for Making This
I have been working through the boot.dev (great course, btw -- [check it out](www.boot.dev)) 
coursework and got to the first solo project, where we were to come up with our
own small Python project.

This was where I mulled over several different project ideas, started and stopped
several of those ideas, and in the midst of all this (and in the chaos of being a
father to twins) realized I was always losing notes and wished I had a way to jot
something down quickly, without taking my eyes from the screen.

Enter note_assistant.

## Under the Hood
If you've read this far, thanks for listening to my ramblings. Now let's get to
why you're actually here, what is this thing and how does it work.

Simply put, it's a cli tool that allows you to enter your note/thought/reminder,
or whatever other names exist for the inner workings of your mind, followed by 
options for changing the storage directory(ies), filename, any subnotes you
would like to add to that note, or creating directories for more specific storage.
These files get stored as markdown with a simple
header for the note and unordered list items for the subnotes.

### "Okay, but what does this look like?"
Great question. Let's start with the basics:

#### Basic Note
```na "Remember to lookup argparse and click"```
This basic input will store the reminder in the default home/note_assistant/notes/na.md file path. It won't be super pretty, but that's not what this is for.

#### Note w/Custom directory and file names
```na "Random thought I had, that pertains to some other project" -d "path/to/my/other/project" -f "pertinent_thought"```
This input will allow you to direct your note storage to a specific project for
 you to easily reference later when you're working on that project.

Adding tags to the input will create subdirectories to store in a more specific 
location:
```na "Random project thought." -d "project/path" -t "new_project_folder" -t "relevant_tag_name"```

#### Adding Subnotes
```na "Info dump" -d "info_dump_dir" -s "Project idea one: ChatGPT wrapper that makes me money" -s "Project idea two: AI wrapper idea that will make me even more money -s "Project idea three: Databases...but with AI!```
This input will store a file named "na.md" in a "info_dump_dir" under your home path
that will contain the Info Dump note with all subnotes listed below it.

If later you would like to come back and add another note, or section, to this
file you can by doing the following:
```na "New Info dump" -d "info_dump_dir" -s "I wonder what the color blue would smell like, if colors had smells"```
This appends the new note and any subnotes to the na.md file within info_dump_dir

You can also come back and add a subnote to the original note within the file:
```na "Info dump" -d "info_dump_dir" -s "New Idea: Quit Programming and be a farmer. I can't buy food, but maybe I can grow it."```
This will edit the original subnote section, without removing any of the notes below.

## Future
Not really sure if I'll keep this project live, or not. I enjoyed working on it
for myself, and I really did (eventually) decide I just wanted, or even needed,
to tone down and keep it extremely simple.

This was the first, big, solo project I have ever done. So even though it probably
is crappy and stupid for most people, I'm satisified, currently. Eventually, I may
come back add some features, or change some things, but we'll see.

## Feedback
Please provide any feedback you have. Good or bad, I know I need to grow and 
learn, so don't hold back! I just ask for the feedback to at least be kind, if
possible. :D

Any ideas you have on what could be added, or if you would like to collaborate,
I'd love to hear from you, thanks!
