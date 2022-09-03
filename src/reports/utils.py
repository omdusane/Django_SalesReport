import base64, uuid
from django.core.files.base import ContentFile

def get_report_image(data):
    f , str_image = data.split(';base64')
    decoded_img = base64.b64decode(str_image)
    img_name = str(uuid.uuid4())[:10] + '.png'
    data = ContentFile(decoded_img, name=img_name)
    return data











#using this custom ajax method check as is_ajax() method is deprecated in django 4 
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
def ajax_test(request):
    return is_ajax(request=request)