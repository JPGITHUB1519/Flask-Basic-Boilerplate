#!flask/bin/python
import os
import unittest

class TestCase(unittest.TestCase):
    def setUp(self):
        # app.config['TESTING'] = True
        # app.config['WTF_CSRF_ENABLED'] = False
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        # self.app = app.test_client()
        # db.create_all()

    def tearDown(self):
        # db.session.remove()
        # db.drop_all()

    def test(self):
        print "Testing"

if __name__ == '__main__':
    unittest.main()