from lib.tag import *

def test_tag_object_initialization():
    tag = Tag(1, 'coding')
    assert tag.name == 'coding'
    assert tag.id == 1

def test_equality_between_two_tag_obj():
    tag_1 = Tag(1, 'coding')
    tag_2 = Tag(1, 'coding')
    assert tag_1 == tag_2

def test_tag_prints_a_nice_format():
    tag = Tag(1, 'coding')
    assert str(tag) == 'Tag(1, coding, [])'