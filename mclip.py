#! python3
#mclip.py - A multi-clipboard program.

TEXT={
    'agree': '''yes, I agree. that sounds great to me.''',
    'busy': "Sorry, Can we do this later, maybe this week or next week?",
    'upsell':"""Would you consider making this a monthly donation?"""

}

import sys,pyperclip
if len(sys.argv)<2:
    print('Usage:python mclip.py[keyphrase]-copy phrase text')
    sys.exit()
keyphrase=sys.argv[1] # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f'You copied text from {keyphrase} to the clipboard!')
    
else:
        print("No key phrase with that name")