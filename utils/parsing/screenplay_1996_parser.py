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
        'scene_head': '<div type="scene" n="{0}">\n\t<head type="scene_heading">\n\t\t<stage type="environment">{1}</stage>\n\t\t<stage type="primary_location">{1}</stage>\n\t\t<stage type="time">{1}</stage>\n\t</head>\n',
        'character': '\t<sp>\n\t\t<speaker>{0}</speaker>\n\t\t<p>{1}</p>\n\t</sp>\n',
        'character_os': '\t<sp rend="{0}">\n\t\t<speaker>{1}</speaker>\n\t\t<p>{2}</p>\n\t</sp>\n',
        'setting': '\t<stage type="setting">{0}</stage>\n',
        'delivery': '\t\t<stage type="delivery">{0}</stage>\n',
        'p': '\t\t<p>{}</p>\n\t</sp>\n',
        'end': '\t<trailer>{}</trailer>'
    }

    patterns = {
        'the_end': (r'^[\n|\s]+?The End', 'end'),
        'character': (r'(?![^\n]*\()\t{3,}\t?\s+[A-Z|A-Z\.]{2,}', 'character'),
        'scene_head': (r'[\&\;\.\/A-Z\s\']+ - ?[A-Z\s\']', 'scene_head'),
        'charstage': (r'\t{2,}\t?\s+[A-Z|A-Z\.]{2,}.*\(.+', 'character_os'),
        'trail_p': (r'^[\t ]+.*', 'p'),
        'stage': (r'.*', 'setting'),
    }

    scene_count = 1
    scenes = re.split(r'\n(?=.*[A-Z]+ - (?:[A-Z].*)?)', html_content, flags=re.MULTILINE)

    for pre_tag in soup.find_all('pre'):
        for block in pre_tag:
            lines = block.split('\n')
            for en, (pattern, block) in patterns.items():
                match = (re.match(pattern, lines[0]), en)
                if match[0]:
                    break
            if match[1] == 'scene_head':
                if scene_count != 1:
                    xml_str += '</div>\n'
                xml_str += xml_blocks[block].format(scene_count, lines[0].strip())
                scene_count += 1
            elif match[1] == 'character':
                xml_str += xml_blocks[block].format(lines[0].strip(), ' '.join(map(str.strip, lines[1:])))
            elif match[1] == 'charstage':
                cs_pattern = r'([A-Z\s\']+)\s*\(([^)]+)\)'
                name, rend = re.findall(cs_pattern, lines[0])[0]
                xml_str += xml_blocks[block].format(rend.strip(), name.strip(), ' '.join(map(str.strip, lines[1:])))
            elif match[1] == 'stage':
                xml_str += xml_blocks[block].format(' '.join(map(str.strip, lines[0:])))
            elif match[1] == 'trail_p':
                previous_lines = xml_str.splitlines()[:-1]
                previous_lines.append(xml_blocks[block].format(' '.join(map(str.strip, lines[0:]))))
                xml_str = '\n'.join(previous_lines)
            else:
                print(match, lines)
                print('---')



    with open(destination_file, 'w') as xml_file:
        xml_str = xml_str.replace("&", "&amp;")
        xml_str += '</div>'
        xml_file.write(xml_str)
        print(scene_count)

if __name__ == "__main__":
    script = './The Kubrick Site_ The Eyes Wide Shut Screenplay.html'
    destination_file = './parsed_script_1996.xml'
    xml_parser(script, destination_file)

# Manual labour:
# Characters such as "BOTH" have to be manually replaced
#POSSIBLE MISSING PAGE has to be manually added
#_Possible scene_. has to be manually added
#italics (_#_) have to be manually tagged
#ex beauty queen
#shots to illustrate