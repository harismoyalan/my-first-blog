from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD


def post_list(request):
	pass
=======
def post_list(request):
    return render(request, 'blog/post_list.html', {})
>>>>>>> 6328d938a27219004ade19416a0f589d2a00444f
