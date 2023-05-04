from django.shortcuts import render, redirect
from .models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer

class UserList(APIView) :
    """
    유저 생성
    /user/
    """
    def post(self, request, format = None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    유저 조회
    /user/
    """
    def get(self,request, format = None):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    """
    특정 유저 조회
    /user/{pk}/
    """
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    """
    특정 유저 수정
    /user/{pk}/
    """
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    특정 유저 삭제
    /user/{pk}/
    """
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)

        err_data = {}
        if not (username and useremail and password and re_password):
            err_data['error'] = '모든 값을 입력해주세요.'

        elif password != re_password:
            err_data['error'] = '비밀번호가 다릅니다.'

        else:
            user = User(
                username=username,
                useremail=useremail,
                password=make_password(password),
            )
            user.save()

        return render(request, 'register.html', err_data)

def login(request):
    if request.method =='GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)

        err_data = {}
        if not(useremail and password):
            err_data['error'] = '모든 값을 입력해 주세요.'
        else:
            user = User.objects.get(useremail=useremail)
            if check_password(password, user.password):
                request.session['user'] = user.id
                return redirect('/')
            else:
                err_data['error'] = '비밀번호가 일치하지 않습니다.'
        return render(request, 'register.html', err_data)


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk = user_id)
        return HttpResponse("Hello! %s님" % user)
    else:
        return HttpResponse("로그인 해주세요!")

