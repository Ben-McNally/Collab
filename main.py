import sys

while True:
    command = input(": ")
    # example input: stab goblin with sword
    # we could split the command at the spaces take the first item which would be command an dthen work from there
    
    segments = command.split(" ")
    
    if segments[0] == "stab":
        pass
    elif segments[0] == "quit":
        sys.exit()

    
    # i was thinking more like 'fight'  + 'goblin'
    #yes, you would say: command fight goblin
    #or command open backpack
    # if input == 'example':
    #     example()