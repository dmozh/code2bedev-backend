from .views import response


def setup_routes(app):
    app.router.add_route('GET', '/test', response.test)

    app.router.add_route('POST', '/addUser', response.add_user)
    app.router.add_route('POST', '/addArticle', response.add_article)
    app.router.add_route('POST', '/addNews', response.add_news)
    app.router.add_route('POST', '/addTask', response.add_task)
    app.router.add_route('POST', '/addLesson', response.add_lesson)

    app.router.add_route('POST', '/updateUserArticle', response.update_user_article)
    app.router.add_route('POST', '/updateUserNews', response.update_user_news)
    app.router.add_route('POST', '/updateUserTask', response.update_user_task)
    app.router.add_route('POST', '/updateUserLesson', response.update_user_lesson)
    app.router.add_route('POST', '/updatePostRate', response.update_vote_post)

    app.router.add_route('POST', '/addSeenPost', response.insert_seen_post)

    app.router.add_route('POST', '/deleteUserArticle', response.delete_user_article)
    app.router.add_route('POST', '/deleteUserNews', response.delete_user_news)
    app.router.add_route('POST', '/deleteUserTask', response.delete_user_task)
    app.router.add_route('POST', '/deleteUserLesson', response.delete_user_lesson)

    app.router.add_route('POST', '/getUser', response.get_user)
    app.router.add_route('POST', '/getUserLessonsName', response.get_user_lessons_name)

    app.router.add_route('POST', '/getUserLessons', response.get_user_lessons)
    app.router.add_route('POST', '/getUserTasks', response.get_user_tasks)
    app.router.add_route('POST', '/getUserNews', response.get_user_news)
    app.router.add_route('POST', '/getUserArticles', response.get_user_articles)
    app.router.add_route('POST', '/getUserAllPosts', response.get_user_posts)

    app.router.add_route('POST', '/getArticles', response.get_articles)
    app.router.add_route('POST', '/getLessons', response.get_lessons)
    app.router.add_route('POST', '/getTasks', response.get_tasks)
    app.router.add_route('POST', '/getLessonTasks', response.get_lesson_tasks)
    app.router.add_route('GET',  '/getNews', response.get_news)

    app.router.add_route('POST', '/getPostText', response.get_post_text)

    app.router.add_route('POST', '/executeCode', response.execute_request_to_jdoodle)
    app.router.add_route('POST', '/checkExecuteCode', response.request_to_jdoodle_with_check_valid)

    app.router.add_route('GET', '/getLangsName', response.get_langs_name)
    app.router.add_route('GET', '/getLangs', response.get_langs)