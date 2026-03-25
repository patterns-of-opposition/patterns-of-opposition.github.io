from django.shortcuts import render, redirect
import markdown




def mk_html(_file):
    with open(_file, "r") as inf:
        return markdown.markdown(inf.read(), extensions=["sane_lists", "tables"])




def landing(request):
    context = {
            "md": mk_html(f"main/markdown/landing.md")
        }
    return render(request, 'main/landing.html', context)

def team(request):
    context = {
            "md": mk_html(f"main/markdown/team.md")
        }
    return render(request, 'main/landing.html', context)
