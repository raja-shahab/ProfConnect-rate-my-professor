from django.shortcuts import render, redirect
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from AI_rate_professor import settings
from .models import Professor, Newsletter
from django.core.mail import send_mail
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            send_mail(
                subject=f"Message from {name}",
                message=message,
                from_email=email,
                recipient_list=[settings.EMAIL_HOST_USER]
            )
            messages.success(request, 'Your message has been sent successfully.')
        else:
            messages.warning(request, 'Please fill out all fields in the contact form.')

    return render(request, 'index.html')


def add_professors(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        expertise = request.POST.get('expertise')
        subject = request.POST.get('subject')
        rating = request.POST.get('rating')
        experience = request.POST.get('experience')

        Professor.objects.create(
            name=name,
            expertise=expertise,
            subject=subject,
            rating=rating,
            experience=experience
        )
        return redirect('add_professors/')

    queryset = Professor.objects.all()

    context = {
        'queryset': queryset
    }

    return render(request, 'add_professors.html', context)


def get_professor_recommendation(request):
    professors = None

    if request.method == 'GET':
        user_input = request.GET.get('query')

        if user_input:
            # Fetch all professors' expertise
            all_professors = Professor.objects.all()
            expertise_list = [prof.expertise for prof in all_professors]
            professor_ids = [prof.id for prof in all_professors]

            # Initialize TF-IDF Vectorizer
            vectorizer = TfidfVectorizer()

            # Fit and transform the expertise data and the query
            expertise_vectors = vectorizer.fit_transform(expertise_list)
            query_vector = vectorizer.transform([user_input])

            # Compute cosine similarity
            similarity_scores = cosine_similarity(query_vector, expertise_vectors).flatten()

            # Rank professors by similarity score
            ranked_indices = similarity_scores.argsort()[-3:][::-1]

            # Get top 3 recommended professors
            recommended_ids = [professor_ids[i] for i in ranked_indices]
            professors = Professor.objects.filter(id__in=recommended_ids)

            if professors.exists():
                return render(request, 'recommend.html', {'best_professors': professors,
                              'user_input': user_input})

    return render(request, 'recommend.html', {'professors': professors, 'user_input': user_input})
