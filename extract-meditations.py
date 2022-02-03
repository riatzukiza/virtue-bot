import os

import nltk

nltk.download('punkt')

divider_sequence = "----------------------------------------------------------------------"

with open("meditations.mb.txt", "r+") as meditations:
    # os.mkdir("./meditations.section")
    text = meditations.read().replace("\n", ' ').strip()
    # sections = text.split(divider_sequence)
    # i=0

    tokens = nltk.sent_tokenize(text)
    with open('./mediations.sentances.txt','w') as sentance_file:
        for token in tokens:
            sentance_file.write(token)
            sentance_file.write("\n")

    # for section in sections:
    #     i+=1

    #     with open(os.path.join('./meditations', f'section-{i}.raw.txt'),'w') as section_file:
    #         section_file.write(section)
    #         section_file.close()

