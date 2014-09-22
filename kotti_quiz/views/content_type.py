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
from kotti_quiz.resources import ContentType
from kotti_quiz.views import BaseView


class ContentTypeSchema(ContentSchema):
    example_text = colander.SchemaNode(colander.String())


@view_config(name=ContentType.type_info.add_view,
             permission='add',
             renderer='kotti:templates/edit/node.pt',)
class ContentTypeAddForm(AddFormView):
    schema_factory = ContentTypeSchema
    add = ContentType
    item_type = _(u"ContentType")


@view_config(name='edit',
             context=ContentType, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class ContentTypeEditForm(EditFormView):
    schema_factory = ContentTypeSchema


@view_defaults(context=ContentType)
class ContentTypeView(BaseView):
    """View for the Content Type """

    @view_config(name="view", permission="view",
                 renderer='kotti_quiz:templates/view.pt')
    def view_content_type(self):
        return {
            'example_text': u'foo…',
        }
