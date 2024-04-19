from lib.tag import *
from lib.post import *

class TagRepository:

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM tags')

        tags = []
        for row in rows:
            item = Tag(row['id'], row['name'])
            tags.append(item)

        return tags
    
    def create(self,tag):
        self.connection.execute('INSERT INTO tags (id, name) VALUES(%s, %s)', [tag.id, tag.name])

    # def delete(self,tag_name):
    #     self.connection.execute('DELETE FROM tags WHERE name = %s',[tag_name])

    def find(self, tag_id):
        rows = self.connection.execute('SELECT * FROM tags WHERE id = %s',[tag_id])

        tags = []
        for row in rows:
            item = Tag(row['id'], row['name'],[])
            tags.append(item)

        return tags
    
    def find_by_post(self, post_id):
        rows = self.connection.execute(
            '''SELECT * FROM tags 
                    JOIN posts_tags ON posts_tags.tag_id = tags.id
                    JOIN posts on posts_tags.post_id = posts.id
                    WHERE posts.id = %s''',
                [post_id]
            )
        tags = []
        for row in rows:
            item = Tag(row['tag_id'], row['name'])
            tags.append(item) 
        
        post = Post(rows[0]['id'], rows[0]['title'],tags)
        return post
    
    