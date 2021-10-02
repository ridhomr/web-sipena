from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def feedback_list(request):
	context = {
		'daftar_feedback': Feedback.objects.all()
	}
	return render(request, "feedback/feedback_list.html", context)


def feedback_form(request, id=0):
	if request.method == "POST":
		if id == 0:
			form = FeedbackForm(request.POST)
		else:
			feed = Feedback.objects.get(pk=id)
			form = FeedbackForm(request.POST, instance=feed)
		form.save()
		return redirect('/feedback')

	else:
		if id == 0:
			form = FeedbackForm()
		else:
			feed = Feedback.objects.get(pk=id)
			form = FeedbackForm(instance=feed)
		return render(request, "feedback/feedback_form.html", {'form':form})


def feedback_delete(request, id):
	feed = Feedback.objects.get(pk=id)
	feed.delete()
	return redirect('/feedback/list')