from lib.tags_repository import *
from lib.tag import *


def test_get_all_tag_records(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = TagRepository(db_connection)

    tags = repository.all()
    assert tags == [
        Tag(1, "coding"),
        Tag(2, "travel"),
        Tag(3, "cooking"),
        Tag(4, "education"),
    ]

def test_create_adds_a_tag_in_table(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = TagRepository(db_connection)

    repository.create( Tag(5,"climbing"))

    tags = repository.all()
    assert tags == [
        Tag(1, "coding"),
        Tag(2, "travel"),
        Tag(3, "cooking"),
        Tag(4, "education"),
        Tag(5, "climbing")
    ] 

# def test_delete_a_tag_in_table(db_connection):
#     db_connection.seed("seeds/blog_posts_tags.sql")
#     repository = TagRepository(db_connection)

#     repository.delete('cooking')

#     tags = repository.all()
#     assert tags == [
#         Tag(1, "coding"),
#         Tag(2, "travel"),
#         Tag(4, "education"),
#     ] 

def test_find_records_with_a_specific_id(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = TagRepository(db_connection)

    tag = repository.find(2)
    assert tag == [Tag(2, "travel")]


def test_find_by_post(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repository = TagRepository(db_connection)

    result = repository.find_by_post(3)
    assert result == Post(3, 'Using a REPL', [
        Tag(1, "coding"),
        Tag(4, "education"),
    ])