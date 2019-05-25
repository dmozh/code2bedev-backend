from .views import response
import credentials as crs

def setup_routes(app):
    app.router.add_route('GET', f'{crs.API}test', response.test)

    app.router.add_route('POST', f'{crs.API}addUser', response.add_user)
    app.router.add_route('POST', f'{crs.API}addArticle', response.add_article)
    app.router.add_route('POST', f'{crs.API}addNews', response.add_news)
    app.router.add_route('POST', f'{crs.API}addTask', response.add_task)
    app.router.add_route('POST', f'{crs.API}addLesson', response.add_lesson)

    app.router.add_route('POST', f'{crs.API}updateUserArticle', response.update_user_article)
    app.router.add_route('POST', f'{crs.API}updateUserNews', response.update_user_news)
    app.router.add_route('POST', f'{crs.API}updateUserTask', response.update_user_task)
    app.router.add_route('POST', f'{crs.API}updateUserLesson', response.update_user_lesson)
    app.router.add_route('POST', f'{crs.API}updatePostRate', response.update_vote_post)
    app.router.add_route('POST', f'{crs.API}updateIsModerated', response.update_is_moderated)

    app.router.add_route('POST', f'{crs.API}addSeenPost', response.insert_seen_post)

    app.router.add_route('POST', f'{crs.API}deleteUserArticle', response.delete_user_article)
    app.router.add_route('POST', f'{crs.API}deleteUserNews', response.delete_user_news)
    app.router.add_route('POST', f'{crs.API}deleteUserTask', response.delete_user_task)
    app.router.add_route('POST', f'{crs.API}deleteUserLesson', response.delete_user_lesson)

    app.router.add_route('POST', f'{crs.API}getUser', response.get_user)
    app.router.add_route('POST', f'{crs.API}getUserLessonsName', response.get_user_lessons_name)

    app.router.add_route('POST', f'{crs.API}getUserLessons', response.get_user_lessons)
    app.router.add_route('POST', f'{crs.API}getUserTasks', response.get_user_tasks)
    app.router.add_route('POST', f'{crs.API}getUserNews', response.get_user_news)
    app.router.add_route('POST', f'{crs.API}getUserArticles', response.get_user_articles)
    app.router.add_route('POST', f'{crs.API}getUserAllPosts', response.get_user_posts)

    app.router.add_route('POST', f'{crs.API}getArticles', response.get_articles)
    app.router.add_route('POST', f'{crs.API}getLessons', response.get_lessons)
    app.router.add_route('POST', f'{crs.API}getTasks', response.get_tasks)
    app.router.add_route('POST', f'{crs.API}getUnModeratedPosts', response.get_unmoderated_posts)
    app.router.add_route('GET',  f'{crs.API}getNews', response.get_news)

    app.router.add_route('POST', f'{crs.API}getPostInfo', response.get_post_info)

    app.router.add_route('POST', f'{crs.API}executeCode', response.execute_request_to_jdoodle)
    app.router.add_route('POST', f'{crs.API}checkExecuteCode', response.request_to_jdoodle_with_check_valid)

    app.router.add_route('GET', f'{crs.API}getLangsName', response.get_langs_name)
    app.router.add_route('GET', f'{crs.API}getLangs', response.get_langs)