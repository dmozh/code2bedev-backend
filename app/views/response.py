from aiohttp import web
import json
# from app import sql_requests
from .sql_handler import handle
import requests, credentials
from .processings_functions import format_to_article, check_lesson_ids_on_update_task as chk_ids

# TODO выделить общие части и вынести в отдельный класс
# TODO сделать хотя бы базовое шифрование и дешифрование передавеммых данных
async def test(request):
    # result = await handle(req='test')
    # print(result)
    # users = []
    # j_response = {}
    # if result != psycopg2.Error:
    #     for i in result:
    #         j_string = {"user": {"id": i[0], "role_id": i[1], "user_name": i[2], "user_email": 's00per s3cr3t', "user_rate": i[4]}}
    #         users.append(j_string)
    #
    # j_response["users"]=users
    # print(request.method)
    headers = {'Access-Control-Allow-Origin': '*', 'content-type': 'text/html'}
    # response = "<div><p><b>kokoko</b></p></div>"
    response = '<script>alert("aoaoaao")</script>'
    return web.Response(body=response, headers=headers)


async def add_article(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        # ответное сообщение
        response_msg = {}

        # get body req
        post = await request.json()
        print(post)

        article_lang = post['lang']
        article_name = post['articleName']
        article_description = post['articleDescription']
        article_text = post['articleText']
        article_rate = 0
        author_email = post['authorEmail']
        article_tags = []

        for i in post['articleTags']:
            article_tags.append(i['name'])
        print(article_tags)
        result = await handle(req='add_article', article_lang=article_lang, article_name=article_name, article_description=article_description,
                        article_text=article_text, article_rate=article_rate, author_email=author_email,article_tags=article_tags)
        response_msg['msg'] = result

        return web.json_response(response_msg, headers=headers)
    else:
        return web.Response(text='get', headers=headers)

async def add_news(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        # ответное сообщение
        response_msg = {}

        # get body req
        post = await request.json()
        print(post)

        news_importance = post['importance']
        news_name = post['newsName']
        news_description = post['newsDescription']
        news_text = post['newsText']
        news_rate = 0
        author_email = post['authorEmail']
        news_tags = []

        for i in post['newsTags']:
            news_tags.append(i['name'])
        print(news_tags)
        result = await handle(req='add_news', news_name=news_name, news_description=news_description, news_text=news_text, news_rate=news_rate, user_email=author_email, news_tags=news_tags, news_importance=news_importance)
        response_msg['msg'] = result
        return web.json_response(response_msg, headers=headers)
    else:
        return web.Response(text='get', headers=headers)

async def add_task(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        # ответное сообщение
        response_msg = {}

        # get body req
        post = await request.json()
        print(post)

        lang_id = post['lang_id']
        task_name = post['taskName']
        task_description = post['taskDescription']
        task_text = post['taskText']
        task_test_input = post['testInput']
        task_expected_output = post['expectedOutput']
        task_rate = 0
        author_email = post['authorEmail']
        task_difficulty = post['difficulty']
        linked_lessons = post['linkedLessons']
        result = await handle(req='add_task', task_name=task_name, lang_id=lang_id,
                        task_description=task_description,
                        task_text=task_text, task_rate=task_rate, author_email=author_email,
                        task_difficulty=task_difficulty, task_test_input=task_test_input, task_expected_output=task_expected_output)
        if result:
            for lesson in linked_lessons:
                await handle(req='link_lessons_to_tasks', lesson_id=lesson['lesson_id'], task_name=task_name)
        response_msg['msg'] = result
        return web.json_response(response_msg, headers=headers)
    else:
        return web.Response(text='get', headers=headers)

async def add_lesson(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        # ответное сообщение
        response_msg = {}

        # get body req
        post = await request.json()
        print(post)

        lesson_lang = post['lang']
        lesson_name = post['lessonName']
        lesson_description = post['lessonDescription']
        lesson_text = post['lessonText']
        lesson_rate = 0
        author_email = post['authorEmail']
        lesson_tags = []

        for i in post['lessonTags']:
            lesson_tags.append(i['name'])
        print(lesson_tags)
        if len(post['lessonTasks']) > 0:
            print(post['lessonTasks'])
            result = await handle(req='add_lesson', lesson_lang=lesson_lang, lesson_name=lesson_name,
                        lesson_description=lesson_description,
                        lesson_text=lesson_text, lesson_rate=lesson_rate, author_email=author_email,
                        lesson_tags=lesson_tags)
            if result:
                lesson_id = await handle(req='get_lesson_id', lesson_name=lesson_name)
                for item in post['lessonTasks']:
                    result = await handle(req='add_task', lang_id=lesson_lang, task_name=item['taskName'],
                                task_description=item['taskDescription'],
                                task_text=item['taskText'], task_rate=0, author_email=author_email,
                                task_difficulty=item['taskDifficulty'], task_test_input=item['taskTestInput'], task_expected_output=item['taskExpectedOutput'])
                    if result:
                        await handle(req='link_lessons_to_tasks', lesson_id=lesson_id[0][0], task_name=item['taskName'])

        else:
            print('else')
            result = await handle(req='add_lesson', lesson_lang=lesson_lang, lesson_name=lesson_name,
                        lesson_description=lesson_description,
                        lesson_text=lesson_text, lesson_rate=lesson_rate, author_email=author_email,
                        lesson_tags=lesson_tags)
            response_msg['msg'] = result

        return web.json_response(response_msg, headers=headers)
    else:
        return web.Response(text='get', headers=headers)

async def add_user(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        #ответное сообщение
        response_msg = {}

        #get body req
        post = await request.json()

        user_name    = post['userName']
        user_email   = post['userEmail']

        result = await handle(req='get_valid_name', user_name=user_name, user_email=user_email)
        if result['valid']:
            user_rate = 0
            result = await handle(req='add_user', user_name=user_name, user_email=user_email, user_rate=user_rate)
            response_msg['valid'] = True
            response_msg['msg'] = result
        else:
            response_msg['valid'] = result['valid']
            response_msg['msg']   = result['msg']
        return web.json_response(response_msg, headers=headers)
    else:
        return web.Response(text='get', headers=headers)

async def get_valid_name(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        # ответное сообщение
        response_msg = {}

        # get body req
        post = await request.json()

        user_name = post['userName']
        user_email = post['userEmail']

        result = await handle(req='get_valid_name', user_name=user_name, user_email=user_email)
        if result[0][0]==True and result[0][1]==True:
            user_rate = 0
            result = await handle(req='add_user', user_name=user_name, user_email=user_email, user_rate=user_rate)
            response_msg['valid'] = True
            response_msg['msg'] = result
        else:
            response_msg['valid'] = False
        return web.json_response(response_msg, headers=headers)

async def update_user_article(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        # ответное сообщение
        response_msg = {}

        # get body req
        post = await request.json()
        print(post)

        article_lang = post['lang']
        article_name = post['articleName']
        article_description = post['articleDescription']
        article_text = post['articleText']
        article_id = post['articleId']
        article_tags = []

        for i in post['articleTags']:
            article_tags.append(i['name'])
        result = await handle(req='update_article',
                              article_name=article_name,
                              article_description=article_description,
                              article_text=article_text,
                              article_lang=article_lang,
                              article_tags=article_tags,
                              article_id=article_id)
        response_msg['msg'] = result

        return web.json_response(response_msg, headers=headers)
    else:
        return web.Response(text='get', headers=headers)

async def update_user_news(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        # ответное сообщение
        response_msg = {}

        # get body req
        post = await request.json()
        print(post)

        news_name = post['newsName']
        news_description = post['newsDescription']
        news_text = post['newsText']
        news_id = post['newsId']
        news_importance=post['importance']
        news_tags = []

        for i in post['newsTags']:
            news_tags.append(i['name'])
        print(news_tags)
        result = await handle(req='update_news', news_name=news_name,
                              news_description=news_description,
                              news_text=news_text,
                              news_importance=news_importance,
                              news_tags=news_tags,
                              news_id=news_id)
        response_msg['msg'] = result

        return web.json_response(response_msg, headers=headers)
    else:
        return web.Response(text='get', headers=headers)

async def update_user_task(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        # ответное сообщение
        response_msg = {}

        # get body req
        post = await request.json()
        print(post)

        lang_name = post['lang_name']
        task_id = post['taskId']
        task_name = post['taskName']
        task_description = post['taskDescription']
        task_text = post['taskText']
        task_difficulty = post['difficulty']
        task_test_input = post['testInput']
        task_expected_output = post['expectedOutput']
        linked_lessons = post['linkedLessons']

        result = await handle(req='update_task', task_name=task_name,
                              task_description=task_description,
                              task_text=task_text,
                              lang_name=lang_name,
                              task_difficulty=task_difficulty,
                              task_id=task_id,
                              task_test_input=task_test_input,
                              task_expected_output=task_expected_output)
        if result:
            lessons_ids = await handle(req='get_links_tasks_to_lessons', task_id=task_id)

            print(lessons_ids)
            print(linked_lessons)
            if not lessons_ids:
                print('net linkov')
                for lesson in linked_lessons:
                    await handle(req='link_lessons_to_tasks', lesson_id=lesson['lesson_id'], task_name=task_name)
            else:
                if linked_lessons:
                    length_cur_ids = len(lessons_ids)
                    length_new_ids = len(linked_lessons)
                    if length_cur_ids == length_new_ids:
                        for i in range(length_cur_ids):
                            print(i)
                            print(f'{lessons_ids[i][0]} {linked_lessons[i]["lesson_id"]}')
                            if chk_ids(lessons_ids[i][0], linked_lessons[i]['lesson_id']):
                                print('ravni')
                            else:
                                print('neravni')
                                await handle(req='update_link_task_to_lesson', lesson_id=lessons_ids[i][0], task_id=task_id,
                                             new_l_id=linked_lessons[i]['lesson_id'])
                    else:
                        if length_cur_ids>length_new_ids:
                            for i in range(length_cur_ids):
                                try:
                                    print(f'{lessons_ids[i][0]} {linked_lessons[i]["lesson_id"]}')
                                    if chk_ids(lessons_ids[i][0], linked_lessons[i]['lesson_id']):
                                        print('ravni')
                                    else:
                                        print('neravni')
                                        await handle(req='update_link_task_to_lesson', lesson_id=lessons_ids[i][0],
                                                     task_id=task_id, new_l_id=linked_lessons[i]['lesson_id'])
                                except IndexError as e:
                                    print(e)
                                    print(f'delete {lessons_ids[i][0]}')
                                    await handle(req='delete_link_task_to_lesson', lesson_id=lessons_ids[i][0], task_id=task_id)
                        else:
                            for i in range(length_new_ids):
                                try:
                                    print(f'{lessons_ids[i][0]} {linked_lessons[i]["lesson_id"]}')
                                    if chk_ids(lessons_ids[i][0], linked_lessons[i]['lesson_id']):
                                        print('ravni')
                                    else:
                                        print('neravni')
                                        await handle(req='update_link_task_to_lesson', lesson_id=lessons_ids[i][0],
                                                     task_id=task_id, new_l_id=linked_lessons[i]['lesson_id'])
                                except IndexError as e:
                                    print(e)
                                    print(f'add {linked_lessons[i]["lesson_id"]}')
                                    await handle(req='link_lessons_to_tasks', lesson_id=linked_lessons[i]["lesson_id"],
                                                 task_name=task_name)
                else:
                    for l_id in lessons_ids:
                        await handle(req='delete_link_task_to_lesson', lesson_id=l_id[0], task_id=task_id)
                    print('delete links')
        response_msg['msg'] = result

        return web.json_response(response_msg, headers=headers)
    else:
        return web.Response(text='get', headers=headers)

async def update_user_lesson(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        # ответное сообщение
        response_msg = {}

        # get body req
        post = await request.json()
        print(post)

        lesson_lang = post['lang']
        lesson_name = post['lessonName']
        lesson_description = post['lessonDescription']
        lesson_text = post['lessonText']
        lesson_id = post['lessonId']
        lesson_tags = []

        for i in post['lessonTags']:
            lesson_tags.append(i['name'])
        print(lesson_tags)
        result = await handle(req='update_lesson', lesson_name=lesson_name,
                              lesson_description=lesson_description,
                              lesson_text=lesson_text,
                              lesson_lang=lesson_lang,
                              lesson_tags=lesson_tags,
                              lesson_id=lesson_id)
        response_msg['msg'] = result

        return web.json_response(response_msg, headers=headers)
    else:
        return web.Response(text='get', headers=headers)

async def delete_user_article(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        # ответное сообщение
        response_msg = {}

        # get body req
        post = await request.json()
        print(post)

        article_id = post['articleId']
        author = post['authorName']

        result = await handle(req='delete_article',
                              article_id=article_id,
                              author=author)
        response_msg['msg'] = result

        return web.json_response(response_msg, headers=headers)
    else:
        return web.Response(text='get', headers=headers)

async def delete_user_news(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        # ответное сообщение
        response_msg = {}

        # get body req
        post = await request.json()
        print(post)

        news_id = post['newsId']
        author = post['authorName']

        result = await handle(req='delete_news',
                              news_id=news_id,
                              author=author)
        response_msg['msg'] = result

        return web.json_response(response_msg, headers=headers)
    else:
        return web.Response(text='get', headers=headers)

async def delete_user_task(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        # ответное сообщение
        response_msg = {}

        # get body req
        post = await request.json()
        print(post)

        task_id = post['taskId']
        author = post['authorName']

        result = await handle(req='delete_task',
                              task_id=task_id,
                              author=author)
        response_msg['msg'] = result

        return web.json_response(response_msg, headers=headers)
    else:
        return web.Response(text='get', headers=headers)

async def delete_user_lesson(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        # ответное сообщение
        response_msg = {}

        # get body req
        post = await request.json()
        print(post)

        lesson_id = post['lessonId']
        author = post['authorName']

        result = await handle(req='delete_lesson',
                              lesson_id=lesson_id,
                              author=author)
        response_msg['msg'] = result

        return web.json_response(response_msg, headers=headers)
    else:
        return web.Response(text='get', headers=headers)

async def get_user(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        response_msg = {}

        # get body req
        post = await request.json()
        user_email = post['email']

        print(request.method)
        print(post)
        result = await handle(req='get_user', user_email=user_email)
        user_id = result[0][0]
        seen_tasks_result       = await handle(req='get_seen_tasks',    user_id=user_id)
        seen_lessons_result     = await handle(req='get_seen_lessons',  user_id=user_id)
        seen_articles_result    = await handle(req='get_seen_articles', user_id=user_id)
        seen_news_result        = await handle(req='get_seen_news',     user_id=user_id)

        seen_tasks_temp = []
        seen_lessons_temp = []
        seen_articles_temp = []
        seen_news_temp = []
        seen_posts = {}
        for i in seen_tasks_result:
            temp = {'user_id': i[0], 'task_id': i[1], 'isSeen': i[2], 'isDecided': i[3], 'upVote': i[4], 'downVote': i[5]}
            seen_tasks_temp.append(temp)
        for i in seen_lessons_result:
            temp = {'user_id': i[0], 'lesson_id': i[1], 'isSeen': i[2], 'upVote': i[3], 'downVote': i[4]}
            seen_lessons_temp.append(temp)
        for i in seen_articles_result:
            temp = {'user_id': i[0], 'article_id': i[1], 'isSeen': i[2], 'upVote': i[3], 'downVote': i[4]}
            seen_articles_temp.append(temp)
        for i in seen_news_result:
            temp = {'user_id': i[0], 'news_id': i[1], 'isSeen': i[2], 'upVote': i[3], 'downVote': i[4]}
            seen_news_temp.append(temp)

        seen_posts['tasks'] = seen_tasks_temp
        seen_posts['lessons'] = seen_lessons_temp
        seen_posts['articles'] = seen_articles_temp
        seen_posts['news'] = seen_news_temp
        if result != 'err':
            response_msg['user'] = {"id": user_id, "role_id": result[0][1], "user_name": result[0][2],
                                "user_email": 's00per s3cr3t =)', "user_rate": result[0][4], "seenPosts": seen_posts}
        else:
            response_msg['err']='err'
        return web.json_response(response_msg, headers=headers)

async def get_langs_name(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    response_msg = {}

    langs_name = []

    result = await handle(req='get_langs_name')
    for item in result:
        j_string = {"lang_id": item[0], "lang_name": item[1]}
        langs_name.append(j_string)

    response_msg['langs_name'] = langs_name
    return web.json_response(response_msg, headers=headers)

async def get_langs(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    response_msg = {}
    langs = []

    result = await handle(req='get_langs')
    for item in result:
        j_string = {"lang_id": item[0], "lang_name": item[1], "lang_description": item[2], "lang_rate": item[3]}
        langs.append(j_string)

    response_msg['langs'] = langs
    print(response_msg)
    return web.json_response(response_msg, headers=headers)

async def get_user_lessons_name(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        response_msg = {}

        # get body req
        post = await request.json()
        user_email = post['authorEmail']
        lang = post['lang']

        print(request.method)
        print(post)
        result = await handle(req='get_user_lessons_name', user_email=user_email, lang=lang)
        lessons=[]

        if result != 'err':
            for i in result:
                j_string = {"id": i[0], "lesson_name": i[1]}
                lessons.append(j_string)
        else:
            response_msg['err'] = 'err'

        response_msg['lessons'] = lessons

        return web.json_response(response_msg, headers=headers)

async def get_user_lessons(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        response_msg = {}

        # get body req
        post = await request.json()
        user_email = post['authorEmail']

        print(request.method)
        print(post)
        result = await handle(req='get_user_lessons', user_email=user_email)
        lessons = []

        if result != 'err':
            for i in result:
                j_string = {"lesson_id": i[0], "lesson_name": i[1], "lesson_description": i[2], "lesson_text": i[3],
                            "lesson_rate": i[4], "lesson_tags": i[5], "lang_id": i[6], "lang_name": i[7]}
                lessons.append(j_string)
        else:
            response_msg['err'] = result

        response_msg['lessons'] = lessons

        return web.json_response(response_msg, headers=headers)

async def get_user_tasks(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        response_msg = {}

        # get body req
        post = await request.json()
        user_email = post['authorEmail']

        print(request.method)
        print(post)
        result = await handle(req='get_user_tasks', user_email=user_email)
        tasks = []

        if result != 'err':
            for i in result:
                j_string = {"task_id": i[0], "task_name": i[1], "task_description": i[2], "task_text": i[3],
                            "task_rate": i[4], "task_difficulty": i[5], "test_input": i[6], "expected_output": i[7],
                            "lang_id": i[8], "lang_name": i[9]}
                tasks.append(j_string)
        else:
            response_msg['err'] = result

        response_msg['tasks'] = tasks

        return web.json_response(response_msg, headers=headers)

async def get_user_news(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        response_msg = {}

        # get body req
        post = await request.json()
        user_email = post['authorEmail']

        print(request.method)
        print(post)
        result = await handle(req='get_user_news', user_email=user_email)
        news = []

        if result != 'err':
            for i in result:
                j_string = {"news_id": i[0], "news_name": i[1], "news_description": i[2], "news_text": i[3],
                            "news_rate": i[4], "news_tags": i[5], "news_importance": i[6]}
                news.append(j_string)
        else:
            response_msg['err'] = result

        response_msg['news'] = news

        return web.json_response(response_msg, headers=headers)

async def get_user_articles(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        response_msg = {}

        # get body req
        post = await request.json()
        user_email = post['authorEmail']

        print(request.method)
        print(post)
        result = await handle(req='get_user_articles', user_email=user_email)
        articles = []

        if result != 'err':
            for i in result:
                j_string = {"article_id": i[0], "article_name": i[1], "article_description": i[2], "article_text": i[3],
                            "article_rate": i[4], "article_tags": i[5], "lang_id": i[6], "lang_name": i[7]}
                articles.append(j_string)
        else:
            response_msg['err'] = result

        response_msg['articles'] = articles

        return web.json_response(response_msg, headers=headers)

async def get_user_posts(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        response_msg = {}

        articles = []
        lessons = []
        tasks = []
        news = []

        # get body req
        post = await request.json()
        user_email = post['authorEmail']

        print(request.method)
        print(post)
        ################################################ get articles #########################################################################
        result = await handle(req='get_user_articles', user_email=user_email)
        if result != 'err':
            for i in result:
                j_string = {"article_id": i[0], "article_name": i[1], "article_description": i[2], "article_text": i[3],
                            "article_rate": i[4], "article_tags": i[5], "lang_id": i[6], "lang_name": i[7]}
                articles.append(j_string)
        else:
            response_msg['err'] = result
        response_msg['articles'] = articles
        ############################################### get news #####################################################################################
        result = await handle(req='get_user_news', user_email=user_email)
        if result != 'err':
            for i in result:
                j_string = {"news_id": i[0], "news_name": i[1], "news_description": i[2], "news_text": i[3],
                            "news_rate": i[4], "news_tags": i[5], "news_importance": i[6]}
                news.append(j_string)
        else:
            response_msg['err'] = result
        response_msg['news'] = news
        ############################################## get tasks ######################################################################################
        result = await handle(req='get_user_tasks', user_email=user_email)
        if result != 'err':
            for i in result:
                lessons_ids = await handle(req='get_links_tasks_to_lessons', task_id=i[0])
                links_lessons = []
                for l_id in lessons_ids:
                    l_name = await handle(req='get_lesson_name', lesson_id=l_id[0])
                    _temp = {'lesson_id': l_id[0], 'lesson_name': l_name[0][0]}
                    links_lessons.append(_temp)
                j_string = {"task_id": i[0], "task_name": i[1], "task_description": i[2], "task_text": i[3],
                            "task_rate": i[4], "task_difficulty": i[5], "test_input": i[6], "expected_output": i[7],
                            "lang_id": i[8], "lang_name": i[9], "lessons": links_lessons}
                # print(j_string)
                tasks.append(j_string)
        else:
            response_msg['err'] = result
        response_msg['tasks'] = tasks
        ################################################ get lessons ##################################################################################
        result = await handle(req='get_user_lessons', user_email=user_email)
        if result != 'err':
            for i in result:
                j_string = {"lesson_id": i[0], "lesson_name": i[1], "lesson_description": i[2], "lesson_text": i[3],
                            "lesson_rate": i[4], "lesson_tags": i[5], "lang_id": i[6], "lang_name": i[7]}
                lessons.append(j_string)
        else:
            response_msg['err'] = result
        response_msg['lessons'] = lessons

        response = {'posts': response_msg}

        return web.json_response(response, headers=headers)

async def get_articles(request):
    headers = {'Access-Control-Allow-Origin': '*',}
    if request.method == 'POST':
        response_msg = {}

        # get body req
        post = await request.json()
        lang = post['lang']

        print(request.method)
        print(post)
        result = await handle(req='get_articles', lang=lang)
        articles = []
        # TODO сейчас мы получаем сразу все статьи
        # TODO необходимо сделать получение порционно, что бы запросы не были по 100000000 лет
        if result != 'err':
            if lang is None:
                for i in result:
                    #
                    # text = await format_to_article(i[3])
                    j_string = {"article_id": i[0], "article_name": i[1], "article_description": i[2], #"article_text": text,
                            "article_rate": i[3], "article_tags": i[4], "author": i[5], "lang": i[6]}
                    articles.append(j_string)
            else:
                for i in result:
                    # text = await format_to_article(i[3])
                    j_string = {"article_id": i[0], "article_name": i[1], "article_description": i[2], #"article_text": text,
                            "article_rate": i[3], "article_tags": i[4], "author": i[5]}
                    articles.append(j_string)
        else:
            response_msg['err'] = result

        response_msg['articles'] = articles

        return web.json_response(response_msg, headers=headers)

async def get_lessons(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        response_msg = {}

        # get body req
        post = await request.json()
        lang = post['lang']

        print(request.method)
        print(post)
        result = await handle(req='get_lessons', lang=lang)
        lessons = []

        if result != 'err':
            if lang is None:
                for i in result:
                    j_string = {"lesson_id": i[0], "lesson_name": i[1], "lesson_description": i[2],
                                # "lesson_text": i[3],
                                "lesson_rate": i[3], "lesson_tags": i[4], "author": i[5], "lang": i[6]}
                    lessons.append(j_string)
            else:
                for i in result:
                    j_string = {"lesson_id": i[0], "lesson_name": i[1], "lesson_description": i[2],
                                # "lesson_text": i[3],
                                "lesson_rate": i[3], "lesson_tags": i[4], "author": i[5]}
                    lessons.append(j_string)
        else:
            response_msg['err'] = result

        response_msg['lessons'] = lessons

        return web.json_response(response_msg, headers=headers)

async def get_tasks(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'POST':
        response_msg = {}

        # get body req
        post = await request.json()
        lang = post['lang']

        print(request.method)
        print(post)
        result = await handle(req='get_tasks', lang=lang)
        tasks = []

        if result != 'err':
            if lang is None:
                for i in result:
                    j_string = {"task_id": i[0], "task_name": i[1], "task_description": i[2],
                                "task_rate": i[3], "author": i[4], "task_difficulty": i[5], "lang": i[6]}
                    tasks.append(j_string)
            else:
                for i in result:
                    j_string = {"task_id": i[0], "task_name": i[1], "task_description": i[2],
                                "task_rate": i[3], "author": i[4], "task_difficulty": i[5]}
                    tasks.append(j_string)
        else:
            response_msg['err'] = result

        response_msg['tasks'] = tasks

        return web.json_response(response_msg, headers=headers)

async def get_news(request):
    headers = {'Access-Control-Allow-Origin': '*'}
    if request.method == 'GET':
        response_msg = {}

        print(request.method)
        result = await handle(req='get_news')
        news = []

        if result != 'err':
            for i in result:
                j_string = {"news_id": i[0], "news_name": i[1], "news_description": i[2],
                            # "news_text": i[3],
                            "news_rate": i[3], "news_tags": i[4], "news_importance": i[5] ,"author": i[6]}
                news.append(j_string)
        else:
            response_msg['err'] = result

        response_msg['news'] = news

        return web.json_response(response_msg, headers=headers)

async def get_lesson_tasks(request):
    headers = {'Access-Control-Allow-Origin': '*',}
    if request.method == 'POST':
        response_msg = {}

        # get body req
        post = await request.json()
        lesson_id = post['lessonId']

        print(request.method)
        print(post)
        result = await handle(req='get_lesson_tasks', lesson_id=lesson_id)
        tasks = []

        if result != 'err':
            for i in result:
                j_string = {"task_id": i[0], "task_name": i[1], "task_description": i[2],
                            "task_text": i[3],
                            "task_rate": i[4], "task_difficulty": i[5]}
                tasks.append(j_string)
        else:
            response_msg['err'] = result

        response_msg['tasks'] = tasks

        return web.json_response(response_msg, headers=headers)

async def get_post_info(request):
    headers = {'Access-Control-Allow-Origin': '*', }
    if request.method == 'POST':
        response_msg = {}
        # result = ''

        # get body req
        post = await request.json()
        post_id = post['id']
        post_type = post['type']

        update_views = await handle(req='update_views', post_id=post_id, post_type=post_type)
        result = await handle(req='get_post_info', post_id=post_id, post_type=post_type)
        if result != 'err':
            print()
            print('##################')
            print()
            print(f'{post_type}\n'
                  f'#name:                          {result[0][0]}  \n'
                  f'#desc:                          {result[0][1]} \n'
                  f'#text:                          {result[0][2]} \n'
                  f'#rate:                          {result[0][3]} \n'
                  f'#tags\#task_difficulty:         {result[0][4]} \n'
                  f'#views:                         {update_views[0][0]} \n'
                  f'#lang\#news importance\#lesson: {result[0][5]} \n'
                  f'#author:                        {result[0][6]}')

            response_msg['views']               = update_views[0][0]  # views
            response_msg['post_name']           = result[0][0] #name
            response_msg['post_description']    = result[0][1] #desc
            text = await format_to_article(result[0][2])
            response_msg['post_text']           = text #text
            response_msg['post_rate']           = result[0][3] #rate

            if post_type != 'task':
                response_msg['post_tags']       = result[0][4] #tags
            elif post_type == 'task':
                response_msg['task_difficulty'] = result[0][4]  #task_difficulty

            if post_type != 'news':
                response_msg['post_lang'] = result[0][5] #lang
            elif post_type == 'news':
                response_msg['news_importance'] = result[0][5] #news importance
            elif post_type == 'task':
                pass

            response_msg['author']              = result[0][6] #author
            if post_type == 'task':
                print(f'#test input:                \n{result[0][7]}\n'
                      f'#expected output:           \n{result[0][8]}')
                lesson_arr = []
                _lesson_ids = await handle(req='get_links_tasks_to_lessons_post_info', post_id=post_id, post_type=post_type)
                for _lesson_id in _lesson_ids:
                    cur_lesson = await handle(req='get_lesson_short_info', lesson_id=_lesson_id[0])
                    j_string = {"lesson_id": cur_lesson[0][0], "lesson_name": cur_lesson[0][1]}
                    lesson_arr.append(j_string)
                response_msg['test_input']      = result[0][7] #test input
                response_msg['expected_output'] = result[0][8] #expected output
                response_msg['linked_lessons'] = lesson_arr
                print(f'#linked tasks:                  {lesson_arr}')
            if post_type == 'lesson':
                task_arr = []
                _task_ids = await handle(req='get_links_tasks_to_lessons_post_info', post_id=post_id, post_type=post_type)
                for _task_id in _task_ids:
                    cur_task = await handle(req='get_task_short_info', task_id=_task_id[0])
                    j_string = {"task_id": cur_task[0][0], "task_name": cur_task[0][1], "task_difficulty": cur_task[0][2]}
                    task_arr.append(j_string)
                print(f'#linked tasks:                  {task_arr}')
                response_msg['linked_tasks'] = task_arr
            print()
            print('##################')
            print()

        return web.json_response(response_msg, headers=headers)

async def execute_request_to_jdoodle(request):
    headers = {'Access-Control-Allow-Origin': '*',}
    if request.method == 'POST':
        post = await request.json()

        code = post['code']
        lang = post['lang'].lower()
        input = post['input']

        print(post)

        params = {
            'script': code,
            'language': lang,
            'versionIndex': 2,
            'stdin': input,
            'clientId': credentials.JDOODLE_CLIENT_ID,
            'clientSecret': credentials.JDOODLE_CLIENT_SECRET
        }
        re = requests.post(credentials.JDOODLE_EXECUTE, json=params, headers=headers, verify=False)

        print(re.text)
        j_resp = json.loads(re.text)

        return web.json_response(j_resp, headers=headers)

async def request_to_jdoodle_with_check_valid(request):
    headers = {'Access-Control-Allow-Origin': '*',}
    if request.method == 'POST':
        response_msg = {}
        post = await request.json()

        code = post['code']
        lang = post['lang'].lower()
        input = post['input']
        user_id = post['userId']
        post_id = post['postId']
        expected_output = post['expectedOutput']

        # print(post)

        params = {
            'script': code,
            'language': lang,
            'versionIndex': 2,
            'stdin': input,
            'clientId': credentials.JDOODLE_CLIENT_ID,
            'clientSecret': credentials.JDOODLE_CLIENT_SECRET
        }
        re = requests.post(credentials.JDOODLE_EXECUTE, json=params, headers=headers)

        # print(re.text)
        j_resp = json.loads(re.text)
        if str(j_resp['output']).replace('\n', ' ').rstrip().__eq__(expected_output.replace('\n', ' ')):
            result = await handle(req='update_decided_user_task', user_id=user_id, post_id=post_id, is_decided=True)
            if result:
                response_msg.update(j_resp)
                response_msg['isDecided'] = True
        else:
            result = await handle(req='update_decided_user_task', user_id=user_id, post_id=post_id, is_decided=False)
            if result:
                response_msg.update(j_resp)
                response_msg['isDecided'] = False
            print('else')
        # print(response_msg)
        return web.json_response(response_msg, headers=headers)

async def insert_seen_post(request):
    headers = {'Access-Control-Allow-Origin': '*', }
    if request.method == 'POST':
        response_msg = {}
        post = await request.json()

        user_id = post['userId']
        post_type = post['postType']
        post_id = post['postId']
        is_seen = post['isSeen']

        if post_type == 'task':
            is_decided = post['isDecided']
            update = await handle(req='insert_seen_tasks', user_id=user_id, post_id=post_id,
                                  is_seen=is_seen, is_decided=is_decided)
            if update:
                seen_tasks = []
                result = await handle(req='get_seen_tasks', user_id=user_id)
                for i in result:
                    temp = {'user_id': i[0], 'task_id': i[1], 'isSeen': i[2], 'isDecided': i[3], 'upVote': i[4], 'downVote': i[5]}
                    seen_tasks.append(temp)
                response_msg['tasks'] = seen_tasks
            elif update['err_code']==23505:
                pass
        else:
            if post_type == 'lesson':
                update = await handle(req='insert_seen_lessons', user_id=user_id, post_id=post_id,
                                      is_seen=is_seen)
                if update:
                    seen_lessons = []
                    result = await handle(req='get_seen_lessons', user_id=user_id)
                    for i in result:
                        temp = {'user_id': i[0], 'lesson_id': i[1], 'isSeen': i[2], 'upVote': i[3], 'downVote': i[4]}
                        seen_lessons.append(temp)
                    response_msg['lessons'] = seen_lessons
                elif update['err_code'] == 23505:
                    pass
            elif post_type == 'article':
                update = await handle(req='insert_seen_articles', user_id=user_id, post_id=post_id,
                                      is_seen=is_seen)
                if update:
                    seen_articles = []
                    result = await handle(req='get_seen_articles', user_id=user_id)
                    for i in result:
                        temp = {'user_id': i[0], 'article_id': i[1], 'isSeen': i[2], 'upVote': i[3], 'downVote': i[4]}
                        seen_articles.append(temp)
                    response_msg['articles'] = seen_articles
                elif update['err_code'] == 23505:
                    pass
            elif post_type == 'news':
                update = await handle(req='insert_seen_news', user_id=user_id, post_id=post_id,
                                      is_seen=is_seen)
                if update:
                    seen_news = []
                    result = await handle(req='get_seen_news', user_id=user_id)
                    for i in result:
                        temp = {'user_id': i[0], 'news_id': i[1], 'isSeen': i[2], 'upVote': i[3], 'downVote': i[4]}
                        seen_news.append(temp)
                    response_msg['news'] = seen_news
                elif update['err_code'] == 23505:
                    pass

        return web.json_response(response_msg, headers=headers)

async def update_vote_post(request):
    headers = {'Access-Control-Allow-Origin': '*', }
    if request.method == 'POST':
        response_msg = {}
        post = await request.json()

        user_id = post['userId']
        post_type = post['postType']
        post_id = post['postId']
        vote_type = post['voteType']
        print(post_id)

        if post_type    == 'task':
            update_rate = await handle(req='update_rate_task', vote_type=vote_type, post_id=post_id)
            if update_rate:
                if vote_type == 'up':
                    update = await handle(req='get_vote_state', post_type=post_type, user_id=user_id, post_id=post_id)
                    if update[0][0] == False and update[0][1] == False:
                        update = await handle(req='update_vote_task', up_vote=True, down_vote=False, post_id=post_id,
                                              user_id=user_id)
                    elif update[0][0] == False and update[0][1] == True:
                        update = await handle(req='update_vote_task', up_vote=False, down_vote=False, post_id=post_id,
                                              user_id=user_id)
                else:
                    update = await handle(req='get_vote_state', post_type=post_type, user_id=user_id, post_id=post_id)
                    if update[0][0] == False and update[0][1] == False:
                        update = await handle(req='update_vote_task', up_vote=False, down_vote=True, post_id=post_id,
                                              user_id=user_id)
                    elif update[0][0] == True and update[0][1] == False:
                        update = await handle(req='update_vote_task', up_vote=False, down_vote=False, post_id=post_id,
                                              user_id=user_id)
                if update:
                    seen_tasks = []
                    result = await handle(req='get_seen_tasks', user_id=user_id)
                    for i in result:
                        temp = {'user_id': i[0], 'task_id': i[1], 'isSeen': i[2], 'isDecided': i[3], 'upVote': i[4], 'downVote': i[5]}
                        seen_tasks.append(temp)
                    response_msg['tasks'] = seen_tasks
                elif update['err_code']==23505:
                    pass
            else:
                pass
        elif post_type  == 'lesson':
            update_rate = await handle(req='update_rate_lesson', vote_type=vote_type, post_id=post_id)
            if update_rate:
                if vote_type == 'up':
                    update = await handle(req='get_vote_state', post_type=post_type, user_id=user_id, post_id=post_id)
                    if update[0][0] == False and update[0][1] == False:
                        update = await handle(req='update_vote_lesson', up_vote=True, down_vote=False, post_id=post_id,
                                              user_id=user_id)
                    elif update[0][0] == False and update[0][1] == True:
                        update = await handle(req='update_vote_lesson', up_vote=False, down_vote=False, post_id=post_id,
                                              user_id=user_id)
                else:
                    update = await handle(req='get_vote_state', post_type=post_type, user_id=user_id, post_id=post_id)
                    if update[0][0] == False and update[0][1] == False:
                        update = await handle(req='update_vote_lesson', up_vote=False, down_vote=True, post_id=post_id,
                                              user_id=user_id)
                    elif update[0][0] == True and update[0][1] == False:
                        update = await handle(req='update_vote_lesson', up_vote=False, down_vote=False, post_id=post_id,
                                              user_id=user_id)
                if update:
                    seen_lessons = []
                    result = await handle(req='get_seen_lessons', user_id=user_id)
                    for i in result:
                        temp = {'user_id': i[0], 'lesson_id': i[1], 'isSeen': i[2], 'upVote': i[3], 'downVote': i[4]}
                        seen_lessons.append(temp)
                    response_msg['lessons'] = seen_lessons
                elif update['err_code'] == 23505:
                    pass
            else:
                pass
        elif post_type  == 'article':
            update_rate = await handle(req='update_rate_article', vote_type=vote_type, post_id=post_id)
            if update_rate:
                if vote_type == 'up':
                    update = await handle(req='get_vote_state', post_type=post_type, user_id=user_id, post_id=post_id)
                    if update[0][0] == False and update[0][1] == False:
                        update = await handle(req='update_vote_article', up_vote=True, down_vote=False, post_id=post_id,
                                              user_id=user_id)
                    elif update[0][0] == False and update[0][1] == True:
                        update = await handle(req='update_vote_article', up_vote=False, down_vote=False, post_id=post_id,
                                              user_id=user_id)
                else:
                    update = await handle(req='get_vote_state', post_type=post_type, user_id=user_id, post_id=post_id)
                    if update[0][0] == False and update[0][1] == False:
                        update = await handle(req='update_vote_article', up_vote=False, down_vote=True, post_id=post_id,
                                              user_id=user_id)
                    elif update[0][0] == True and update[0][1] == False:
                        update = await handle(req='update_vote_article', up_vote=False, down_vote=False, post_id=post_id,
                                              user_id=user_id)

                if update:
                    seen_articles = []
                    result = await handle(req='get_seen_articles', user_id=user_id)
                    for i in result:
                        temp = {'user_id': i[0], 'article_id': i[1], 'isSeen': i[2], 'upVote': i[3], 'downVote': i[4]}
                        seen_articles.append(temp)
                    response_msg['articles'] = seen_articles
                elif update['err_code'] == 23505:
                    pass
            else:
                pass
        elif post_type  == 'news':
            update_rate = await handle(req='update_rate_news', vote_type=vote_type, post_id=post_id)
            if update_rate:
                if vote_type == 'up':
                    update = await handle(req='get_vote_state', post_type=post_type, user_id=user_id, post_id=post_id)
                    if update[0][0] == False and update[0][1] == False:
                        update = await handle(req='update_vote_news', up_vote=True, down_vote=False, post_id=post_id,
                                              user_id=user_id)
                    elif update[0][0] == False and update[0][1] == True:
                        update = await handle(req='update_vote_news', up_vote=False, down_vote=False, post_id=post_id,
                                              user_id=user_id)
                else:
                    update = await handle(req='get_vote_state', post_type=post_type, user_id=user_id, post_id=post_id)
                    if update[0][0] == False and update[0][1] == False:
                        update = await handle(req='update_vote_news', up_vote=False, down_vote=True, post_id=post_id,
                                              user_id=user_id)
                    elif update[0][0] == True and update[0][1] == False:
                        update = await handle(req='update_vote_news', up_vote=False, down_vote=False, post_id=post_id,
                                              user_id=user_id)

                if update:
                    seen_news = []
                    result = await handle(req='get_seen_news', user_id=user_id)
                    for i in result:
                        temp = {'user_id': i[0], 'news_id': i[1], 'isSeen': i[2], 'upVote': i[3], 'downVote': i[4]}
                        seen_news.append(temp)
                    response_msg['news'] = seen_news
                elif update['err_code'] == 23505:
                    pass
            else:
                pass
        return web.json_response(response_msg, headers=headers)