# myapp/renderers.py
from rest_framework.renderers import JSONRenderer
from rest_framework import status

class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_status = renderer_context.get('response').status_code
        if status.is_success(response_status):
            response_data = {
                'msg': 'success',
                'data': data,
            }
        else:
            response_data = {
                'msg': 'failed',
                'error': data,
            }

        return super().render(response_data, accepted_media_type, renderer_context)
