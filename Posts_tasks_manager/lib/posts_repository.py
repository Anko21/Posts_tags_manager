from lib.post import *
from lib.tag import *

class PostRepository:

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM posts')

        posts = []
        for row in rows:
            item = Post(row['id'], row['title'])
            posts.append(item)

        return posts
    
    def create(self,post):
        self.connection.execute('INSERT INTO posts (id, title) VALUES(%s, %s)', [post.id, post.title])

    # def delete(self,post_title):
    #     self.connection.execute('DELETE FROM posts WHERE title = %s',[post_title])

    def find(self, post_id):
        rows = self.connection.execute('SELECT * FROM posts WHERE id = %s',[post_id])

        posts = []
        for row in rows:
            item = Post(row['id'], row['title'])
            posts.append(item)

        return posts
    
    def find_by_tag(self, tag_name):
        rows = self.connection.execute(
            '''SELECT * FROM posts 
                    JOIN posts_tags ON posts_tags.post_id = posts.id
                    JOIN tags on posts_tags.tag_id = tags.id
                    WHERE tags.name = %s''',
                [tag_name]
            )
        posts = []
        for row in rows:
            item= Post(row['post_id'], row['title'])
            posts.append(item) 
        
        tag = Tag(rows[0]['id'], rows[0]['name'],posts)
        return tag