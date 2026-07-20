# a programming tool that lets you 
# interact with a database using the 
# same object-oriented code you write 
# in your application, instead of 
# writing raw SQL
 # Benefits of ORM
# Less SQL – aapko raw queries likhne ki zaroorat nahi.
# Database Independent – MySQL, PostgreSQL, SQLite sab ke saath kaam karega.
# Secure – SQL Injection ke chances bahut kam ho jate hain.
# Readable – Easy to maintain.


class Student(models.Model):
    name =  models.CharField()
    age= models.IntegerField()

    student = student.objects.all()

