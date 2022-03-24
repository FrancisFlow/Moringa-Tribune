from django.test import TestCase
from .models import Editor, Article, Tags
import datetime as dt
# Create your tests here.
class EditorTestClass(TestCase):
    #set up method
    def setUp(self):
        self.francis=Editor(first_name='Francis', last_name="Karanja", email="francis@moringaschool.com")
    #test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.francis, Editor))


class ArticleTestClass(TestCase):
    def setUp(self):
        #Creating a new editor and saving
        self.francis=Editor(first_name='Francis', last_name="Karanja", email="francis@moringaschool.com")
    #creating a new tag and saving it
        self.new_tag=Tags(name='testing')
        self.new_tag.save()

        self.new_article=Article(title='Test Article', post='This is a random test Post', editor = self.francis)
        self.new_article.save()
        self.new_article.Tags.add(self.new_tag)

        def tearDown(self):
            Editor.objects.all().delete()
            Tags.objects.all().delete()
            Article.objects.all().delete()
        
        def test_get_news_today(self):
            today_news = Article.todays_news()
            self.assertTrue(len(today_news)>0)
        
        def test_get_news_by_date(self):
            test_date='2021-03-23'
            date=dt.datetime.striptime(test_date, '%Y-%m-%d').date()
            news_by_date=Article.days_news(date)
            self.assertTrue(len(news_by_date)==0)