from bs4 import BeautifulSoup
import re
from pprint import pprint



def transcript_parser(script, destination_file):
    

    xml_str = ''

    xml_blocks = {
        'scene_head': '<div type="scene" n="{0}">\n\t<head type="scene_heading">\n\t\t<stage type="environment">{1}</stage>\n\t\t<stage type="primary_location">{2}</stage>\n\t\t<stage type="time">{3}</stage>\n\t</head>\n',
        'scene_head_secondary': '<div type="scene" n="{0}">\n\t<head type="scene_heading">\n\t\t<stage type="environment">{1}</stage>\n\t\t<stage type="secondary_location">{2}</stage>\n\t\t<stage type="primary_location">{3}</stage>\n\t\t<stage type="time">{4}</stage>\n\t</head>\n',
        'character': '\t<sp>\n\t\t<speaker>{0}</speaker>\n{1}\t</sp>\n',
        'character_os': '\t<sp rend="{0}">\n\t\t<speaker>{1}</speaker>\n{2}\t</sp>\n',
        'setting': '\t<stage type="setting">{0}</stage>\n',
        'delivery': '\t\t<stage type="delivery">{0}</stage>\n'
    }

    patterns = {
        'scene_head_secondary': (r'^(\d+)\. (\w+\.) (.+) - (.+) - (\w+)', 'scene_head_secondary'),
        'scene_head': (r'^(\d+)\. (\w+\.) (.+) - (\w+)', 'scene_head'),
        'character': (r"^[A-Z\s\d']+(?: \(o/s\)|\(v/o\))?$", 'character'),
    }

    with open(script, 'r') as html_file:
        html_content = html_file.read()
        scenes = re.split(r'\n\n(?=\d+\.)', html_content, flags=re.MULTILINE)

        for scene in scenes:
            print('-----------')
            blocks = scene.split('\n\n')
            for block in blocks:
                lines = block.split('\n')
                for en, (pattern, xml_block) in patterns.items():
                    match = (re.match(pattern, lines[0]), en)
                    if match[0]:
                        break
                print(lines)
                if match[0] and match[1] == 'scene_head_secondary':
                    xml_str += xml_blocks[xml_block].format(match[0].groups()[0], match[0].groups()[1], match[0].groups()[2], match[0].groups()[3], match[0].groups()[4])
                elif match[0] and match[1] == 'scene_head':
                    xml_str += xml_blocks[xml_block].format(match[0].groups()[0], match[0].groups()[1], match[0].groups()[2], match[0].groups()[3])
                elif match[0] and match[1] == 'character':
                    speaker = lines[0]
                    sp = ''
                    dialogue = ''
                    for line in lines[1:]:
                        if line.startswith('('):
                            sp += xml_blocks['delivery'].format(line)
                            if dialogue != '':
                                sp += f'\t\t<p>{dialogue.strip()}</p>\n'
                                dialogue = ''
                        else:
                            dialogue += line + ' '
                    sp += f'\t\t<p>{dialogue.strip()}</p>\n'
                    if '(' in speaker:
                        st = speaker.split(' ')
                        xml_str += xml_blocks['character_os'].format(st[1], st[0], sp)
                    else:
                        xml_str += xml_blocks[xml_block].format(speaker, sp)
                else:
                    xml_str += xml_blocks['setting'].format(' '.join(lines))


                
            xml_str += '</div>\n'


    with open(destination_file, 'w') as xml_file:
        xml_str = xml_str.replace("&", "&amp;")
        xml_file.write(xml_str)

if __name__ == "__main__":
    script = './src/eyes-wide-shut-1999-transcription.txt'
    destination_file = './parsed_transcription.xml'
    transcript_parser(script, destination_file)