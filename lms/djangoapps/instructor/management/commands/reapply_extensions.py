#!/usr/bin/python
from django.http import Http404
from django.core.management.base import BaseCommand, CommandError

from courseware.courses import get_course_by_id
from instructor.views.tools import fix_missing_extensions


class Command(BaseCommand):
    args = "<course_id>"
    help = "Reapply all extensions (fixes extensions for newly added problems)"

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError("insufficient arguments")
        try:
            course = get_course_by_id(args[0])
            fix_missing_extensions(course)
        except (ValueError, Http404) as e:
            raise CommandError(e)
