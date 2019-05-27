# Обрабатывающие функции

async def format_to_article(text):
    code_templates = {}
    while text.find('<code') > 0:
        start = text.find('<code')
        end = text.find('</code>')+7
        substr = text[start:end]
        code_templates[f'|code_template_{len(code_templates)+1}|'] = f'{substr}'
        text = text.replace(
            code_templates[f'|code_template_{len(code_templates)}|'],  # template
            f'|code_template_{len(code_templates)}|\n')                  # replace
    split_text = text.split('\n')
    start = 0
    for i in range(len(split_text)):
        for m in code_templates.keys():
            if split_text[i].find(m) != -1:
                if split_text[i].find(m) != 0:
                    sub = split_text[i][split_text[i].find(m):split_text[i].find(m)+len(m)]
                    if len(sub) == 0:
                        pass
                    else:
                        split_text[i] = f'<div>{split_text[i][start:split_text[i].find(m)]}</div>{sub}'
                else:
                    sub = split_text[i][split_text[i].find(m):len(m)]
                    if len(sub) == 0:
                        pass
                    else:
                        if split_text[i] != '':
                            split_text[i] = f'{sub}'
                        else:
                            pass
            else:
                pass
        if split_text[i].find('<div>') != -1:
            pass
        else:
            split_text[i] = split_text[i].strip()
            if split_text[i]=='':
                pass
            else:
                if split_text[i].find('|code_template_') == -1:
                    # print(f'ya {split_text[i]}')
                    split_text[i] = f'<div>{split_text[i]}</div>'
        # if split_text[i]=='':
        #     split_text.remove('')
    formatted = ''
    for item in split_text:
        formatted+= f'{item}\n'
    # print(formatted)
    for key, value in code_templates.items():
        formatted = formatted.replace(key, value)

    formatted = formatted.replace('\n', '<br>')

    # print(formatted)
    return formatted

def check_lesson_ids_on_update_task(lesson_id, lesson_linked_id):
    # last_cur_id = lesson_id
    # last_new_id = lesson_linked_id
    # print(f'{lesson_id}       {lesson_linked_id}')
    if lesson_id == lesson_linked_id:
        return True

def identicalChk(cur_post, upd_post, post_type):
    identical = False
    print('temp', cur_post)
    print('upd', upd_post)
    if post_type=='article':
        _temp_tags = []
        for i in upd_post['articleTags']:
            _temp_tags.append(i['name'])
        if cur_post[0][0] == upd_post['articleName'] and \
                        cur_post[0][1] == upd_post['articleDescription'] and \
                        cur_post[0][2] == upd_post['articleText'] and \
                        cur_post[0][3] == _temp_tags and \
                        cur_post[0][4] == upd_post['lang']:
            identical = True
    elif post_type=='lesson':
        _temp_tags = []
        for i in upd_post['lessonTags']:
            _temp_tags.append(i['name'])
        if cur_post[0][0] == upd_post['lessonName'] and \
                        cur_post[0][1] == upd_post['lessonDescription'] and \
                        cur_post[0][2] == upd_post['lessonText'] and \
                        cur_post[0][3] == _temp_tags and \
                        cur_post[0][4] == upd_post['lang']:
            identical = True
    elif post_type=='task':
        # print(f'{cur_post[0]} {upd_post["taskName"]} {cur_post[0]== upd_post["taskName"]}\n'
        #       f'{cur_post[1]} {upd_post["taskDescription"]} {cur_post[1]== upd_post["taskDescription"]}\n'
        #       f'{cur_post[2]} {upd_post["taskText"]} {cur_post[2]== upd_post["taskText"]}\n'
        #       f'{cur_post[3]} {upd_post["difficulty"]} {cur_post[3]== int(upd_post["difficulty"])}\n'
        #       f'{cur_post[4]} {upd_post["testInput"]} {cur_post[4]== upd_post["testInput"]}\n'
        #       f'{cur_post[5]} {upd_post["expectedOutput"]} {cur_post[5]== upd_post["expectedOutput"]}\n'
        #       f'{cur_post[6]} {upd_post["lang_name"]} {cur_post[6]== upd_post["lang_name"]}\n')
        if cur_post[0] == upd_post['taskName'] and \
                        cur_post[1] == upd_post['taskDescription'] and \
                        cur_post[2] == upd_post['taskText'] and \
                        cur_post[3] == int(upd_post['difficulty']) and \
                        cur_post[4] == upd_post['testInput'] and \
                        cur_post[5] == upd_post['expectedOutput'] and \
                        cur_post[6] == upd_post['lang_name']:
            if len(cur_post[7]) == len(upd_post['linkedLessons']):
                idx = 0
                for i in cur_post[7]:
                    if check_lesson_ids_on_update_task(i[0], upd_post['linkedLessons'][idx]['lesson_id']):
                        identical = True
                    else:
                        identical = False
                    idx += 1
            else:
                identical = False

    return identical