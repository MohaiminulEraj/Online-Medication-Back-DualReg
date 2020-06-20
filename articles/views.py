from django.shortcuts import render, redirect
from articles.models import PostedArticle


def editorpanel(request):
    if request.method == 'GET':
        return render(request, 'articles/editorpanel.html')
    elif request.method == 'POST':
        postarticle = PostedArticle()
        postarticle.title = request.POST['title']
        postarticle.topic = request.POST['topic']
        postarticle.description = request.POST['description']
        postarticle.image = request.POST['myfile']
        postarticle.causes = request.POST['causes']
        postarticle.stages = request.POST['stages']
        postarticle.image2 = request.POST['myfile2']
        postarticle.consequences = request.POST['consequences']
        postarticle.remedies_and_treatment = request.POST['remedies']
        postarticle.image3 = request.POST['myfile3']
        postarticle.question_and_answer = request.POST['question']
        postarticle.prevention = request.POST['prevention']
        postarticle.adverse = request.POST['adverse']
        postarticle.side_effect = request.POST['sideEffect']
        postarticle.diagnosis = request.POST['diagnosis']
        postarticle.symptomps = request.POST['symptoms']
        postarticle.user_id = request.POST['uID']
        postarticle.doc_user_id = request.POST['duID']
        postarticle.ref_link = request.POST['refLink']

        postarticle.save()
        return redirect('editorpanel')
        # store_article = PostedArticle.title
        # .save(title=title, topic=topic, description=description, image=image, causes=causes, stages=stages, image2=image2, consequences=consequences, remedies_and_treatment=remedies_and_treatment, image3=image3,)

        # if RegDoctor.objects.filter(username=username).exists():
        #     return render(request, 'users/regDoctor.html', {'form': UserCreationForm(), 'error': "That username has already been taken. Please chose a new username"})
        # if RegDoctor.objects.filter(email=email).exists():
        #     return render(request, 'users/regDoctor.html', {'form': UserCreationForm(), 'error': "That email has already been taken. Please chose a new email"})
        # if password == confirm_password:
        #     user_doc = RegDoctor.objects.create_user(
        #         username=username, first_name=first_name, last_name=last_name, email=email, password=password, date_of_birth=date_of_birth, gender=gender, license_no=license_no, university=university, referral_id=referral_id, city=city, country=country, zip_code=zip_code, phone=phone)
        #     user_doc.save()
        #     login(request, user_doc)
        #     return redirect('index')
        # else:
        #     return render(request, 'users/regDoctor.html', {'form': UserCreationForm(), 'error': "Passwords did not match"})
