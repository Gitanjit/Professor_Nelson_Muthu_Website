from django.shortcuts import render, get_object_or_404
from .models import Award, Education, Experience , Publication, Course, Curr_student, Passed_student, Project, ProjectImage, Review, Collaboration, Collaboration_acad, Position, Research, Company, Book, Service


# Create your views here.
def home(request):
    educations = Education.objects.all()
    awards = Award.objects.all()
    projects = Project.objects.all()
    projectImages = ProjectImage.objects.all()
    courses = Course.objects.all()
    curr_students = Curr_student.objects.all()
    collaborations = Collaboration.objects.all()
    experiences = Experience.objects.all()
    companys = Company.objects.all()
    collaboration_acads = Collaboration_acad.objects.all()
    services = Service.objects.all()
    data = {
        'awards': awards,
        'educations': educations,
        'projects': projects,
        'projectImages': projectImages,
        'courses': courses,
        'curr_students': curr_students,
        'collaborations': collaborations,
        'collaboration_acads': collaboration_acads,
        'experiences': experiences,
        'companys': companys,
        'services': services,
    }
    return render(request, 'home.html', data)


def teaching(request):
    positions = Position.objects.all()
    courses = Course.objects.all()
    curr_students = Curr_student.objects.all()
    passed_students = Passed_student.objects.all()
    companys = Company.objects.all()
    data = {
        'positions': positions,
        'courses': courses,
        'curr_students': curr_students,
        'passed_students': passed_students,
        'companys': companys,
    }
    return render(request, 'teaching.html', data)


def projectpg(request):
    projects = Project.objects.all()
    projectImages = ProjectImage.objects.all()
    collaborations = Collaboration.objects.all()
    companys = Company.objects.all()
    collaboration_acads = Collaboration_acad.objects.all()
    data = {
        'projects': projects,
        'projectImages': projectImages,
        'collaborations': collaborations,
        'companys': companys,
        'collaboration_acads': collaboration_acads,
    }
    return render(request, 'projectpg.html', data)


def publicationpg(request):
    researchs = Research.objects.all()
    publications = Publication.objects.all()
    reviews = Review.objects.all()
    companys = Company.objects.all()
    books = Book.objects.all()
    data = {
        'researchs': researchs,
        'publications': publications,
        'reviews': reviews,
        'companys': companys,
        'books': books,
    }
    return render(request, 'publicationpg.html', data)


def projview(request, id):
    project = get_object_or_404(Project, proj_id=id)
    photos = ProjectImage.objects.filter(project=project)
    return render(request, 'projpop.html', {
        'project':project,
        'photos':photos
    })