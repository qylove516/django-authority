import re
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse, HttpResponseRedirect


class ValidPermission(MiddlewareMixin):

    def process_request(self, request):
        # 定义白名单
        current_path = request.path_info
        white_list = ['/user/login/', '/user/reg/', '/admin/.*']
        for p in white_list:
            ret = re.match(p, current_path)
            if ret:
                return None
        if not request.session.get('permissions'):
            return HttpResponseRedirect('/user/login/')

        # 权限控制
        permissions = request.session.get('permissions', [])
        for item in permissions.values():
            urls = item.get("urls"  )
            for p in urls:
                p = '^{path}$'.format(path=p)
                ret = re.match(p, current_path)
                if ret:
                    request.actions = item.get("actions")
                    return None
        return HttpResponse('你没有访问权限！')
