import unittest
import requests
import https_get_requests as gr

class TestClass(unittest.TestCase):

    url_list = [
                requests.get("http://www.bbc.co.uk/iplayer"),
                requests.get("http://checkip.amazonaws.com"),
                requests.get("https://www.bbc.co.uk/missing/thing"),
                requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Juve nile_Ragdoll.jpg/220px-Juvenile_Ragdoll.jpg"),
                requests.get("https://site.mockito.org/")
                ]

    def test_area(self):
        bbc_response = TestClass.url_list[0].status_code

        self.assertEqual(bbc_response, gr.get_requests.create_json_data()[0]['Status-code'],
                        f'Status code is {bbc_response}')

if __name__ == '__main__':
    unittest.main()
