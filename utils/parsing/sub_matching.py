from bs4 import BeautifulSoup
from thefuzz import fuzz
from thefuzz import process
import re
from bs4.formatter import HTMLFormatter

class UnsortedAttributes(HTMLFormatter):
    def attributes(self, tag):
        for k, v in tag.attrs.items():
            yield k, v



with open('./eyes-wide-shut-1999-transcription.xml', 'r') as xml_file:
    xml_content = xml_file.read()

with open('./src/Eyes.Wide.Shut.1999.1080p.BluRay.x264.YIFY.srt', 'r') as sub_file:
    subs = sub_file.read()

soup = BeautifulSoup(xml_content, 'xml')
body = soup.find('body')
ps = [p for p in body.find_all('p')]
sps = [sp for sp in body.find_all('sp')[220:]]

subl = subs.split('\n\n')
subd = {' '.join(sub.split('\n')[2:]).strip('<i/>'): (sub.split('\n')[0],sub.split('\n')[1]) for sub in subl}

subs = [
    ' '.join(subl[idx].split('\n')[2:]).strip('<i/>')
    for idx, sub in enumerate(subl)
]

merged_subs = []
merge_buffer = []

for sub in subs:
    if sub.endswith('...'):
        merge_buffer.append(sub)
    elif merge_buffer:
        merge_buffer.append(sub)
        merged_subs.append('#'.join(merge_buffer))
        merge_buffer = []
    else:
        merged_subs.append(sub)

if merge_buffer:
    merged_subs.append('#'.join(merge_buffer))

for sp in sps:
    line1 = sp.find('p').text.strip()

    if process.extractOne(line1, merged_subs)[1] >= 95:
        if '#' in process.extractOne(line1, merged_subs)[0]:
            lines = process.extractOne(line1, merged_subs)[0].split('#')
            sub_num = subd[lines[0]][0]
            time1 = subd[lines[0]][1].replace(',', '.').split(' --> ')[0]
            time2 = subd[lines[-1]][1].replace(',', '.').split(' --> ')[1]
            line_start = time1
            line_end = time2
            block = BeautifulSoup(f'''
                    <timeline xml:id="SUB{sub_num}">
                        <when xml:id="line_start" absolute="{line_start}"/>
                        <when xml:id="line_end" absolute="{line_end}"/>
                    </timeline>\n''', 'xml')
            old = sp.find('timeline')
            old.replace_with(block)
            merged_subs.remove(process.extractOne(line1, merged_subs)[0])
        else:
            line = process.extractOne(line1, merged_subs)[0]
            sub_num = subd[line][0]
            time = subd[line][1].replace(',', '.').split(' --> ')
            line_start = time[0]
            line_end = time[1]
            block = BeautifulSoup(f'''
                    <timeline xml:id="SUB{sub_num}">
                        <when xml:id="line_start" absolute="{line_start}"/>
                        <when xml:id="line_end" absolute="{line_end}"/>
                    </timeline>\n''', 'xml')
            old = sp.find('timeline')
            old.replace_with(block)
            merged_subs.remove(line)
    else:
        if line1.endswith('saying?'):
            print(line1)
            print(process.extractOne(line1, merged_subs))
        blockù = BeautifulSoup(f'''
                <timeline xml:id="SUB">
                    <when xml:id="line_start" absolute=""/>
                    <when xml:id="line_end" absolute=""/>
                </timeline>\n''', 'xml')
        old = sp.find('timeline')
        old.replace_with(blockù)

with open('timestamp_xml.xml', 'w') as xml_file:
    xml_content = soup.encode(formatter=UnsortedAttributes()).decode('utf-8').replace('&', '&amp;')
    xml_file.write(xml_content)
    print(process.extractOne("So, when you are feeling tits it's nothing more than your professionalism, is that what you're saying?", merged_subs))
    print(merged_subs[250:270])