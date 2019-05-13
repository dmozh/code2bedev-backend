# Обрабатывающие функции

async def format_to_article(text):
    code_templates = {}
    # print(text)
    # text = text.replace(' \n', '\n')
    # text = text.replace('\n', '<br>')
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


# format_to_article(
#             "Такс, ща глянем че получится во первых <code class=python>print('пляшем')</code> fhfhfhfhfhfh"
#            "\nТеперь вот так<code class=python>print('продолжаем плясать')</code>       "
#            "\n<code class=python>print('надо тестануть че получится')</code>         Пробелов много не бывает          "
#            "\n<code class=python>print('пляшем')</code>повторимсячтобыпроверить"
#            "\nahhhhhhhhhhhahahhahahahahaha"
#            "\n<code class=python>print('тестик')</code>")

# i = input()
# print(i)