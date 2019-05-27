SELECT_USERS = "SELECT * FROM users;"

SELECT_USER_ON_EMAIL_OR_NAME = "select user_email, user_name from users where user_email=%s or user_name = %s"

SELECT_USER = """SELECT * from users WHERE user_email = %s;"""

SELECT_USER_ROLE = "select user_role from users where user_name=%s;"

SELECT_USER_SEEN_TASKS = "select * from users_to_tasks where user_id = %s"

SELECT_USER_SEEN_LESSONS = "select * from users_to_lessons where user_id = %s"

SELECT_USER_SEEN_ARTICLES = "select * from users_to_articles where user_id = %s"

SELECT_USER_SEEN_NEWS = "select * from users_to_news where user_id = %s"

SELECT_PROG_LANGS_NAME = "SELECT lang_id, lang_name FROM programming_langs;"

SELECT_PROG_LANGS = "SELECT * FROM programming_langs;"

SELECT_ARTICLE_VIEWS = "select article_views from articles WHERE article_id = %s"

SELECT_NEWS_VIEWS = "select news_views from news WHERE news_id = %s"

SELECT_LESSON_VIEWS = "select lesson_views from lessons WHERE lesson_id = %s"

SELECT_TASK_VIEWS = "select task_views from tasks WHERE task_id = %s"

SELECT_USER_LESSONS_NAME = "SELECT lesson_id, lesson_name " \
                           "FROM lessons " \
                           "WHERE author_id = (SELECT user_id FROM users WHERE user_email = %s) " \
                           "AND lang_id = (SELECT lang_id FROM programming_langs WHERE lang_name = %s)"

SELECT_USER_LESSONS = "SELECT lessons.lesson_id, lessons.lesson_name, lessons.lesson_description, lessons.lesson_text, lessons.lesson_rate, lessons.lesson_tags, lessons.lang_id, programming_langs.lang_name " \
                      "FROM lessons " \
                      "LEFT OUTER JOIN users on (lessons.author_id = users.user_id) " \
                      "LEFT OUTER JOIN programming_langs on (lessons.lang_id = programming_langs.lang_id)" \
                      "WHERE users.user_email = %s;"

SELECT_USER_TASKS = "SELECT tasks.task_id, tasks.task_name, tasks.task_description, " \
                    "tasks.task_text, tasks.task_rate, tasks.task_difficulty, " \
                    "tasks.test_input, tasks.expected_output, tasks.lang_id, programming_langs.lang_name " \
                    "FROM tasks " \
                    "LEFT OUTER JOIN users on (tasks.author_id = users.user_id) " \
                    "LEFT OUTER JOIN programming_langs on (tasks.lang_id = programming_langs.lang_id) " \
                    "WHERE users.user_email = %s;"

SELECT_USER_ARTICLES = "SELECT articles.article_id, articles.article_name, articles.article_description, " \
                       "articles.article_text, articles.article_rate, articles.article_tags, articles.lang_id, programming_langs.lang_name " \
                      "FROM articles " \
                      "LEFT OUTER JOIN users on (articles.author_id = users.user_id) " \
                      "LEFT OUTER JOIN programming_langs on (articles.lang_id = programming_langs.lang_id)" \
                      "WHERE users.user_email = %s;"

SELECT_USER_NEWS = "SELECT news_id, news_name, news_description, news_text, news_rate, news_tags, news_importance " \
                   "FROM news " \
                   "WHERE author_id = (SELECT user_id FROM users WHERE user_email = %s)"

SELECT_ARTICLE_ON_ID = "select articles.article_name, articles.article_description, articles.article_text, " \
                       "articles.article_tags, programming_langs.lang_name " \
                       "from articles " \
                       "left outer join programming_langs on (articles.lang_id = programming_langs.lang_id)" \
                       "where article_id=%s"

SELECT_LESSON_ON_ID =  "select lessons.lesson_name, lessons.lesson_description, lessons.lesson_text, " \
                       "lessons.lesson_tags, programming_langs.lang_name " \
                       "from lessons " \
                       "left outer join programming_langs on (lessons.lang_id = programming_langs.lang_id)" \
                       "where lesson_id=%s"

