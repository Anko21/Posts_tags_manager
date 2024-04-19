from lib.post import *

def test_post_object_initialization():
    post = Post(1, 'coding')
    assert post.title == 'coding'
    assert post.id == 1

def test_equality_between_two_post_obj():
    post_1 = Post(1, 'coding')
    post_2 = Post(1, 'coding')
    assert post_1 == post_2

def test_post_prints_a_nice_format():
    post = Post(1, 'coding')
    assert str(post) == 'Post(1, coding, [])'