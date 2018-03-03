import json

class Conf():
    value = []

    def load(self, file_name):
        file_config = open('./env/'+ file_name, 'r')

        try:
            self.value = json.loads(file_config.read())
        except ValueError:
            print("Error: file config invalid formated!")
            raise

        file_config.close()
