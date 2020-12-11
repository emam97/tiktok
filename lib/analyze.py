import json
import sys
import re

input_file = sys.argv[1]

print("Parsing data...")

rejected = 0
likes = 0
matches = 0
chats = 0
u_ghosted = 0
unrequited_love = 0
they_dunk = 0
they_ghosted = 0
u_dunk = 0
total_interactions = 0
numbers_sent = 0

# Thanks to StackOverflow for this regex for phone numbers
# https://stackoverflow.com/a/16702965/1031615
phone_regex = '^.*\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*'

with open(input_file, 'r') as f:
    data = json.load(f)
    for blob in data:
        interactions = list(blob.keys())
        first_interaction = interactions[0]
        if len(interactions) > 1:
            second_interaction = interactions[1]
        else:
            second_interaction = 'noop'
        total_interactions += 1
        if first_interaction == 'block':
            rejected += 1
        elif first_interaction == 'like':
            likes += 1
            if second_interaction == 'match':
                matches += 1
                u_ghosted += 1
                u_dunk +=1
        elif first_interaction == 'match':
            matches += 1
            they_dunk += 1
            they_ghosted += 1
        elif first_interaction == 'chats':
            chats += 1
            if second_interaction == 'like':
                likes += 1
                matches += 1
                u_dunk +=1
            elif second_interaction == 'match':
                matches += 1
                they_dunk += 1
            for c in blob['chats']:
                if bool(re.search(phone_regex, c['body'])):
                    numbers_sent += 1
                    break

tot_string = "You've interacted with " + str(total_interactions) + " people on Hinge \n"
rej_string = "You've rejected " + str(rejected) + " people (ouch) \nYou match with " + str(matches/total_interactions * 100) + "% of profiles you see on Hinge.\n"
tot_ghost_string = "You've ghosted at least " + str(u_ghosted + they_ghosted) + ", or at least " + str((u_ghosted+they_ghosted)/matches * 100) + "% of all the people you match with\n"
u_ghost_string = "Total you've dropped the ball: " + str(u_ghosted) + " (you sent a like and they matched, no chatting) \n"
they_ghost_string = "Total they've dropped the ball " + str(they_ghosted) + " (they sent a like and you matched, no chatting) \n"
they_dunk_string = "Total shots they've shot and scored: " + str(they_dunk) + " (they sent a like and you matched) \n"
u_dunk_string = "Total shots you've shot and scored: " + str(u_dunk) + " (you sent a like and they matched) \n"
tot_likes = "Total shots you've shot: " + str(likes) + " (you sent a like)\n"
tot_matches = "Total slam dunks: " + str(matches) + " (you've matched with someone or they've matched with you) \n"
tot_chats = "Total people you've blessed with your time: " + str(chats) + " (you sent a message at least once) \n"
tot_nubers = "You have sent a phone number to " + str(numbers_sent) + " people on Hinge \n"

analysis = tot_string + tot_likes + tot_matches + tot_chats
analysis += "\n------------- \n\n\n"
analysis += "Fun Stuff ~ \n\n"
analysis += rej_string + tot_ghost_string + u_ghost_string + they_ghost_string + they_dunk_string + u_dunk_string + tot_nubers


print("Analysis complete!")
print(analysis)