SELECT_TASK_ON_ID =  "select tasks.task_name, tasks.task_description, tasks.task_text, " \
                       "tasks.task_difficulty, tasks.test_input, tasks.expected_output, programming_langs.lang_name " \
                       "from tasks " \
                       "left outer join programming_langs on (tasks.lang_id = programming_langs.lang_id)" \
                       "where task_id=%s"

SELECT_ALL_ARTICLES = """select articles.article_id, articles.article_name, articles.article_description, 
                      articles.article_rate, articles.article_tags, users.user_name, programming_langs.lang_name, 
                      articles.added_time, articles.last_update, articles.article_views 
                      from articles 
                      left outer join users on (articles.author_id = users.user_id) 
                      left outer join programming_langs on (articles.lang_id = programming_langs.lang_id) 
                      where articles."isModerated"=TRUE"""

SELECT_ALL_NEWS = "select news.news_id, news.news_name, news.news_description, " \
                  "news.news_rate, news.news_tags, news.news_importance, users.user_name," \
                  "news.added_time, news.last_update, news.news_views " \
                  "from news " \
                  "left outer join users on (news.author_id = users.user_id) "

SELECT_ALL_TASKS = """select tasks.task_id, tasks.task_name, tasks.task_description, tasks.task_rate, 
                   users.user_name, tasks.task_difficulty, 
                   programming_langs.lang_name, tasks.added_time, tasks.last_update, tasks.task_views  
                   from tasks  
                   left outer join users on (users.user_id = tasks.author_id) 
                   left outer join programming_langs on (programming_langs.lang_id = tasks.lang_id)
                   where tasks."isModerated"=TRUE """

SELECT_ALL_LESSONS = """select lessons.lesson_id, lessons.lesson_name, lessons.lesson_description, 
                      lessons.lesson_rate, lessons.lesson_tags, users.user_name, programming_langs.lang_name, 
                      lessons.added_time, lessons.last_update, lessons.lesson_views 
                      from lessons 
                      left outer join users on (lessons.author_id = users.user_id) 
                      left outer join programming_langs on (lessons.lang_id = programming_langs.lang_id) 
                      where lessons."isModerated"=TRUE"""

SELECT_LANG_ARTICLES = """select articles.article_id, articles.article_name, articles.article_description, 
                       articles.article_rate, articles.article_tags, users.user_name, articles.added_time, 
                       articles.last_update, articles.article_views  
                       from articles 
                       left outer join users on (articles.author_id = users.user_id) 
                       left outer join programming_langs on (articles.lang_id = programming_langs.lang_id) 
                       where programming_langs.lang_name = %s and articles."isModerated"=TRUE"""

SELECT_LANG_LESSONS = """select lessons.lesson_id, lessons.lesson_name, lessons.lesson_description, 
                      lessons.lesson_rate, lessons.lesson_tags, users.user_name,
                      lessons.added_time, lessons.last_update, lessons.lesson_views 
                      from lessons 
                      left outer join users on (lessons.author_id = users.user_id) 
                      left outer join programming_langs on (lessons.lang_id = programming_langs.lang_id) 
                      where programming_langs.lang_name = %s and lessons."isModerated"=TRUE"""

SELECT_LANG_TASKS = """select tasks.task_id, tasks.task_name, tasks.task_description, tasks.task_rate, 
                    users.user_name, tasks.task_difficulty, 
                    tasks.added_time, tasks.last_update, tasks.task_views 
                    from tasks  
                    left outer join users on (users.user_id = tasks.author_id)
                    left outer join programming_langs on (programming_langs.lang_id = tasks.lang_id)
                    where programming_langs.lang_name = %s and tasks."isModerated"=TRUE """

SELECT_LESSON_TASKS = "select task_id from tasks_to_lessons " \
                      "where lesson_id = %s;"

SELECT_SHORT_TASK_INFO = "select task_id, task_name, task_difficulty " \
                         "from tasks " \
                         "where task_id=%s;"

SELECT_TASK_LESSONS = "select lesson_id from tasks_to_lessons " \
                      "where task_id = %s;"

