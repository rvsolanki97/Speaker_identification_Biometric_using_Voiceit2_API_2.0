import requests
import urllib


class VoiceIt2:
    base_URL = 'https://api.voiceit.io'
    version = '2.6.0'
    voiceit_basic_auth_credentials = ''
    notification_url = ''

    def __init__(self, key, token):
        self.voiceit_basic_auth_credentials = (key, token)
        self.headers = {'platformId': '28', 'platformVersion': self.version}

    def add_notification_url(self, url):
        self.notification_url = '?notificationURL=' + urllib.parse.quote(url, safe='')

    def remove_notification_url(self):
        self.notification_url = ''

    def get_all_users(self):
        try:
            response = requests.get(self.base_URL + '/users' + self.notification_url, auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def get_phrases(self, lang):
        try:
            response = requests.get(self.base_URL + '/phrases/' + str(lang) + self.notification_url, auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def create_user(self):
        try:
            response = requests.post(self.base_URL + '/users' + self.notification_url, auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()
    
    def create_unmanaged_sub_account(self, firstName, lastName, email, password, lang):
        dataObj = {}
        dataObj['firstName'] = firstName
        dataObj['contentLanguage'] = lang
        dataObj['lastName'] = lastName
        dataObj['email'] = email
        dataObj['password'] = password
        try:
            response = requests.post(self.base_URL + '/subaccount/unmanaged' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()
    
    def create_managed_sub_account(self, firstName, lastName, email, password, lang):
        dataObj = {}
        dataObj['firstName'] = firstName
        dataObj['contentLanguage'] = lang
        dataObj['lastName'] = lastName
        dataObj['email'] = email
        dataObj['password'] = password
        try:
            response = requests.post(self.base_URL + '/subaccount/managed' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()
    
    def switch_sub_account_type(self, subAccountAPIKey):
        try:
            response = requests.post(self.base_URL + '/subaccount/' + subAccountAPIKey + '/switchType' + self.notification_url, auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def regenerate_sub_account_api_token(self, sub_account_api_key):
        try:
            response = requests.post(self.base_URL + '/subaccount/' + str(sub_account_api_key) + self.notification_url, auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def delete_sub_account(self, sub_account_api_key):
        try:
            response = requests.delete(self.base_URL + '/subaccount/' + str(sub_account_api_key) + self.notification_url, auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()
    
    def check_user_exists(self, user_id):
        try:
            response = requests.get(self.base_URL + '/users/' + str(user_id) + self.notification_url, auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def delete_user(self, user_id):
        try:
            response = requests.delete(self.base_URL + '/users/' + str(user_id) + self.notification_url, auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def get_groups_for_user(self, user_id):
        try:
            response = requests.get(self.base_URL + '/users/' + str(user_id) + '/groups' + self.notification_url, auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def get_all_groups(self):
        try:
            response = requests.get(self.base_URL + '/groups' + self.notification_url, auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def get_group(self, group_id):
        try:
            response = requests.get(self.base_URL + '/groups/' + str(group_id) + self.notification_url, auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def group_exists(self, group_id):
        try:
            response = requests.get(self.base_URL + '/groups/' + str(group_id) + '/exists' + self.notification_url, auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def create_group(self, group_desc):
        dataObj = {}
        dataObj['description'] = group_desc
        try:
            response = requests.post(self.base_URL + '/groups' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def add_user_to_group(self, group_id, user_id):
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['userId'] = user_id
        try:
            response = requests.put(self.base_URL + '/groups/addUser' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def remove_user_from_group(self, group_id, user_id):
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['userId'] = user_id
        try:
            response = requests.put(self.base_URL + '/groups/removeUser' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def delete_group(self, group_id):
        try:
            response = requests.delete(self.base_URL + '/groups/' + str(group_id) + self.notification_url, auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def get_all_face_enrollments(self, user_id):
        try:
            response = requests.get(self.base_URL + '/enrollments/face/' + str(user_id) + self.notification_url, auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def get_all_voice_enrollments(self, user_id):
        try:
            response = requests.get(self.base_URL + '/enrollments/voice/' + str(user_id) + self.notification_url, auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def get_all_video_enrollments(self, user_id):
        try:
            response = requests.get(self.base_URL + '/enrollments/video/' + str(user_id) + self.notification_url, auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def create_voice_enrollment(self, user_id, lang, phrase, file_path=None, file_buffer=None):
        if not file_path and not file_buffer:
            raise Exception("file_path or file_buffer needs to be specified")
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        if file_path:
            f = open(file_path, 'rb')
        if file_buffer:
            f = file_buffer
        filesObj = [('recording', ('enrollment.wav', f, 'audio/wav'))]
        try:
            response = requests.post(self.base_URL + '/enrollments/voice' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj, headers=self.headers)
            f.close()
            return response.json()
        except requests.exceptions.HTTPError as e:
            f.close()
            return e.read()

    def create_voice_enrollment_by_url(self, user_id, lang, phrase, file_Url):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        dataObj['fileUrl'] = file_Url
        try:
            response = requests.post(self.base_URL + '/enrollments/voice/byUrl' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def create_face_enrollment(self, user_id, file_path=None, file_buffer=None):
        if not file_path and not file_buffer:
            raise Exception("file_path or file_buffer needs to be specified")
        dataObj = {}
        dataObj['userId'] = user_id
        if file_path:
            f = open(file_path, 'rb')
        if file_buffer:
            f = file_buffer
        filesObj = [('video', ('video.mp4', f, 'video/mp4'))]
        try:
            response = requests.post(self.base_URL + '/enrollments/face' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj, headers=self.headers)
            f.close()
            return response.json()
        except requests.exceptions.HTTPError as e:
            f.close()
            return e.read()

    def create_face_enrollment_by_url(self, user_id, file_Url):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['fileUrl'] = file_Url
        try:
            response = requests.post(self.base_URL + '/enrollments/face/byUrl' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def create_video_enrollment(self, user_id, lang, phrase, file_path=None, file_buffer=None):
        if not file_path and not file_buffer:
            raise Exception("file_path or file_buffer needs to be specified")
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        if file_path:
            f = open(file_path, 'rb')
        if file_buffer:
            f = file_buffer
        filesObj = [('video', ('video.mp4', f, 'video/mp4'))]
        try:
            response = requests.post(self.base_URL + '/enrollments/video' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj, headers=self.headers)
            f.close()
            return response.json()
        except requests.exceptions.HTTPError as e:
            f.close()
            return e.read()

    def create_video_enrollment_by_url(self, user_id, lang, phrase, file_Url):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        dataObj['fileUrl'] = file_Url
        try:
            response = requests.post(self.base_URL + '/enrollments/video/byUrl' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def delete_all_enrollments(self, user_id):
        try:
            response = requests.delete(self.base_URL + '/enrollments/' + str(user_id) + '/all' + self.notification_url, auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
                return e.read()

    def voice_verification(self, user_id, lang, phrase, file_path=None, file_buffer=None):
        if not file_path and not file_buffer:
            raise Exception("file_path or file_buffer needs to be specified")
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        if file_path:
            f = open(file_path, 'rb')
        if file_buffer:
            f = file_buffer
        filesObj = [('recording', ('verification.wav', f, 'audio/wav'))]
        try:
            response = requests.post(self.base_URL + '/verification/voice' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj, headers=self.headers)
            f.close()
            return response.json()
        except requests.exceptions.HTTPError as e:
            f.close()
            return e.read()

    def voice_verification_by_url(self, user_id, lang, phrase, file_Url):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        dataObj['fileUrl'] = file_Url
        try:
            response = requests.post(self.base_URL + '/verification/voice/byUrl' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def face_verification(self, user_id, file_path=None, file_buffer=None):
        if not file_path and not file_buffer:
            raise Exception("file_path or file_buffer needs to be specified")
        dataObj = {}
        dataObj['userId'] = user_id
        if file_path:
            f = open(file_path, 'rb')
        if file_buffer:
            f = file_buffer
        filesObj = [('video', ('video.mp4', f, 'video/mp4'))]
        try:
            response = requests.post(self.base_URL + '/verification/face' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj, headers=self.headers)
            f.close()
            return response.json()
        except requests.exceptions.HTTPError as e:
            f.close()
            return e.read()

    def face_verification_by_url(self, user_id, file_Url):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['fileUrl'] = file_Url
        try:
            response = requests.post(self.base_URL + '/verification/face/byUrl' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def video_verification(self, user_id, lang, phrase, file_path=None, file_buffer=None):
        if not file_path and not file_buffer:
            raise Exception("file_path or file_buffer needs to be specified")
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        if file_path:
            f = open(file_path, 'rb')
        if file_buffer:
            f = file_buffer
        filesObj = [('video', ('video.mp4', f, 'video/mp4'))]
        try:
            response = requests.post(self.base_URL + '/verification/video' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj, headers=self.headers)
            f.close()
            return response.json()
        except requests.exceptions.HTTPError as e:
            f.close()
            return e.read()

    def video_verification_by_url(self, user_id, lang, phrase, file_Url):
        dataObj = {}
        dataObj['userId'] = user_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        dataObj['fileUrl'] = file_Url
        try:
            response = requests.post(self.base_URL + '/verification/video/byUrl' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def voice_identification(self, group_id, lang, phrase, file_path=None, file_buffer=None):
        if not file_path and not file_buffer:
            raise Exception("file_path or file_buffer needs to be specified")
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        if file_path:
            f = open(file_path, 'rb')
        if file_buffer:
            f = file_buffer
        filesObj = [('recording', ('identification.wav', f, 'audio/wav'))]
        try:
            response = requests.post(self.base_URL + '/identification/voice' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj, headers=self.headers)
            f.close()
            return response.json()
        except requests.exceptions.HTTPError as e:
            f.close()
            return e.read()

    def voice_identification_by_url(self, group_id, lang, phrase, file_Url):
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        dataObj['fileUrl'] = file_Url
        try:
            response = requests.post(self.base_URL + '/identification/voice/byUrl' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def video_identification(self, group_id, lang, phrase, file_path=None, file_buffer=None):
        if not file_path and not file_buffer:
            raise Exception("file_path or file_buffer needs to be specified")
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        if file_path:
            f = open(file_path, 'rb')
        if file_buffer:
            f = file_buffer
        filesObj = [('video', ('video.mp4', f, 'video/mp4'))]
        try:
            response = requests.post(self.base_URL + '/identification/video' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj, headers=self.headers)
            f.close()
            return response.json()
        except requests.exceptions.HTTPError as e:
            f.close()
            return e.read()

    def video_identification_by_url(self, group_id, lang, phrase, file_Url):
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['contentLanguage'] = lang
        dataObj['phrase'] = phrase
        dataObj['fileUrl'] = file_Url
        try:
            response = requests.post(self.base_URL + '/identification/video/byUrl' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def face_identification(self, group_id, file_path=None, file_buffer=None):
        if not file_path and not file_buffer:
            raise Exception("file_path or file_buffer needs to be specified")
        dataObj = {}
        dataObj['groupId'] = group_id
        if file_path:
            f = open(file_path, 'rb')
        if file_buffer:
            f = file_buffer
        filesObj = [('video', ('video.mp4', f, 'video/mp4'))]
        try:
            response = requests.post(self.base_URL + '/identification/face' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, files=filesObj, headers=self.headers)
            f.close()
            return response.json()
        except requests.exceptions.HTTPError as e:
            f.close()
            return e.read()

    def face_identification_by_url(self, group_id, file_Url):
        dataObj = {}
        dataObj['groupId'] = group_id
        dataObj['fileUrl'] = file_Url
        try:
            response = requests.post(self.base_URL + '/identification/face/byUrl' + self.notification_url, auth=self.voiceit_basic_auth_credentials, data=dataObj, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def create_user_token(self, user_id, seconds_to_timeout):
        try:
            response = requests.post(self.base_URL + '/users/' + user_id + '/token' + '?timeOut=' + str(seconds_to_timeout), auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()

    def expire_user_tokens(self, user_id):
        try:
            response = requests.post(self.base_URL + '/users/' + user_id + '/expireTokens', auth=self.voiceit_basic_auth_credentials, headers=self.headers)
            return response.json()
        except requests.exceptions.HTTPError as e:
            return e.read()
