from lib.posts_repository import *
from lib.post import *


def test_get_all_post_records(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)

    posts = repository.all()
    assert posts == [
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(4, 'My weekend in Edinburgh'),
        Post(5, 'The best chocolate cake EVER'),
        Post(6, 'A foodie week in Spain'),
        Post(7, 'SQL basics')
    ]

def test_create_adds_a_post_in_table(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)

    repository.create( Post(8,"Free time"))

    posts = repository.all()
    assert posts == [
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(4, 'My weekend in Edinburgh'),
        Post(5, 'The best chocolate cake EVER'),
        Post(6, 'A foodie week in Spain'),
        Post(7, 'SQL basics'),
        Post(8, 'Free time')
    ] 

# def test_delete_a_postin_table(db_connection):
#     db_connection.seed("seeds/blog_posts_tags.sql")
#     repository = PostRepository(db_connection)

#     repository.delete('Fun classes')

#     posts = repository.all()
#     assert posts == [
#         Post(1, 'How to use Git'),
#         Post(3, 'Using a REPL'),
#         Post(4, 'My weekend in Edinburgh'),
#         Post(5, 'The best chocolate cake EVER'),
#         Post(6, 'A foodie week in Spain'),
#         Post(7, 'SQL basics'),
#         Post(8, 'Free time')
#     ] 

def test_find_post_records_with_a_specific_id(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)

    post = repository.find(2)
    assert post == [Post(2, 'Fun classes')]

def test_find_by_tag_returns_posts_with_tag(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = PostRepository(db_connection)

    result = repository.find_by_tag("coding")
    assert result == Tag(1, 'coding', [
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(7, 'SQL basics'),
    ])
