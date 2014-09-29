from __future__ import absolute_import

from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource

library = Library("kotti_quiz", "static")
kotti_quiz_css = Resource(library, "style.css")
kotti_quiz_js = Resource(library, "quiz.js")
kotti_quiz_group = Group([kotti_quiz_css, kotti_quiz_js])
