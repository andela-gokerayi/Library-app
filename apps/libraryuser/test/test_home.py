from django.test import TestCase

class HomePageTest(TestCase):

    # def test_homepage(self):
    #     url = "/home/"
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 302)
    #     # print '####'
    #     # print response
    #     # self.assertContains(response, 'login')
    #     # self.assertRedirects(response, '/home/', status_code=302, target_status_code=302 )


    def test_login(self):
        pass
        # TODO re-enable these tests
        # print "###"
        # import ipdb; ipdb.set_trace()
        # print self.client.login(username='admin', password='eniola')
        # response=self.client.get('/home/', follow=True)
        # print response
