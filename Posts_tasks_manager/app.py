from lib.database_connection import DatabaseConnection
from lib.posts_repository import*
from lib.tags_repository import *

class Application():
    # Connect to the database
    def __init__(self):
        self.connection = DatabaseConnection()
        self.connection.connect()
        self.connection.seed("seeds/blog_posts_tags.sql")

    def run(self):
        post_repository = PostRepository(self.connection)
        tag_repository = TagRepository(self.connection)

        posts = post_repository.find_by_tag("coding")
        tags = tag_repository.find_by_post(3)


        for post in posts:
            print(post)

        # for tag in tags:
        #     print(tag)

if __name__ == '__main__':
    app = Application()
    app.run()