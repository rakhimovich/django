from django.shortcuts import render, redirect

from apps.comments.models import Comment

def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return redirect('homepage')


def update_comment(request,pk):
    comment = Comment.objects.get(id=pk)

    if request.method == 'POST':
        text = request.POST['text']
        comment.text = text
        comment.save()

        return redirect('homepage')


    return render(request, 'update_comment.html',locals())
