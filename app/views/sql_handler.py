import psycopg2, credentials
from app import sql_requests


async def handle(**kwargs):
    # подключение к дб
    connection = psycopg2.connect(credentials.DB_CRED)
    # получение курсора
    cursor = connection.cursor()
    result = None
    try:
        # проверка параметра, и выполнение нужного запроса в зависиомости от параметра req
        if kwargs['req'] == 'get_user':
            try:
                cursor.execute(sql_requests.SELECT_USER, [kwargs['user_email']])
                result = cursor.fetchall()
            except psycopg2.Error:
                result = 'err'
                print(psycopg2.Error)
        if kwargs['req'] == 'get_valid_name':
            cursor.execute(sql_requests.SELECT_USER_ON_EMAIL_OR_NAME, [kwargs['user_email'], kwargs['user_name']])
            temp = cursor.fetchall()
            print(temp)
            if temp:
                if temp[0][0] == kwargs['user_email'] and temp[0][1] == kwargs['user_name']:
                    result = {'valid': False, 'msg': 'Данные имя и email уже используются'}
                elif temp[0][0] == kwargs['user_email']:
                    result = {'valid': False, 'msg': 'Данный email уже используется'}
                elif temp[0][1] == kwargs['user_name']:
                    result = {'valid': False, 'msg': 'Данное имя уже используется'}
                else:
                    result = {'valid': True}
            else:
                result = {'valid': True}
        elif kwargs['req'] == 'get_articles_on_id':
            cursor.execute(sql_requests.SELECT_ARTICLE_ON_ID, [kwargs['article_id']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_lesson_on_id':
            cursor.execute(sql_requests.SELECT_LESSON_ON_ID, [kwargs['lesson_id']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_task_on_id':
            cursor.execute(sql_requests.SELECT_TASK_ON_ID, [kwargs['task_id']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_seen_tasks':
            cursor.execute(sql_requests.SELECT_USER_SEEN_TASKS, [kwargs['user_id']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_seen_lessons':
            cursor.execute(sql_requests.SELECT_USER_SEEN_LESSONS, [kwargs['user_id']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_seen_articles':
            cursor.execute(sql_requests.SELECT_USER_SEEN_ARTICLES, [kwargs['user_id']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_seen_news':
            cursor.execute(sql_requests.SELECT_USER_SEEN_NEWS, [kwargs['user_id']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_langs_name':
            cursor.execute(sql_requests.SELECT_PROG_LANGS_NAME)
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_langs':
            cursor.execute(sql_requests.SELECT_PROG_LANGS)
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_lang_lessons_name':
            cursor.execute(sql_requests.SELECT_LANG_LESSONS_NAME, [kwargs['lang']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_user_lessons_name':
            cursor.execute(sql_requests.SELECT_USER_LESSONS_NAME, [kwargs['user_email'], kwargs['lang']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_user_lessons':
            cursor.execute(sql_requests.SELECT_USER_LESSONS, [kwargs['user_email']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_user_tasks':
            cursor.execute(sql_requests.SELECT_USER_TASKS, [kwargs['user_email']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_user_articles':
            cursor.execute(sql_requests.SELECT_USER_ARTICLES, [kwargs['user_email']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_user_news':
            cursor.execute(sql_requests.SELECT_USER_NEWS, [kwargs['user_email']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_articles':
            if kwargs['lang'] is None:
                cursor.execute(sql_requests.SELECT_ALL_ARTICLES)
            else:
                cursor.execute(sql_requests.SELECT_LANG_ARTICLES, [kwargs['lang']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_news':
            cursor.execute(sql_requests.SELECT_ALL_NEWS)
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_lessons':
            if kwargs['lang'] is None:
                cursor.execute(sql_requests.SELECT_ALL_LESSONS)
            else:
                cursor.execute(sql_requests.SELECT_LANG_LESSONS, [kwargs['lang']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_tasks':
            if kwargs['lang'] is None:
                cursor.execute(sql_requests.SELECT_ALL_TASKS)
            else:
                cursor.execute(sql_requests.SELECT_LANG_TASKS, [kwargs['lang']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_links_tasks_to_lessons_post_info':
            if kwargs['post_type'] == 'lesson':
                cursor.execute(sql_requests.SELECT_LESSON_TASKS, [kwargs['post_id']])
                result = cursor.fetchall()
            elif kwargs['post_type'] == 'task':
                cursor.execute(sql_requests.SELECT_TASK_LESSONS, [kwargs['post_id']])
                result = cursor.fetchall()

        elif kwargs['req'] == 'get_task_short_info':
            cursor.execute(sql_requests.SELECT_SHORT_TASK_INFO, [kwargs['task_id']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_lesson_short_info':
            cursor.execute(sql_requests.SELECT_SHORT_LESSON_INFO, [kwargs['lesson_id']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_links_tasks_to_lessons':
            cursor.execute(sql_requests.SELECT_LINK_TASKS_TO_LESSONS, [kwargs['task_id']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_links_lessons_to_tasks':
            cursor.execute(sql_requests.SELECT_LINK_LESSONS_TO_TASKS, [kwargs['lesson_id']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_lesson_name':
            cursor.execute(sql_requests.SELECT_LESSON_NAME, [kwargs['lesson_id']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_task':
            cursor.execute(sql_requests.SELECT_TASK_TO_LESSONS, [kwargs['task_id']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_lesson_id':
            cursor.execute(sql_requests.SELECT_LESSON_ID, [kwargs['lesson_name']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_post_info':
            if kwargs['post_type'] == 'article':
                cursor.execute(sql_requests.SELECT_ARTICLE_INFO, [kwargs['post_id']])
                result = cursor.fetchall()
            elif kwargs['post_type'] == 'news':
                cursor.execute(sql_requests.SELECT_NEWS_INFO, [kwargs['post_id']])
                result = cursor.fetchall()
            elif kwargs['post_type'] == 'lesson':
                cursor.execute(sql_requests.SELECT_LESSON_INFO, [kwargs['post_id']])
                result = cursor.fetchall()
            elif kwargs['post_type'] == 'task':
                cursor.execute(sql_requests.SELECT_TASK_INFO, [kwargs['post_id']])
                result = cursor.fetchall()
        elif kwargs['req'] == 'get_vote_state':
            if kwargs['post_type']   == 'article':
                cursor.execute(sql_requests.SELECT_USER_TO_ARTICLE_VOTES, [kwargs['user_id'], kwargs['post_id']])
                result = cursor.fetchall()
            elif kwargs['post_type'] == 'news':
                cursor.execute(sql_requests.SELECT_USER_TO_NEWS_VOTES, [kwargs['user_id'], kwargs['post_id']])
                result = cursor.fetchall()
            elif kwargs['post_type'] == 'lesson':
                cursor.execute(sql_requests.SELECT_USER_TO_LESSON_VOTES, [kwargs['user_id'], kwargs['post_id']])
                result = cursor.fetchall()
            elif kwargs['post_type'] == 'task':
                cursor.execute(sql_requests.SELECT_USER_TO_TASK_VOTES, [kwargs['user_id'], kwargs['post_id']])
                result = cursor.fetchall()
        elif kwargs['req'] == 'get_user_role':
            cursor.execute(sql_requests.SELECT_USER_ROLE, [kwargs['moder_name']])
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_unmod_articles':
            cursor.execute(sql_requests.SELECT_UNMOD_ARTICLES)
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_unmod_lessons':
            cursor.execute(sql_requests.SELECT_UNMOD_LESSONS)
            result = cursor.fetchall()
        elif kwargs['req'] == 'get_unmod_tasks':
            cursor.execute(sql_requests.SELECT_UNMOD_TASKS)
            result = cursor.fetchall()
        # TODO в add запросах result должен возвращать состояние запроса успешно, исключение или ошибка, если ошибка/исключение, то её описание,
        elif kwargs['req'] == 'add_user':
            try:
                cursor.execute(sql_requests.INSERT_USER, (kwargs['user_name'], kwargs['user_email'], kwargs['user_rate'],
                                                          kwargs['time'], kwargs['time']))
                result = 'user added'
            except psycopg2.IntegrityError as e:
                result = {'err_code': e.pgcode}
        elif kwargs['req'] == 'add_article':
            cursor.execute(sql_requests.INSERT_ARTICLE,
                          (kwargs['article_name'], kwargs['article_description'], kwargs['article_text'], kwargs['article_rate'],
                           kwargs['article_lang'], kwargs['author_email'], kwargs['article_tags'], kwargs['time'], kwargs['time']))
            result = True
            print(result)
        elif kwargs['req'] == 'add_lesson':
            cursor.execute(sql_requests.INSERT_LESSON,
                          (kwargs['lesson_name'], kwargs['lesson_description'], kwargs['lesson_text'], kwargs['lesson_rate'],
                           kwargs['lesson_lang'], kwargs['author_email'], kwargs['lesson_tags'], kwargs['time'], kwargs['time']))
            result = True
            print(result)
        elif kwargs['req'] == 'add_task':
            cursor.execute(sql_requests.INSERT_TASK,
                          (kwargs['task_name'], kwargs['task_description'], kwargs['task_text'], kwargs['task_rate'],
                           kwargs['author_email'], kwargs['task_difficulty'],
                           kwargs['task_test_input'], kwargs['task_expected_output'], kwargs['lang_id'], kwargs['time'], kwargs['time']))
            result = True
            print(result)
        elif kwargs['req'] == 'add_news':
            cursor.execute(sql_requests.INSERT_NEWS,
                           (kwargs['news_name'], kwargs['news_description'], kwargs['news_text'], kwargs['news_rate'],
                                kwargs['user_email'], kwargs['news_tags'], kwargs['news_importance'], kwargs['time'], kwargs['time']))
            result = True
            print(result)
        elif kwargs['req'] == 'update_article':
            cursor.execute(sql_requests.UPDATE_ARTICLE,
                           (kwargs['article_name'], kwargs['article_description'], kwargs['article_text'], kwargs['article_lang'],
                            kwargs['article_tags'], kwargs['last_update'], kwargs['is_moderated'],kwargs['is_denied'],kwargs['is_approved'],
                            kwargs['article_id']))
            result = True
        elif kwargs['req'] == 'update_news':
            cursor.execute(sql_requests.UPDATE_NEWS,
                           (kwargs['news_name'], kwargs['news_description'], kwargs['news_text'],
                            kwargs['news_tags'],
                            kwargs['news_importance'], kwargs['last_update'], kwargs['news_id']))
            result = True
        elif kwargs['req'] == 'update_lesson':
            cursor.execute(sql_requests.UPDATE_LESSON,
                           (kwargs['lesson_name'], kwargs['lesson_description'], kwargs['lesson_text'],
                            kwargs['lesson_lang'], kwargs['lesson_tags'], kwargs['last_update'],
                            kwargs['is_denied'], kwargs['is_approved'], kwargs['is_moderated'],
                            kwargs['lesson_id']))
            result = True
        elif kwargs['req'] == 'update_task':
            cursor.execute(sql_requests.UPDATE_TASK,
                           (kwargs['task_name'], kwargs['task_description'], kwargs['task_text'],
                            kwargs['lang_name'], kwargs['task_difficulty'], kwargs['task_test_input'],
                            kwargs['task_expected_output'], kwargs['last_update'],kwargs['is_denied'],kwargs['is_approved'],
                            kwargs['is_moderated'], kwargs['task_id']))
            result = True
        elif kwargs['req'] == 'update_decided_user_task':
            cursor.execute(sql_requests.UPDATE_TASK_DECIDED, (kwargs['is_decided'], kwargs['post_id'], kwargs['user_id']))
            result = True
        elif kwargs['req'] == 'update_views':
            if kwargs['post_type'] == 'article':
                cursor.execute(sql_requests.UPDATE_ARTICLE_VIEWS, [kwargs['post_id']])
                cursor.execute(sql_requests.SELECT_ARTICLE_VIEWS, [kwargs['post_id']])
                result = cursor.fetchall()
            elif kwargs['post_type'] == 'news':
                cursor.execute(sql_requests.UPDATE_NEWS_VIEWS, [kwargs['post_id']])
                cursor.execute(sql_requests.SELECT_NEWS_VIEWS, [kwargs['post_id']])
                result = cursor.fetchall()
            elif kwargs['post_type'] == 'lesson':
                cursor.execute(sql_requests.UPDATE_LESSON_VIEWS, [kwargs['post_id']])
                cursor.execute(sql_requests.SELECT_LESSON_VIEWS, [kwargs['post_id']])
                result = cursor.fetchall()
            elif kwargs['post_type'] == 'task':
                cursor.execute(sql_requests.UPDATE_TASKS_VIEWS, [kwargs['post_id']])
                cursor.execute(sql_requests.SELECT_TASK_VIEWS, [kwargs['post_id']])
                result = cursor.fetchall()
        elif kwargs['req'] == 'update_rate_task':
           if kwargs['vote_type'] == 'up':
               cursor.execute(sql_requests.UPDATE_TASK_PLUS_RATE, [kwargs['post_id']])
               result = True
           else:
               cursor.execute(sql_requests.UPDATE_TASK_MINUS_RATE, [kwargs['post_id']])
               result = True
        elif kwargs['req'] == 'update_rate_lesson':
            if kwargs['vote_type'] == 'up':
                cursor.execute(sql_requests.UPDATE_LESSON_PLUS_RATE, [kwargs['post_id']])
                result = True
            else:
                cursor.execute(sql_requests.UPDATE_LESSON_MINUS_RATE, [kwargs['post_id']])
                result = True
        elif kwargs['req'] == 'update_rate_article':
            if kwargs['vote_type'] == 'up':
                cursor.execute(sql_requests.UPDATE_ARTICLE_PLUS_RATE, [kwargs['post_id']])
                result = True
            else:
                cursor.execute(sql_requests.UPDATE_ARTICLE_MINUS_RATE, [kwargs['post_id']])
                result = True
        elif kwargs['req'] == 'update_rate_news':
            if kwargs['vote_type'] == 'up':
                cursor.execute(sql_requests.UPDATE_NEWS_PLUS_RATE, [kwargs['post_id']])
                result = True
            else:
                cursor.execute(sql_requests.UPDATE_NEWS_MINUS_RATE, [kwargs['post_id']])
                result = True
        elif kwargs['req'] == 'update_vote_task':
            cursor.execute(sql_requests.UPDATE_TASK_VOTE, (kwargs['up_vote'], kwargs['down_vote'], kwargs['post_id'], kwargs['user_id']))
            result = True
        elif kwargs['req'] == 'update_vote_lesson':
            cursor.execute(sql_requests.UPDATE_LESSON_VOTE, (kwargs['up_vote'], kwargs['down_vote'], kwargs['post_id'], kwargs['user_id']))
            result = True
        elif kwargs['req'] == 'update_vote_article':
            cursor.execute(sql_requests.UPDATE_ARTICLE_VOTE, (kwargs['up_vote'], kwargs['down_vote'], kwargs['post_id'], kwargs['user_id']))
            result = True
        elif kwargs['req'] == 'update_vote_news':
            cursor.execute(sql_requests.UPDATE_NEWS_VOTE, (kwargs['up_vote'], kwargs['down_vote'], kwargs['post_id'], kwargs['user_id']))
            result = True
        elif kwargs['req'] == 'update_link_task_to_lesson':
            cursor.execute(sql_requests.UPDATE_LINK_TASK_TO_LESSON, (kwargs['new_l_id'], kwargs['task_id'], kwargs['task_id'], kwargs['lesson_id']))
            result = True
        elif kwargs['req'] == 'update_ismoderated':
            if kwargs['post_type'] == 'article':
                cursor.execute(sql_requests.UPDATE_ISMODER_ARTICLE,
                               (kwargs['moder'], kwargs['is_denied'],kwargs['is_approved'],
                                kwargs['post_id'], kwargs['user_id']))
                result = True
            elif kwargs['post_type'] == 'task':
                cursor.execute(sql_requests.UPDATE_ISMODER_TASK,
                               (kwargs['moder'], kwargs['is_denied'],kwargs['is_approved'],
                                kwargs['post_id'], kwargs['user_id']))
                result = True
            elif kwargs['post_type'] == 'lesson':
                cursor.execute(sql_requests.UPDATE_ISMODER_LESSON,
                               (kwargs['moder'], kwargs['is_denied'],kwargs['is_approved'],
                                kwargs['post_id'], kwargs['user_id']))
                result = True
        elif kwargs['req'] == 'insert_seen_lessons':
            cursor.execute(sql_requests.INSERT_SEEN_LESSON,
                           (kwargs['user_id'], kwargs['post_id'], kwargs['is_seen']))
            result = True
        elif kwargs['req'] == 'insert_seen_tasks':
            cursor.execute(sql_requests.INSERT_SEEN_TASK,
                           (kwargs['user_id'], kwargs['post_id'], kwargs['is_seen'], kwargs['is_decided']))
            result = True
        elif kwargs['req'] == 'insert_seen_articles':
            cursor.execute(sql_requests.INSERT_SEEN_ARTICLE,
                           (kwargs['user_id'], kwargs['post_id'], kwargs['is_seen']))
            result = True
        elif kwargs['req'] == 'insert_seen_news':
            cursor.execute(sql_requests.INSERT_SEEN_NEWS,
                           (kwargs['user_id'], kwargs['post_id'], kwargs['is_seen']))
            result = True
        elif kwargs['req'] == 'delete_article':
            cursor.execute(sql_requests.DELETE_ARTICLE, (kwargs['author'], kwargs['article_id']))
            result = 'article deleted'
        elif kwargs['req'] == 'delete_news':
            cursor.execute(sql_requests.DELETE_NEWS, (kwargs['author'], kwargs['news_id']))
            result = 'news deleted'
        elif kwargs['req'] == 'delete_lesson':
            cursor.execute(sql_requests.DELETE_LESSON, (kwargs['author'], kwargs['lesson_id']))
            result = 'lesson deleted'
        elif kwargs['req'] == 'delete_task':
            cursor.execute(sql_requests.DELETE_TASK, (kwargs['author'], kwargs['task_id']))
            result = 'task deleted'
        elif kwargs['req'] == 'delete_link_task_to_lesson':
            cursor.execute(sql_requests.DELETE_LINK_TASK_TO_LESSON, (kwargs['lesson_id'], kwargs['task_id']))
        elif kwargs['req'] == 'link_lessons_to_tasks':
            cursor.execute(sql_requests.INSERT_TASK_TO_LESSON, [kwargs['task_name'], kwargs['lesson_id']])
        elif kwargs['req'] == 'test':
            cursor.execute(sql_requests.SELECT_USERS)
            result = cursor.fetchall()


        return result
    # TODO сделать обработку ошибок по кодам
    except psycopg2.IntegrityError as e:
        print('integrity error code', e.pgcode)
        print(e)
        if e.pgcode == '23505':
            msg = {'err_code': e.pgcode, 'err_info': 'Данное имя поста уже существует.'}
            return msg
        else:
            return 'err'
    except psycopg2.DataError as e:
        print('data error code', e.pgcode)
        print(e)
        msg = {'err_code': e.pgcode}
        return msg
    except psycopg2.DatabaseError as e:
        print('database error code', e.pgcode)
        print(e)
        msg = {'err_code': e.pgcode}
        return msg
    except psycopg2.Error as e:
        print('error code', e)
        print(e)
        msg = {'err_code': e.pgcode}
        return msg
    finally:
        # завершение транзакции, закрытие подключения
        connection.commit()
        cursor.close()
        connection.close()