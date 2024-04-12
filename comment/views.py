from django.shortcuts import render, redirect
from .models import Comment

def submit_comment(request):
    if request.method == 'POST':
        content = request.POST.get('commentaire')
        comment = Comment(content=content)
        comment.save()
        return redirect('home1')  # Redirigez vers une page de confirmation ou autre
    return render(request, 'Page_Home.html')  # Affichez le formulaire si la requête n'est pas POST

