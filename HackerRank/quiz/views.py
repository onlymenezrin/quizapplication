from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework import authentication,permissions

from quiz.serializers import CategorySerializer,QuestionSerializer,AnswerSerializer
from quiz.models import Category,Questions,Answers

from django_filters.rest_framework import DjangoFilterBackend


class CategoriesView(viewsets.ModelViewSet):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()
    # authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


#localhost:8000/api/v1/categories/{id}/add_question/
    @action(methods=["post"],detail=True)
    def add_question(self,request,*args,**kwargs):
        serializer=QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(category=self.get_object())
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

class QuestionsView(viewsets.ModelViewSet):
    serializer_class=QuestionSerializer
    queryset=Questions.objects.all()
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['mode','mark']
    # authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    # def list(self,request,*args,**kwargs):
    #     qs=Questions.objects.all()
    #     if "category" in request.query_params:
    #         cat=request.query_params.get("category")
    #         qs=qs.filter(category__name=cat)
    #     serializer=QuestionSerializer(qs,many=True) 
    #     return Response(data=serializer.data)   


#localhost:8000/api/v1/questions/{id}/add_answer/
    @action(methods=["post"],detail=True)
    def add_answer(self,request,*args,**kwargs):
        serializer=AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(question=self.get_object())
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
        