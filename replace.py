# -*- coding: utf-8 -*-
'''
  This is an automatic replacement script
  version : v1.0
  Functions:
    1.  Through step1, step2 to REPLACE "render_to_response('template.html', {...}, context_instance=RequestContext(request))"
                                WITH    "render(request, 'template.html', {....})"

    2.  Through step3, step4, step8 DELETE "from django.template import RequestContext"

    3.  Through step5 to REPLACE "from django.shortcuts import render_to_response"
                         WITH "from django.shortcuts import render"

    4.  Through step6, step7 to REPLACE "render_to_string('template.html', {...}, context_instance=RequestContext(request))"
                                WITH "render(request, 'template.html', {....})"

    5.  Through step9 to REPLACE "from django.template.loader import render_to_string"
                         WITH    "from django.shortcuts import render"


    6. Search for other status(This section needs to be manually modified. step10, step11)

      e.g.

      6.1  ./seahub/seahub/auth/views.py:416:                       context_instance=context_instance
           ./seahub/thirdpart/registration/views.py:96:             context_instance=context

            context = RequestContext(request)
            for key, value in extra_context.items():
                context[key] = callable(value) and value() or value

            return render(request, template_name,
                                    kwargs,
                                    context_instance=context)

      6.2  ./seahub/seahub/views/file.py:969:

            return render(request, 'share_access_validation.html', d,
                                   context_instance=RequestContext(request))

      6.3  ./seahub/seahub/avatar/views.py:131:

                return render(request,
                                   'avatar/confirm_delete.html',
                                   extra_context,
                                   context_instance = RequestContext(
                                                    request,
                                                    { 'avatar': avatar,
                                                      'avatars': avatars,
                                                      'delete_avatar_form': delete_avatar_form,
                                                      'next': next_override or _get_next(request), }
                                                    )
                                  )

'''

from subprocess import call


class Replace(object):
    def __init__(self):
        pass

    def origin_replace(self, path="~/dev/seahub/*"):
        step1 = "sed -i 's/render_to_response(/render(request, /g' `grep 'render_to_response' -rl  %s`" % path

        step2 = "sed -i 's/, context_instance=RequestContext(request)//g' `grep 'render_to_response' -rl  %s`" % path

        step3 = "sed -i 's/from django.template import RequestContext,/from django.template import/g' `grep 'render_to_response' -rl  %s`" % path

        step4 = "sed -i 's/from django.template import RequestContext//g' `grep 'render_to_response' -rl  %s`" % path

        step5 = "sed -i 's/import render_to_response/import render/g' `grep 'render_to_response' -rl  %s`" % path

        step6 = "sed -i 's/render_to_string(/render(request, /g' `grep 'render_to_string' -rl  %s`" % path

        step7 = "sed -i 's/, context_instance=RequestContext(request)//g' `grep 'render_to_string' -rl  %s`" % path

        step8 = "sed -i 's/from django.template import RequestContext//g' `grep 'render_to_string' -rl  %s`" % path

        step9 = "sed -i 's/from django.template.loader import render_to_string/from django.shortcuts import render/g' `grep 'render_to_string' -rl  %s`" % path

        # step10 = "grep -rn 'context_instance=RequestContext' %s" % path

        # step11 = "grep -rn 'context_instance=context_instance' %s" % path

        # step12 = "grep -rn 'context_instance=context' %s" % path

        step10 = "grep -rn 'context_instance=' %s" % path

        step11 = "grep -rn 'context_instance = RequestContext' %s" % path

        steps = []
        steps.append(step1)
        steps.append(step2)
        steps.append(step3)
        steps.append(step4)
        steps.append(step5)
        steps.append(step6)
        steps.append(step7)
        steps.append(step8)
        steps.append(step9)
        steps.append(step10)
        steps.append(step11)

        for step in steps:
            call([step], shell=True)

    def add_replace_by_user(self, old_string, new_string, include_string, path):
        step = "sed -i 's/%s/%s/g' `grep %s -rl  %s`" % (old_string, new_string, include_string, path)
        call([step], shell=True)

    def run(self):
        replace_status = raw_input("Whether to use a custom replacement?(yes or no): ")
        if replace_status == "yes":
            print("Please enter path like ~/dev/seahub/*")
            path = raw_input("Please enter path: ")
            self.origin_replace(path)
        else:
            self.origin_replace()


if __name__ == "__main__":
    replace = Replace()
    replace.run()
