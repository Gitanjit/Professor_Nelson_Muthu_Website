from django.db import models
from django.utils.html import format_html


# Create your models here.


# images for companys and instis
class Company(models.Model):
    comp_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, help_text='name of the institution or company')
    # project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='company/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))


# for education
class Education(models.Model):
    ed_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=20)
    position = models.CharField(max_length=100)
    # institute = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='education/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    company = models.ForeignKey(Company, default=None, on_delete=models.CASCADE, help_text='name of the institution from choices as present in company model')


# for experience
class Experience(models.Model):
    ex_id = models.AutoField(primary_key=True)
    duration = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    # company = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='experience/')
    company = models.ForeignKey(Company, default=None, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now_add=True, null=True)


# for publication
class Publication(models.Model):
    pub_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, help_text='For journal:title, book-chapters:title, conferences:topic, patent:title ')
    author = models.CharField(max_length=100, help_text='Type as author1 | author2 | ... and so on ')
    year = models.CharField(max_length=20, blank=True, help_text='For journal:issue year(e.g 116(1186):2012), book-chapters:year of publishing, conferences:year of publishing, patent:none ')
    info = models.TextField(max_length=5000, help_text='For journal:journal name and pages(e.g.journal name | page 52-56), book-chapters:name of the book, conferences:name of the conference and location(for e.g. conference name | Delhi), patent:patent id(for e.g PAT/ME/P14050-1/16-17) ')
    publication_choices = [
        ('Patents', 'Patents'), ('Conferences', 'Conferences'), ('Journals', 'Journals'),
        ('Book_Chapters', 'Book_Chapters')
    ]
    type = models.CharField(
        choices=publication_choices,
        default='Patents',
        max_length=50,
    )
    add_date = models.DateTimeField(auto_now_add=True, null=True)


# for courses
class Course(models.Model):
    c_id = models.AutoField(primary_key=True)
    course_id = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    times_conducted = models.CharField(max_length=100, help_text='Type as tenure1 | tenure2 | ... and so on  for e.g. jan2020 | july2018')
    # image = models.ImageField(upload_to='course/')
    about = models.TextField(max_length=10, blank=True, help_text='Please ignore this field')
    special_position = models.TextField(max_length=100, blank=True, help_text='e.g course coordinator etc')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    clink = models.URLField(max_length=400, default='', help_text='Type as full url link e.g. https://github.com/')
    company = models.ForeignKey(Company, default=None, on_delete=models.CASCADE, help_text='Name of the institution from choices as present in company model')


# for current students
class Curr_student(models.Model):
    cstu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=500, help_text='e.g email | phone no | linkedin etc')
    year_joining = models.CharField(max_length=20)
    about = models.TextField(max_length=5000, help_text='e.g thesis | area of interest | current lab etc')
    edlevel_choices = [
        ('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('Research Scholar', 'Research Scholar'), ('Project Staff', 'Project Staff')
    ]
    ed_level = models.CharField(
        choices=edlevel_choices,
        default='Research Scholar',
        max_length=50,
    )
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='student/')

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))


# for current students
class Passed_student(models.Model):
    pstu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=500, help_text='e.g email | phone no | linkedin etc')
    tenure = models.CharField(max_length=50, help_text='year of passing')
    about = models.TextField(max_length=5000, help_text='e.g current affiliation | new lab etc')
    edlevel_choices = [
        ('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('Research Scholar', 'Research Scholar'), ('Project Staff', 'Project Staff')
    ]
    ed_level = models.CharField(
        choices=edlevel_choices,
        default='Research Scholar',
        max_length=50,
    )
    add_date = models.DateTimeField(auto_now_add=True, null=True)


# for projects
class Project(models.Model):
    proj_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)
    tenure = models.CharField(max_length=100, help_text='year1-year2 e.g. 2018-2021')
    project_value = models.CharField(max_length=50, blank=True, help_text='in lakhs INR')
    pi = models.CharField(max_length=100, blank=True, help_text='principal investigator')
    copi = models.CharField(max_length=100, blank=True, help_text='co-principal investigator')
    about = models.TextField(max_length=5000)
    pr_choices = [
        ('Consultancy', 'Consultancy'), ('Sponsored', 'Sponsored')
    ]
    type = models.CharField(
        choices=pr_choices,
        default='Consultancy',
        max_length=50,
    )
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='project/', help_text='featured image')
    featured = models.BooleanField(default=False)

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))


# images for project
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE, help_text='project id connected to set of images')
    images = models.ImageField(upload_to='project/', help_text='set of images to be viewed along with project')
    add_date = models.DateTimeField(auto_now_add=True, null=True)


# for reviews(only journals)
class Review(models.Model):
    rev_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text='journal name')
    add_date = models.DateTimeField(auto_now_add=True, null=True)


# for collabs
class Collaboration(models.Model):
    col_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text='industrial agency/company name')
    add_date = models.DateTimeField(auto_now_add=True, null=True)


# for collabs_academic
class Collaboration_acad(models.Model):
    col_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text='academic agency/institute name')
    add_date = models.DateTimeField(auto_now_add=True, null=True)


# for Position openings
class Position(models.Model):
    pos_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text='if no openings keep single field with name (Positions open: none) else type position names')
    add_date = models.DateTimeField(auto_now_add=True, null=True)


# for Research
class Research(models.Model):
    res_id = models.AutoField(primary_key=True)
    col_choices = [
        ('Major Specialization', 'Major Specialization'), ('Normal', 'Normal'), ('Minor Specialization', 'Minor Specialization')
    ]
    type = models.CharField(
        choices=col_choices,
        default='Normal',
        max_length=50,
        help_text='single specialization and multiple normal research fields'
    )
    name = models.CharField(max_length=100)
    # about should be static maybe
    add_date = models.DateTimeField(auto_now_add=True, null=True)


# for Position openings
class Book(models.Model):
    b_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    author = models.CharField(max_length=100, blank=True, help_text='Type as author1 | author2 | ... and so on ')
    year = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=100, blank=True)
    add_date = models.DateTimeField(auto_now_add=True, null=True)


# for Position openings
class Service(models.Model):
    b_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    tenure = models.CharField(max_length=1000)
    add_date = models.DateTimeField(auto_now_add=True, null=True)