SELECT_SHORT_LESSON_INFO = "select lesson_id, lesson_name " \
                         "from lessons " \
                         "where lesson_id=%s;"

SELECT_LINK_TASKS_TO_LESSONS = "select lesson_id from tasks_to_lessons where task_id = %s"

SELECT_LESSON_NAME = "select lesson_name from lessons where lesson_id = %s;"

SELECT_LESSON_ID =  "select lesson_id from lessons where lesson_name = %s;"

SELECT_UNMOD_ARTICLES="""select articles.article_id, articles.article_name, articles.article_description,
                          articles.article_text, articles.article_tags, articles.author_id, users.user_name 
                          from articles left outer join users on (articles.author_id = users.user_id) 
                          where "isModerated" = False;"""

SELECT_UNMOD_LESSONS  ="""select lessons.lesson_id, lessons.lesson_name, lessons.lesson_description,
                          lessons.lesson_text, lessons.lesson_tags, lessons.author_id, users.user_name 
                          from lessons left outer join users on (lessons.author_id = users.user_id) 
                          where "isModerated" = False;"""

SELECT_UNMOD_TASKS    ="""select tasks.task_id, tasks.task_name, tasks.task_description,
                          tasks.task_text, tasks.task_difficulty, tasks.test_input, tasks.expected_output, 
                          tasks.author_id, users.user_name 
                          from tasks left outer join users on (tasks.author_id = users.user_id) 
                          where "isModerated" = False;"""

SELECT_ARTICLE_INFO = "select articles.article_name, articles.article_description, articles.article_text, " \
                      "articles.article_rate, articles.article_tags, programming_langs.lang_name, " \
                      "users.user_name, articles.added_time, articles.last_update " \
                      "from articles " \
                      "left outer join users on (articles.author_id = users.user_id) " \
                      "left outer join programming_langs on (articles.lang_id = programming_langs.lang_id) " \
                      "where article_id = %s;"

SELECT_NEWS_INFO = "select news.news_name, news.news_description, news.news_text, news.news_rate, news.news_tags, " \
                   "news.news_importance, users.user_name, news.added_time, news.last_update " \
                   "from news " \
                   "left outer join users on (news.author_id = users.user_id) " \
                   "where news_id = %s;"

SELECT_LESSON_INFO = "select lessons.lesson_name, lessons.lesson_description, lessons.lesson_text, lessons.lesson_rate, " \
                     "lessons.lesson_tags, programming_langs.lang_name, users.user_name, lessons.added_time, lessons.last_update " \
                     "from lessons " \
                     "left outer join users on (lessons.author_id = users.user_id) " \
                     "left outer join programming_langs on (lessons.lang_id = programming_langs.lang_id)" \
                     "where lesson_id = %s;"

SELECT_TASK_INFO = "select tasks.task_name, tasks.task_description, tasks.task_text, tasks.task_rate, " \
                   "tasks.task_difficulty, programming_langs.lang_name, users.user_name, tasks.added_time, tasks.last_update, tasks.test_input, tasks.expected_output " \
                   "from tasks " \
                   "left outer join users on (tasks.author_id = users.user_id) " \
                   "left outer join programming_langs on (tasks.lang_id = programming_langs.lang_id)" \
                   "where task_id = %s;"

SELECT_USER_TO_TASK_VOTES = """select "upVote", "downVote" from users_to_tasks where user_id = %s and task_id=%s"""

SELECT_USER_TO_LESSON_VOTES = """select "upVote", "downVote" from users_to_lessons where user_id = %s and lesson_id=%s"""

SELECT_USER_TO_ARTICLE_VOTES = """select "upVote", "downVote" from users_to_articles where user_id = %s and article_id=%s"""

SELECT_USER_TO_NEWS_VOTES = """select "upVote", "downVote" from users_to_news where user_id = %s and news_id=%s"""

INSERT_USER = "INSERT INTO users (user_role, user_name, user_email, user_rate, added_time, last_update) " \
              "VALUES (" \
                "(SELECT role_num from roles where role_name='User'), " \
                "%s, " \
                "%s, " \
                "%s, " \
                "%s, " \
                "%s);"

