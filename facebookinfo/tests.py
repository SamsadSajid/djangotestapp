from django.conf import settings
from selenium.webdriver.common.keys import Keys
import unittest
from selenium import webdriver
import facebook
import vcr
import re

with vcr.use_cassette('fixtures/vcr_cassettes/isaacasimov.yaml'):
    page_id="isaacasimov"
    graph = facebook.GraphAPI(access_token=settings.ACCESS_TOKEN,version='2.7')
    fields = 'name, id, posts.limit(20){name, created_time, comments.limit(20){from, message, created_time, comments.limit(20){from, message, created_time}}}'
    response = graph.get_object(page_id, fields=fields)
    assert 'Isaac' in str(response)

class FacebookinfoTestCase(unittest.TestCase):
    def setUp(self):
        self.page_name = 'isaacasimov'
        self.post_id = '735289683296645'
        self.home_url = 'http://127.0.0.1:8000/'
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_show_index_page(self):
        """
        Test that the index page shows correctly
        """
        driver = self.driver
        driver.get(self.home_url)
        self.assertIn("Please enter a Page or Post", driver.page_source)
        driver.find_element_by_tag_name("input")


    def test_show_facebook_page(self):
        driver = self.driver
        url = "{0}{1}".format(self.home_url, self.page_name)
        driver.get(url)

        h1 = driver.find_element_by_tag_name("h1")
        page_id = driver.find_element_by_id("page-id")
        driver.find_element_by_tag_name("input")
        post = driver.find_elements_by_css_selector("#post-id")[0]
        comment = driver.find_elements_by_css_selector(".comment .message")[0]
        subcomment = driver.find_elements_by_css_selector(".subcomment .message")[0]

        # Make sure I have posts, comments, and subcomments
        page_id_content = "293431410815810"
        post_content = "293431410815810_735289683296645"
        comment_content = "message: I don't remember the exact words but later on he also had law"
        subcomment_content = "message: But Danil Olivav, ONLY robot with that zero law"

        self.assertIn(page_id_content, page_id.text)
        self.assertIn(post_content, post.text)
        self.assertIn(comment_content, comment.text)
        self.assertIn(subcomment_content, subcomment.text)

    """
    TODO DRY these tests!
    """
    """
    TODO I want to check that a post I know
    will have:
    - a certain ammount of comments
    - a certain ammount of subcomments
    - that the post, comment and subcomments have the contents I need
    """
    def test_show_facebook_post(self):
        driver = self.driver
        url = "{0}{1}/posts/{2}".format(self.home_url, self.page_name, self.post_id)
        driver.get(url)

        h1 = driver.find_element_by_tag_name("h1")
        driver.find_element_by_tag_name("input")
        post = driver.find_element_by_id("post-id")
        comment = driver.find_elements_by_css_selector(".comment .message")[0]
        subcomment = driver.find_elements_by_css_selector(".subcomment .message")[0]

        # Make sure I have the post, comments, and subcomments
        post_content = "293431410815810_735289683296645"
        comment_content = "message: I don't remember the exact words but later on he also had law"
        subcomment_content = "message: But Danil Olivav, ONLY robot with that zero law"

        self.assertIn(post_content, post.text)
        self.assertIn(comment_content, comment.text)
        self.assertIn(subcomment_content, subcomment.text)
