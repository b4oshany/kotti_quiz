# -*- coding: utf-8 -*-

"""
Created on 2014-09-22
:author: Andreas Kaiser (disko)
"""

import colander
from kotti.views.edit import AddFormView
from kotti.views.edit import ContentSchema
from kotti.views.edit import EditFormView
from pyramid.view import view_config
from pyramid.view import view_defaults


from kotti_quiz import _
from kotti_quiz.resources import Quiz
from kotti_quiz.resources import Question
from kotti_quiz.resources import Answer
from kotti_quiz.views import BaseView


class QuizSchema(ContentSchema):
    title = colander.SchemaNode(
        colander.String(),
        title = u'Quiz Bezeichnung',
        )


class QuestionSchema(ContentSchema):
    title = colander.SchemaNode(
        colander.String(),
        title = u'Question:',
        )
    correctanswer = colander.SchemaNode(
        colander.String(),
        title = u'Correct Answer:',
        )


class AnswerSchema(ContentSchema):
    title = colander.SchemaNode(
        colander.String(),
        title = u'Answering <Choice></Choice>:',
        )


@view_config(name=Quiz.type_info.add_view,
             permission='add',
             renderer='kotti:templates/edit/node.pt',)
class QuizAddForm(AddFormView):
    schema_factory = QuizSchema
    add = Quiz
    item_type = _(u"Quiz")


@view_config(name=Question.type_info.add_view,
             permission='add',
             renderer='kotti:templates/edit/node.pt',)
class QuestionAddForm(AddFormView):
    schema_factory = QuestionSchema
    add = Question
    item_type = _(u"Question")


@view_config(name=Answer.type_info.add_view,
             permission='add',
             renderer='kotti:templates/edit/node.pt',)
class AnswerAddForm(AddFormView):
    schema_factory = AnswerSchema
    add = Answer
    item_type = _(u"Answer")


@view_config(name='edit',
             context=Quiz, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class QuizEditForm(EditFormView):
    schema_factory = QuizSchema


@view_config(name='edit',
             context=Question, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class QuestionEditForm(EditFormView):
    schema_factory = QuestionSchema


@view_config(name='edit',
             context=Answer, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class AnswerEditForm(EditFormView):
    schema_factory = AnswerSchema


@view_defaults(context=Quiz, permission="view")
class QuizView(BaseView):
    """View for Quiz Content Type"""

    @view_config(name="view",
                 request_method='GET',
                 renderer='kotti_quiz:templates/quizview.pt')
    def view_quiz(self):
        questions = self.context.children
        return {
            'questions': questions,
        }

    @view_config(name='view',
                 request_method='POST',
                 renderer='kotti_quiz:templates/checkview.pt')
    def check_answers(self):
        questions = self.context.children
        answers = self.request.POST
        sumtotal = 0
        sumcorrect = 0
        questioncorrect = {question.name: False for question in questions}
        for question in questions:
            sumtotal += 1
            #import pdb; pdb.set_trace()
            if question.name in answers:
                if question.correctanswer == answers[question.name]:
                    questioncorrect[question.name] = True
                    sumcorrect += 1

        return {
            'questions': questions,
            'questioncorrect': questioncorrect,
            'sumtotal': sumtotal,
            'sumcorrect': sumcorrect,
        }


@view_defaults(context=Question)
class QuestionView(BaseView):
    """View for Question Content Type"""

    @view_config(name="view", permission="view",
                 renderer='kotti_quiz:templates/questionview.pt')
    def view_question(self):
        answers = self.context.values()
        return {
            'answers': answers,
        }
