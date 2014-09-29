from kotti.resources import Content
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import String
from sqlalchemy import Boolean

from kotti_quiz import _
from kotti.interfaces import IDefaultWorkflow
from zope.interface import implements


class Quiz(Content):
    """Quiz Content type."""
    implements(IDefaultWorkflow)

    id = Column(Integer, ForeignKey('contents.id'), primary_key=True)

    type_info = Content.type_info.copy(
        name=u'Quiz',
        title=_(u'Quiz'),
        add_view=u'add_quiz',
        addable_to=[u'Document'],
        )


class Question(Content):
    """Question Content type."""

    id = Column(Integer, ForeignKey('contents.id'), primary_key=True)
    correct_answer = Column(Unicode(256))
    question_type = Column(String())

    # change the type info to your needs
    type_info = Content.type_info.copy(
        name=u'Question',
        title=_(u'Question'),
        add_view=u'add_question',
        addable_to=[u'Quiz'],
        )


class Answer(Content):
    """Answer Content type."""

    id = Column(Integer, ForeignKey('contents.id'), primary_key=True)
    correct = Column(Boolean())

    type_info = Content.type_info.copy(
        name=u'Answer',
        title=_(u'Answer'),
        add_view=u'add_answer',
        addable_to=[u'Question'],
        )