INSERT_NEWS = "INSERT INTO news (news_name, news_description, news_text, news_rate, author_id, news_tags, news_importance, added_time, last_update) " \
              "VALUES (" \
                "%s, " \
                "%s, " \
                "%s, " \
                "%s, " \
                "(SELECT user_id from users where user_email=%s), " \
                "%s, " \
                "%s," \
                "%s," \
                "%s);"

INSERT_ARTICLE = "INSERT INTO articles (article_name, article_description, article_text, article_rate, lang_id, author_id, article_tags, added_time, last_update) " \
              "VALUES (" \
                "%s, " \
                "%s, " \
                "%s, " \
                "%s," \
                "(SELECT lang_id from programming_langs where lang_name=%s)," \
                "(SELECT user_id from users where user_email=%s)," \
                "%s," \
                "%s," \
                "%s)"

INSERT_LESSON = "INSERT INTO lessons (lesson_name, lesson_description, lesson_text, lesson_rate, lang_id, author_id, lesson_tags, added_time, last_update) " \
              "VALUES (" \
                "%s, " \
                "%s, " \
                "%s, " \
                "%s," \
                "(SELECT lang_id from programming_langs where lang_name=%s)," \
                "(SELECT user_id from users where user_email=%s)," \
                "%s," \
                "%s," \
                "%s);"

INSERT_TASK = "INSERT INTO tasks (task_name, task_description, task_text, task_rate, author_id, task_difficulty, test_input, expected_output, lang_id, added_time, last_update) " \
              "VALUES (" \
                "%s, " \
                "%s, " \
                "%s, " \
                "%s," \
                "(SELECT user_id from users where user_email=%s)," \
                "%s," \
                "%s," \
                "%s," \
                "(SELECT lang_id from programming_langs where lang_name=%s)," \
                "%s," \
                "%s);" \

INSERT_SEEN_TASK =  """INSERT INTO users_to_tasks (user_id, task_id, "isSeen", "isDecided") VALUES (%s, %s, %s, %s)"""

INSERT_SEEN_LESSON =  """INSERT INTO users_to_lessons (user_id, lesson_id, "isSeen") VALUES (%s, %s, %s)"""

INSERT_SEEN_ARTICLE =  """INSERT INTO users_to_articles (user_id, article_id, "isSeen") VALUES (%s, %s, %s)"""

INSERT_SEEN_NEWS =  """INSERT INTO users_to_news (user_id, news_id, "isSeen") VALUES (%s, %s, %s)"""

INSERT_TASK_TO_LESSON = "INSERT INTO tasks_to_lessons (task_id, lesson_id) " \
                        "VALUES" \
                        "((SELECT task_id from tasks where task_name = %s), %s)"

UPDATE_ARTICLE = """UPDATE articles SET 
                 article_name = %s, 
                 article_description = %s, 
                 article_text = %s, 
                 lang_id = (SELECT lang_id from programming_langs WHERE lang_name = %s), 
                 article_tags = %s,
                 last_update = %s,
                 "isModerated" = %s
                 WHERE article_id = %s"""

UPDATE_NEWS =    "UPDATE news SET " \
                 "news_name = %s, " \
                 "news_description = %s, " \
                 "news_text = %s, " \
                 "news_tags = %s," \
                 "news_importance = %s," \
                 "last_update = %s " \
                 "WHERE news_id = %s"

UPDATE_LESSON = """UPDATE lessons SET
                 lesson_name = %s, 
                 lesson_description = %s, 
                 lesson_text = %s, 
                 lang_id = (SELECT lang_id from programming_langs WHERE lang_name = %s),
                 lesson_tags = %s,
                 last_update = %s,
                 "isModerated" = %s
                 WHERE lesson_id = %s"""

UPDATE_TASK =    """UPDATE tasks SET
                 task_name = %s, 
                 task_description = %s, 
                 task_text = %s, 
                 lang_id = (SELECT lang_id from programming_langs WHERE lang_name = %s), 
                 task_difficulty = %s, 
                 test_input = %s, 
                 expected_output = %s,
                 last_update = %s,
                 "isModerated" = %s
                 WHERE task_id = %s"""

