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


    6. Search for other status(This section needs to be manually modified.)

      e.g.

      6.1  ./seahub/seahub/auth/views.py:416:                       context_instance=context_instance
           ./seahub/thirdpart/registration/views.py:96:             context_instance=context

            context = RequestContext(request)
            for key, value in extra_context.items():
                context[key] = callable(value) and value() or value

            return render(request, template_name,
                                    kwargs,
                                    context_instance=context)


      6.2  ./seahub/seahub/avatar/views.py:131:

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

      6.3  ./seahub/seahub/views/file.py:969:

            return render(request, 'share_access_validation.html', d,
                                   context_instance=RequestContext(request))
'''

import subprocess


step1 = "sed -i 's/render_to_response(/render(request, /g' `grep 'render_to_response' -rl  ./seahub/*`"

step2 = "sed -i 's/, context_instance=RequestContext(request)//g' `grep 'render_to_response' -rl  ./seahub/*`"

step3 = "sed -i 's/from django.template import RequestContext,/from django.template import/g' `grep 'render_to_response' -rl  ./seahub/*`"

step4 = "sed -i 's/from django.template import RequestContext//g' `grep 'render_to_response' -rl  ./seahub/*`"

step5 = "sed -i 's/import render_to_response/import render/g' `grep 'render_to_response' -rl  ./seahub/*`"

step6 = "sed -i 's/render_to_string(/render(request, /g' `grep 'render_to_string' -rl  ./seahub/*`"

step7 = "sed -i 's/, context_instance=RequestContext(request)//g' `grep 'render_to_string' -rl  ./seahub/*`"

step8 = "sed -i 's/from django.template import RequestContext//g' `grep 'render_to_string' -rl  ./seahub/*`"

step9 = "sed -i 's/from django.template.loader import render_to_string/from django.shortcuts import render/g' `grep 'render_to_string' -rl  ./seahub/*`"


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

for step in steps:
    subprocess.call([step], shell=True)


subprocess.call(["grep -rn 'context_instance=RequestContext' ./seahub/*"], shell=True)

subprocess.call(["grep -rn 'context_instance=context_instance' ./seahub/*"], shell=True)

subprocess.call(["grep -rn 'context_instance = RequestContext' ./seahub/*"], shell=True)

subprocess.call(["grep -rn 'context_instance=' ./seahub/*"], shell=True)

