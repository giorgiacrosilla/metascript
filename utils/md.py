from bs4 import BeautifulSoup
import re



def xml_parser(script, destination_file):
    with open(script, 'r', errors='ignore') as html_file:
        html_content = html_file.read()
        #substitute the '------'
        html_content = re.sub(r'\n---+\n', r'</pre>\n<pre>', html_content)
        html_content = re.sub(r'<pre>--+\n', r'<pre>', html_content)
    

    soup = BeautifulSoup(html_content, 'html.parser')

    xml_str = ''

    xml_blocks = {
        'speech': '''\t<sp who="#{0}">\n\t\t<speaker>{0}</speaker>\n\t\t<p>{1}</p>\n\t</sp>\n''',
        'charstage': '''\t<sp who="#{0}">\n\t\t<speaker>{0}</speaker>\n\t\t<stage type="delivery">{1}</stage>\n\t\t<p>{2}</p>\n\t</sp>\n''',
        'stage': '\t<stage type="#replace">{}</stage>\n',
        'p': '\t\t<p>{}</p>\n\t</sp>\n',
        'location': '\t<set>\n\t\t<p>{}</p>\n\t</set>\n',
        'end': '\t<trailer>{}</trailer>'
    }

    patterns = {
        'the_end': (r'^[\n|\s]+?The End', 'end'),
        'character': (r'(?![^\n]*\()\t{3,}t?\s+[A-Z|A-Z\.]{2,}+', 'speech'),
        'location': (r'^[A-Z].+?-', 'location'),
        'stage': (r'^\w.*', 'stage'),
        'charstage': (r'\t{2,}\t?\s+[A-Z|A-Z\.]{2,}.*\(+', 'charstage'),
        'trail_p': (r'^[\t\t]{1,}\s+?.*', 'p')
    }

    scene_count = 1

    for pre_tag in soup.find_all('pre'):
        for block in pre_tag:
            lines = block.split('\n')
            for en, (pattern, block) in patterns.items():
                match = (re.match(pattern, lines[0]), en)
                if match[0]:
                    break
            if match[1] == 'character':
                xml_str += xml_blocks[block].format(lines[0].strip(), ' '.join(map(str.strip, lines[1:])))
            elif match[1] == 'stage':
                xml_str += xml_blocks[block].format(' '.join(map(str.strip, lines[0:])))
            elif match[1] == 'location':
                if scene_count == 1:
                    xml_str += f'<div type="scene" n="{scene_count}">\n' + xml_blocks[block].format(lines[0].strip()) + '\n'
                else:
                    xml_str += f'</div>\n<div type="scene" n="{scene_count}">\n' + xml_blocks[block].format(lines[0].strip())
                scene_count += 1
            elif match[1] == 'charstage':
                xml_str += xml_blocks[block].format(lines[0].strip().split(' (')[0],'(' + lines[0].strip().split(' (')[1],' '.join(map(str.strip, lines[1:])))
            elif match[1] == 'trail_p':
                previous_lines = xml_str.splitlines()[:-1]
                previous_lines.append(xml_blocks[block].format(' '.join(map(str.strip, lines[0:]))))
                xml_str = '\n'.join(previous_lines)
            elif match[1] == 'the_end':
                xml_str += xml_blocks[block].format(lines[0].strip())
            
            else:
                print(lines)
                print('no match\n')



    with open(destination_file, 'w') as xml_file:
        xml_file.write(xml_str)

    print("XML file generated successfully!")



if __name__ == "__main__":
    script = './0085.html'
    destination_file = './parsed_xml.xml'
    xml_parser(script, destination_file)

# Manual labour:
# Characters such as "BOTH" have to be manually replaced
#POSSIBLE MISSING PAGE has to be manually added
#_Possible scene_. has to be manually added
#italics (_#_) have to be manually tagged
#pages have to be manually dealt with
#stage's #replace has to be manually replaced
#ex beauty queen
#close the last div