UPDATE_ISMODER_ARTICLE = """UPDATE articles set "isModerated"=%s where article_id=%s and author_id=%s"""

UPDATE_ISMODER_LESSON = """UPDATE lessons set "isModerated"=%s where lesson_id=%s and author_id=%s"""

UPDATE_ISMODER_TASK = """UPDATE tasks set "isModerated"=%s where task_id=%s and author_id=%s"""

UPDATE_TASK_DECIDED = """UPDATE users_to_tasks SET "isDecided"=%s WHERE task_id=%s AND user_id=%s"""

UPDATE_ARTICLE_VIEWS = "UPDATE articles SET article_views = article_views + 1 WHERE article_id = %s"

UPDATE_NEWS_VIEWS = "UPDATE news SET news_views = news_views + 1 WHERE news_id = %s"

UPDATE_LESSON_VIEWS = "UPDATE lessons SET lesson_views = lesson_views + 1 WHERE lesson_id = %s"

UPDATE_TASKS_VIEWS = "UPDATE tasks SET task_views = task_views + 1 WHERE task_id = %s"

UPDATE_ARTICLE_PLUS_RATE    = "UPDATE articles SET article_rate = article_rate + 1 WHERE article_id =%s"

UPDATE_ARTICLE_MINUS_RATE   = "UPDATE articles SET article_rate = article_rate - 1 WHERE article_id =%s"

UPDATE_ARTICLE_VOTE         = """UPDATE users_to_articles SET "upVote" = %s, "downVote" = %s WHERE article_id = %s AND user_id=%s"""

UPDATE_NEWS_PLUS_RATE       = "UPDATE news SET news_rate = news_rate + 1 WHERE news_id = %s"

UPDATE_NEWS_MINUS_RATE      = "UPDATE news SET news_rate = news_rate - 1 WHERE news_id = %s"

UPDATE_NEWS_VOTE            = """UPDATE users_to_news SET "upVote" = %s, "downVote" = %s WHERE news_id = %s AND user_id=%s"""

UPDATE_LESSON_PLUS_RATE     =  "UPDATE lessons SET lesson_rate = lesson_rate + 1 WHERE lesson_id = %s"

UPDATE_LESSON_MINUS_RATE    = "UPDATE lessons SET lesson_rate = lesson_rate - 1 WHERE lesson_id = %s"

UPDATE_LESSON_VOTE          = """UPDATE users_to_lessons SET "upVote" = %s, "downVote" = %s WHERE lesson_id = %s AND user_id=%s"""

UPDATE_TASK_PLUS_RATE       = "UPDATE tasks SET task_rate = task_rate + 1 WHERE task_id = %s"

UPDATE_TASK_MINUS_RATE      = "UPDATE tasks SET task_rate = task_rate - 1 WHERE task_id = %s"

UPDATE_TASK_VOTE            = """UPDATE users_to_tasks SET "upVote" = %s, "downVote" = %s WHERE task_id = %s AND user_id=%s"""

UPDATE_LINK_TASK_TO_LESSON  = "UPDATE tasks_to_lessons SET lesson_id=%s, task_id=%s WHERE task_id=%s AND lesson_id = %s"

DELETE_ARTICLE = "DELETE FROM articles USING users " \
                 "WHERE articles.author_id = (SELECT user_id FROM users WHERE user_name = %s) AND " \
                 "articles.article_id = %s"

DELETE_NEWS = "DELETE FROM news USING users " \
                 "WHERE news.author_id = (SELECT user_id FROM users WHERE user_name = %s) AND " \
                 "news.news_id = %s"

DELETE_TASK = "DELETE FROM tasks USING users " \
                 "WHERE tasks.author_id = (SELECT user_id FROM users WHERE user_name = %s) AND " \
                 "tasks.task_id = %s"

DELETE_LESSON = "DELETE FROM lessons USING users " \
                 "WHERE lessons.author_id = (SELECT user_id FROM users WHERE user_name = %s) AND " \
                 "lessons.lesson_id = %s"

DELETE_LINK_TASK_TO_LESSON = "DELETE FROM tasks_to_lessons WHERE lesson_id = %s and task_id=%s "